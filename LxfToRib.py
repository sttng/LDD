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
import shutil
import math
from BrickReader import BrickReader
import ObjToRib2
import xml.etree.ElementTree as ET
import numpy as np
import csv
import zlib
import random

compression = zipfile.ZIP_DEFLATED


# Checks if a matrix is a valid rotation matrix.
def isRotationMatrix(R) :
	Rt = np.transpose(R)
	shouldBeIdentity = np.dot(Rt, R)
	I = np.identity(3, dtype = R.dtype)
	n = np.linalg.norm(I - shouldBeIdentity)
	return n < 1e-6


# Calculates rotation matrix to euler angles.
def rotationMatrixToEulerAngles(R):
 
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
	
	with zipfile.ZipFile('Bricks_Archive.zip', 'w') as myzip:
		lst = tree.findall('Bricks/Brick/Part')
		processed_brick = dict()
		for item in lst:
			design_id = item.get('designID')
			materials = item.get('materials')
			material_ids = materials.split(',')
			material_string = '_'.join(material_ids)
			processed = design_id + '_' + material_string
			
			if processed in processed_brick:
				# Don't process bricks twice
				continue
			else:
				
				BrickReader.read_brick(design_id)
				
				ObjToRib2.export_obj_to_rib(design_id + '.obj', material_ids)
				myzip.write(design_id + '_' + material_string + '.rib', compress_type=compression)
				os.remove(design_id + '_' + material_string + '.rib')
				os.remove(design_id + '.obj')
				processed_brick[processed] = True
			

def export_to_rib(lxf_filename):

	archive = zipfile.ZipFile(lxf_filename, 'r')
	lxfml_file = archive.read('IMAGE100.LXFML')
	trans_xyz = []
	minx = 1000
			
	ribfile = os.path.splitext(os.path.basename(lxf_filename))[0]
	with open(ribfile + '.rib', 'w') as file_writer:
	
		cam_tree = ET.fromstring(lxfml_file)
		cam_lst = cam_tree.findall('Cameras/Camera')
		for item in cam_lst:
			fov = item.get('fieldOfView')
			dist = item.get('distance')
			cam_trans = item.get('transformation')
		
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
		file_writer.write('\tAttributeBegin\n\t\tAttribute "visibility" "int indirect" [0] "int transmission" [0]\n\t\tAttribute "visibility" "int camera" [1]\n\t\tRotate 50 0 1 0\n\t\tRotate -90 1 0 0\n\t\tLight "PxrDomeLight" "domeLight" "string lightColorMap" ["GriffithObservatory.tex"]\n\tAttributeEnd\n')
		tree = ET.fromstring(lxfml_file)
		
		lst = tree.findall('Bricks/Brick/Part')
		
		
		for item in lst:
			design_id = item.get('designID')
			materials = item.get('materials')
			material_ids = materials.split(',')
			material_string = '_'.join(material_ids)
				
			for sub in item:
				transformation = sub.get('transformation')
					
			transformation_array = transformation.split(',')
			trans_xyz = (transformation_array[9], transformation_array[10], str((-1) * float(transformation_array[11]))) # left vs right handed coord system
			
			# get lowest brick translation for floor plane
			if minx > float(transformation_array[9]):
				minx = transformation_array[9]
			
			R = np.array([[float(transformation_array[0]), float(transformation_array[1]) ,float(transformation_array[2])], [ float(transformation_array[3]), float(transformation_array[4]) ,float(transformation_array[5])], [ float(transformation_array[6]), float(transformation_array[7]) ,float(transformation_array[8])]])
			b = np.array([1, 0, 0])
			
			rotx, roty, rotz = rotationMatrixToEulerAngles(R)
			rotz = (-1) * rotz #Renderman is lefthanded coordinate system, but LDD is right handed.
			
			file_writer.write('\tAttributeBegin\n')
			rand = str(0.9) #str(random.uniform(0.999, 1))
			file_writer.write('\t\t#Translate ' + trans_xyz[0] + ' ' + trans_xyz[1] + ' ' + trans_xyz[2] + '\n')
			file_writer.write('\t\t#Rotate ' + str(math.degrees(rotx)) + ' 1 0 0\n')
			file_writer.write('\t\t#Rotate ' + str(math.degrees(roty)) + ' 0 1 0\n')
			file_writer.write('\t\t#Rotate ' + str(math.degrees(rotz)) + ' 0 0 1\n')
			file_writer.write('\t\tConcatTransform [' 
			+ transformation_array[0] + ' ' + transformation_array[1] + ' ' + str((-1) * float(transformation_array[2])) + ' 0 ' 
			+ transformation_array[3] + ' ' + transformation_array[4] + ' ' + str((-1) * float(transformation_array[5])) + ' 0 ' 
			+ str((-1) * float(transformation_array[6])) + ' ' + str((-1) * float(transformation_array[7])) + ' ' + transformation_array[8] + ' 0 ' 
			+ trans_xyz[0] + ' ' + trans_xyz[1] + ' ' + trans_xyz[2] + ' 1]\n')
			#file_writer.write('\tScale ' + rand + ' ' + rand + ' ' + rand + '\n') #Random brick size for seams.
			file_writer.write('\t\tScale 1 1 1\n')
			file_writer.write('\t\tAttribute "identifier" "name" ["'+ design_id + '_' + material_string +'"]\n')
			file_writer.write('\t\tReadArchive "Bricks_Archive.zip!'+ design_id + '_' + material_string + '.rib"\n')
			file_writer.write('\tAttributeEnd\n\n')
		
		file_writer.write('\tAttributeBegin\n')
		file_writer.write('\t\tAttribute "identifier" "string name" ["plane1"]')
		file_writer.write('\t\tTranslate ' + minx + ' ' +'0 10\n')
		file_writer.write('\t\tScale 100 1 100')
		file_writer.write('\t\tPolygon "P" [-0.5 0 -0.5  -0.5 0 0.5  0.5 0 0.5  0.5 0 -0.5]')
		file_writer.write('\t\t"st" [0 0  0 1  1 1  1 0]')
		file_writer.write('\tAttributeEnd\n\n')
		file_writer.write('WorldEnd\n')
	
	file_writer.close()
	return True


def generate_master_scene(lxf_filename):
	lxf_extension = os.path.splitext(os.path.basename(lxf_filename))[1]
	lxf_filename = os.path.splitext(os.path.basename(lxf_filename))[0]
	with open('test_scene.rib','wb') as wfd:
		for f in ['template.rib',lxf_filename + '.rib']:
			with open(f,'rb') as fd:
				shutil.copyfileobj(fd, wfd, 1024*1024*10)
	os.remove(lxf_filename + '.rib')
	print 'Success: Created rib scene from ' + lxf_filename + lxf_extension
	
	
def main():
	lxf_filename = sys.argv[1]
	
	generate_bricks(lxf_filename)
	
	export_to_rib(lxf_filename)
	
	generate_master_scene(lxf_filename)
	
if __name__ == "__main__":
	main()
