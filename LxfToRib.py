#!/usr/bin/env python

#
# Version 0.1 - Copyright (c) 2019 by 
#
# Updates:
#
# License: MIT License
#

import os
import sys
import re
import unicodedata
import zipfile
import math
from BrickReader import BrickReader
from ObjToRib import ObjToRib
import xml.etree.ElementTree as ET
import numpy as np
import csv


# Checks if a matrix is a valid rotation matrix.
def isRotationMatrix(R) :
	Rt = np.transpose(R)
	shouldBeIdentity = np.dot(Rt, R)
	I = np.identity(3, dtype = R.dtype)
	n = np.linalg.norm(I - shouldBeIdentity)
	return n < 1e-6


# Calculates rotation matrix to euler angles.
def rotationMatrixToEulerAngles(R) :
 
	#assert(isRotationMatrix(R))
	
	sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
	
	singular = sy < 1e-6

	if not singular :
		x = math.atan2(R[2,1] , R[2,2])
		y = math.atan2(-R[2,0], sy)
		z = math.atan2(R[1,0], R[0,0])
	else :
		x = math.atan2(-R[1,2], R[1,1])
		y = math.atan2(-R[2,0], sy)
		z = 0
 
	return np.array([x, y, z])

	
def generate_bricks(lxf_filename):

	archive = zipfile.ZipFile(lxf_filename, 'r')
	lxfml_file = archive.read('IMAGE100.LXFML')
	
	tree = ET.fromstring(lxfml_file)
	lst = tree.findall('Bricks/Brick')
	for item in lst:
		design_id = item.get('designID')
		print design_id
		BrickReader.read_brick(design_id)
		ObjToRib.export_obj_to_rib(design_id + '.obj')


def export_to_rib(lxf_filename):

	archive = zipfile.ZipFile(lxf_filename, 'r')
	lxfml_file = archive.read('IMAGE100.LXFML')
	trans_xyz =[]
	
	material_id_dict = {}
	with open('lego_colors.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(csvfile) # skip the first row
		for row in reader:
			material_id_dict[row[0]] = row[6], row[7], row[8]
			#print(row)
			
	ribfile = os.path.splitext(os.path.basename(lxf_filename))[0]
	with open(ribfile + '.rib', 'w') as file_writer:
	
		cam_tree = ET.fromstring(lxfml_file)
		cam_lst = cam_tree.findall('Cameras/Camera')
		for item in cam_lst:
			fov = item.get('fieldOfView')
			dist = item.get('distance')
			cam_trans = item.get('transformation')
			
		print fov
		print dist
		
		transformation_array = cam_trans.split(',')
		
		R = np.array([[float(transformation_array[0]), float(transformation_array[1]) ,float(transformation_array[2])], [ float(transformation_array[3]), float(transformation_array[4]) ,float(transformation_array[5])], [ float(transformation_array[6]), float(transformation_array[7]) ,float(transformation_array[8])]])
		
		rotx, roty, rotz = rotationMatrixToEulerAngles(R)
		rotz = (-1) * rotz #Renderman is lefthanded coordinate system, but LDD is right handed.
			
		file_writer.write('#Rotate ' + str(math.degrees(rotx)) + ' 1 0 0\n')
		file_writer.write('#Rotate ' + str(math.degrees(roty)) + ' 0 1 0\n')
		file_writer.write('#Rotate ' + str(math.degrees(rotz)) + ' 0 0 1\n')
		
		file_writer.write('#ConcatTransform [' 
			+ transformation_array[0] + ' ' + transformation_array[1] + ' ' + str((-1) * float(transformation_array[2])) + ' 0 ' 
			+ transformation_array[3] + ' ' + transformation_array[4] + ' ' + str((-1) * float(transformation_array[5])) + ' 0 ' 
			+ str((-1) * float(transformation_array[6])) + ' ' + str((-1) * float(transformation_array[7])) + ' ' + transformation_array[8] + ' 0 ' 
			+ transformation_array[9] + ' ' + transformation_array[10] + ' ' + transformation_array[11] + ' 1]\n')
	
		file_writer.write('WorldBegin\n')
		file_writer.write('\tTranslate 0 0 10\n')
		file_writer.write('\tScale 0.7 0.7 0.7\n')
		file_writer.write('\tRotate -25 1 0 0\n')
		file_writer.write('\tRotate 45 0 1 0\n')
		file_writer.write('\tLight \"PxrDomeLight\" \"domeLight\" \"string lightColorMap\" [\"GriffithObservatory.tex\"]\n')
	
		tree = ET.fromstring(lxfml_file)
		lst = tree.findall('Bricks/Brick')
		
		for item in lst:
			design_id = item.get('designID')
			for subelem in item:
				material_id = subelem.get('materials')
				
				for sub in subelem:
					transformation = sub.get('transformation')
					
			transformation_array = transformation.split(',')
			trans_xyz = (transformation_array[9], transformation_array[10], str((-1) * float(transformation_array[11]))) # left vs right handed coord system
			
			R = np.array([[float(transformation_array[0]), float(transformation_array[1]) ,float(transformation_array[2])], [ float(transformation_array[3]), float(transformation_array[4]) ,float(transformation_array[5])], [ float(transformation_array[6]), float(transformation_array[7]) ,float(transformation_array[8])]])
			b = np.array([1, 0, 0])
			
			try:
				color_r, color_g, color_b = material_id_dict[material_id]
				
			except KeyError:
				color_r, color_g, color_b = [100, 100, 100]

			color_r = round((float(color_r) / 255),2)
			color_g = round((float(color_g) / 255),2)
			color_b = round((float(color_b) / 255),2)
			
			rotx, roty, rotz = rotationMatrixToEulerAngles(R)
			rotz = (-1) * rotz #Renderman is lefthanded coordinate system, but LDD is right handed.
			
			file_writer.write('\tAttributeBegin\n')
			file_writer.write('\t\t#Translate ' + trans_xyz[0] + ' ' + trans_xyz[1] + ' ' + trans_xyz[2] + '\n')
			file_writer.write('\t\t#Rotate ' + str(math.degrees(rotx)) + ' 1 0 0\n')
			file_writer.write('\t\t#Rotate ' + str(math.degrees(roty)) + ' 0 1 0\n')
			file_writer.write('\t\t#Rotate ' + str(math.degrees(rotz)) + ' 0 0 1\n')
			file_writer.write('\t\tConcatTransform [' 
			+ transformation_array[0] + ' ' + transformation_array[1] + ' ' + str((-1) * float(transformation_array[2])) + ' 0 ' 
			+ transformation_array[3] + ' ' + transformation_array[4] + ' ' + str((-1) * float(transformation_array[5])) + ' 0 ' 
			+ str((-1) * float(transformation_array[6])) + ' ' + str((-1) * float(transformation_array[7])) + ' ' + transformation_array[8] + ' 0 ' 
			+ trans_xyz[0] + ' ' + trans_xyz[1] + ' ' + trans_xyz[2] + ' 1]\n')
			file_writer.write('\t\tScale 1 1 1\n')
			file_writer.write('\t\tBxdf \"PxrSurface\" \"terminal.bxdf\" \"color diffuseColor\" [' + str(color_r) + ' ' + str(color_g) + ' ' + str(color_b) + '] \"float specularRoughness\" [0.008] \"color specularEdgeColor\" [0.45 0.45 0.45]\n')
			file_writer.write('\t\tAttribute \"identifier\" \"name" [\"'+ design_id +'\"]\n')
			file_writer.write('\t\tReadArchive \"'+ design_id + '.rib\"\n')
			file_writer.write('\tAttributeEnd\n\n')
			
		file_writer.write('WorldEnd\n')
	
	file_writer.close()
	return True
	
	
def main():
	lxf_filename = sys.argv[1]
	
	generate_bricks(lxf_filename)
	
	export_to_rib(lxf_filename)
	
	
if __name__ == "__main__":
	main()
