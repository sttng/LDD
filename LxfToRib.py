#!/usr/bin/env python

#
# Version 0.1 - Copyright (c) 2019 by 
# Scans lxf file, writes ribs of bricks, places them in scene.rib
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
useplane = True #defines if plane for the ground should be there or not.


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


# Scan the lxf file for parts / bricks and put rib versions of these with correct material (color) 
# and decoration (texture) into 'Bricks_Archive.zip' 
def generate_bricks(lxf_filename):

	archive = zipfile.ZipFile(lxf_filename, 'r')
	lxfml_file = archive.read('IMAGE100.LXFML')
	# After we read in the full path to the LXF file, we only need the name later, so we split here
	lxf_filename = os.path.splitext(os.path.basename(lxf_filename))[0]
	
	tree = ET.fromstring(lxfml_file)
	
	with zipfile.ZipFile(lxf_filename + '_Bricks_Archive.zip', 'w') as myzip:
		lst = tree.findall('Bricks/Brick/Part')
		processed_brick = dict()
		processed_deco = dict()
		for item in lst:
			design_id = item.get('designID')
			materials = item.get('materials')
			decorations = item.get('decoration')
			material_id_list = materials.split(',')
			material_string = '_' + '_'.join(material_id_list)
			decoration_id_list = False
			processed = design_id + material_string
			
			if decorations != None and decorations != '0':
				# We have decorations
				decoration_id_list = decorations.split(',')
				for decoration in decoration_id_list:
					if decoration != '0' and decoration not in processed_deco:
						# Don't process decorations twice
						txmake_cmd = '/Applications/Pixar/RenderManProServer-22.4/bin/txmake -t:8 -compression zip -mode clamp -resize up ./liftmp/db/Decorations/' + decoration + '.png ' + decoration + '.tex'
						os.system(txmake_cmd)
						#myzip.write(decoration + '.tex', compress_type=compression)
						#os.remove(decoration + '.tex')
						processed_deco[decoration] = True
				
				decoration_string = '_' + '_'.join(decoration_id_list)
				processed = design_id + material_string + decoration_string

			if processed not in processed_brick:
				# Don't process bricks twice
				BrickReader.read_brick(design_id)
				written_rib = ObjToRib2.export_obj_to_rib(design_id + '.obj', material_id_list, decoration_id_list)
				myzip.write(written_rib + '.rib', compress_type=compression)
				os.remove(written_rib + '.rib')
				os.remove(design_id + '.obj')
				processed_brick[processed] = True
				

# Scan the lxf file and create a rib scene file, referencing the parts / bricks, and move them to correct position with correct rotation.
def export_to_rib(lxf_filename):

	archive = zipfile.ZipFile(lxf_filename, 'r')
	lxfml_file = archive.read('IMAGE100.LXFML')
	lxf_filename = os.path.splitext(os.path.basename(lxf_filename))[0]
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
		
		file_writer.write('''\n# Camera Minus One
TransformBegin
	ConcatTransform [''' 
		+ transformation_array[0] + ''' ''' + transformation_array[1] + ''' ''' + transformation_array[2] + ''' 0 \n'''
		+ transformation_array[3] + ''' ''' + transformation_array[4] + ''' ''' + transformation_array[5] + ''' 0 \n'''
		+ transformation_array[6] + ''' ''' + transformation_array[7] + ''' ''' + transformation_array[8] + ''' 0 \n'''
		+ str((0.1) * float(transformation_array[9])) + ''' ''' + str((0.1) * float(transformation_array[10])) + ''' ''' + transformation_array[11] + ''' 1]
	# Distance: '''+ dist + '''
	Camera "Cam--1" 
		"float shutterOpenTime" [0] 
		"float shutterCloseTime" [1] 
		"int apertureNSides" [0] 
		"float apertureAngle" [0] 
		"float apertureRoundness" [0] 
		"float apertureDensity" [0] 
		"float dofaspect" [1] 
		"float nearClip" [0.100000001] 
		"float farClip" [10000]
TransformEnd\n''')
		
		R = np.array([[float(transformation_array[0]), float(transformation_array[1]) ,float(transformation_array[2])], [ float(transformation_array[3]), float(transformation_array[4]) ,float(transformation_array[5])], [ float(transformation_array[6]), float(transformation_array[7]) ,float(transformation_array[8])]])
		
		rotx, roty, rotz = rotationMatrixToEulerAngles(R)
		rotz = (-1) * rotz #Renderman is lefthanded coordinate system, but LDD is right handed.
		
		file_writer.write('''\n# Camera Zero
TransformBegin
	#Translate ''' + str((0.1) * float(transformation_array[9])) + ''' ''' + str((0.1) * float(transformation_array[10])) + ''' ''' + transformation_array[11] + '''
	Translate 0 0 40
	Rotate ''' + str(math.degrees(roty)) + ''' 1 0 0
	#Rotate -25 1 0 0
	Rotate ''' + str(math.degrees(rotx)) + ''' 0 1 0
	#Rotate 45 0 1 0
	#Rotate ''' + str(math.degrees(rotz)) + ''' 0 0 1
	Camera "Cam-0"
		"float shutterOpenTime" [0] 
		"float shutterCloseTime" [1] 
		"int apertureNSides" [0] 
		"float apertureAngle" [0] 
		"float apertureRoundness" [0] 
		"float apertureDensity" [0] 
		"float dofaspect" [1] 
		"float nearClip" [0.100000001] 
		"float farClip" [10000]
TransformEnd\n''')
		
		file_writer.write('''
Display "''' + ribfile + '''.beauty.001.exr" "openexr" "Ci,a,mse,albedo,albedo_var,diffuse,diffuse_mse,specular,specular_mse,zfiltered,zfiltered_var,normal,normal_var,forward,backward" "int asrgba" 1
	"string storage" ["scanline"]
	"string exrpixeltype" ["half"]
	"string compression" ["zips"]
	"float compressionlevel" [45]
	"string camera" ["Cam-0"]\n\n''')
		
		file_writer.write('WorldBegin\n')
		file_writer.write('\tScale 1 1 1\n')
		file_writer.write('''\tAttributeBegin
		Attribute "visibility" "int indirect" [0] "int transmission" [0]
		Attribute "visibility" "int camera" [1]
		Rotate 50 0 1 0
		Rotate -90 1 0 0
		Light "PxrDomeLight" "domeLight" "string lightColorMap" ["islandsun_small.tex"]
	AttributeEnd\n''')
		
		tree = ET.fromstring(lxfml_file)
		lst = tree.findall('Bricks/Brick/Part')
		
		for item in lst:
			design_id = item.get('designID')
			materials = item.get('materials')
			decorations = item.get('decoration')
			material_id_list = materials.split(',')
			material_string = '_' + '_'.join(material_id_list)
			decoration_string = '' # in case of decoration set string from empty ('') to the values so to use later.
			
			if decorations != None and decorations != '0':
				# We have decorations
				decoration_ids = decorations.split(',')
				decoration_string = '_' + '_'.join(decoration_ids)
			
			name = design_id + material_string + decoration_string
			
			for sub in item:
				transformation = sub.get('transformation')
					
			transformation_array = transformation.split(',')
			trans_xyz = (transformation_array[9], transformation_array[10], str((-1) * float(transformation_array[11]))) # left vs right handed coord system
			
			# get lowest brick translation for floor plane
			if minx > float(transformation_array[9]):
				minx = transformation_array[9]
			
			file_writer.write('\tAttributeBegin\n')
			#rand = str(0.9) #str(random.uniform(0.999, 1)) #Random brick size for seams.
			
			file_writer.write('\t\tConcatTransform [' 
			+ transformation_array[0] + ' ' + transformation_array[1] + ' ' + str((-1) * float(transformation_array[2])) + ' 0 ' 
			+ transformation_array[3] + ' ' + transformation_array[4] + ' ' + str((-1) * float(transformation_array[5])) + ' 0 ' 
			+ str((-1) * float(transformation_array[6])) + ' ' + str((-1) * float(transformation_array[7])) + ' ' + transformation_array[8] + ' 0 ' 
			+ trans_xyz[0] + ' ' + trans_xyz[1] + ' ' + trans_xyz[2] + ' 1]\n')
			
			#file_writer.write('\tScale ' + rand + ' ' + rand + ' ' + rand + '\n') #Random brick size for seams.
			
			file_writer.write('\t\tScale 1 1 1\n')
			file_writer.write('\t\tAttribute "identifier" "name" ["'+ name + '"]\n')
			file_writer.write('\t\tReadArchive "' + lxf_filename +'_Bricks_Archive.zip!'+ name + '.rib"\n')
			file_writer.write('\tAttributeEnd\n\n')
		
		if useplane: # write the floor plane in case True
			file_writer.write('''\tAttributeBegin
		Attribute "identifier" "string name" ["groundplane"]
		Translate ''' + minx +''' 0 10
		Scale 200 1 200
		Polygon "P" [-0.5 0 -0.5  -0.5 0 0.5  0.5 0 0.5  0.5 0 -0.5]
		"st" [0 0  0 1  1 1  1 0]
	AttributeEnd\n\n)'''
	
file_writer.write('''WorldEnd\n''')
	
	file_writer.close()
	return True


# append rib scence based on lxf file to 'template.rib'
def generate_master_scene(lxf_filename):
	lxf_extension = os.path.splitext(os.path.basename(lxf_filename))[1]
	lxf_filename = os.path.splitext(os.path.basename(lxf_filename))[0]
	with open(lxf_filename + '_Scene.rib','wb') as wfd:
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
