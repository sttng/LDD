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
import xml.etree.ElementTree as ET
import numpy as np
import csv
		
def read_brick(partnumber):
	
	files_to_convert = []
	files_to_convert = glob.glob(os.path.join(path_to_lif_tmp_dir + '/db/Primitives/LOD0', str(partnumber) + '.g*'))
	geometry_file_dict_list = []
	print 'Brick ' + partnumber + ' consist of ' + str(len(files_to_convert)) + ' files.\n'
		
	# Various similar extensions like g, .g1, .g2, ..., .g8 exist if the brick is composed of multiple parts. 
	# The .g file is the 'base_brick'. Currently no difference between 'base_brick' and 'additional geometry' implemented.
	for geometry_file in files_to_convert:
		
		geometry_file_dict = BrickReader.load_single_geometry_file(geometry_file)
		geometry_file_dict_list.append(geometry_file_dict)
				
	return geometry_file_dict_list
	
	
def transform_brick(geometry_file_dict_list, T):

	for geometry_file_dict in geometry_file_dict_list:
	
		for i in range(0, len(geometry_file_dict["vertices"]), 3):
		
			v = np.array([geometry_file_dict["vertices"][i], geometry_file_dict["vertices"][i+1], geometry_file_dict["vertices"][i+2], 1])
			v_t = dot(v,T)
			
			n = np.array([geometry_file_dict["normals"][i], geometry_file_dict["normals"][i+1], geometry_file_dict["normals"][i+2], 1])
			n_t = dot(n,T)
			
			for i in range(0, len(v_t) - 1): #take x,y,z value, omit the 'added' 1
				vertices_list.append(v_t[i])
				normals_list.append(n_t[i])
		
		# update the list with the new values (which are the result of the vector x matrix multiplication)
		geometry_file_dict["vertices"] = vertices_list
		geometry_file_dict["normals"] = normals_list
	
	return geometry_file_dict_list


def export_to_obj(lxf_filename):

	archive = zipfile.ZipFile(lxf_filename, 'r')
	lxfml_file = archive.read('IMAGE100.LXFML')
	
	material_id_dict = {}
	with open('lego_colors.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(csvfile) # skip the first row
		for row in reader:
			material_id_dict[row[0]] = row[6], row[7], row[8]
			
	objfile = os.path.splitext(os.path.basename(lxf_filename))[0]
	with open(objfile + '.obj', 'w') as file_writer:
	
		tree = ET.fromstring(lxfml_file)
		lst = tree.findall('Bricks/Brick')
		
		for item in lst:
			design_id = item.get('designID')
			for subelem in item:
				material_id = subelem.get('materials')
				
				for sub in subelem:
					transformation = sub.get('transformation')
					
			transformation_array = transformation.split(',')
			
			# Read the current brick into a list (as bricks my be build of sub-bricks)
			geometry_file_dict_list = read_brick(design_id)
			
			T = np.array([[transformation_array[0], transformation_array[1], transformation_array[2], 0],
                     [transformation_array[3], transformation_array[4], transformation_array[5], 0],
					 [transformation_array[6], transformation_array[7], transformation_array[8], 0],
                     [transformation_array[9], transformation_array[10], transformation_array[11], 1]])
			
			# Rotate and transpose (T matrix) the brick based on the LXF file info
			geometry_file_dict_list = transform_brick(geometry_file_dict_list, T)
			
			file_writer.write('o brick_' + partnumber + '\n')	
			
			for geometry_file_dict in geometry_file_dict_list:
				
				file_writer.write('g ' + geometry_file_dict["partnumber"] + geometry_file_dict["part_extension"] + '\n')
				file_writer.write('# From file: ' + geometry_file_dict["partnumber"] + geometry_file_dict["part_extension"] + '\n')
				
				for i in range(0, len(geometry_file_dict["vertices"]), 3):
					file_writer.write('v ' + str(geometry_file_dict["vertices"][i]) + ' ' + str(geometry_file_dict["vertices"][i + 1]) + ' ' + str(geometry_file_dict["vertices"][i + 2]) + ' ' + '\n\n')
		
				for i in range(0, len(geometry_file_dict["normals"]), 3):
					file_writer.write('vn ' + str(geometry_file_dict["normals"][i]) + ' ' + str(geometry_file_dict["normals"][i + 1]) + ' ' + str(geometry_file_dict["normals"][i + 2]) + ' ' + '\n\n')
		
				if (geometry_file_dict["uv_texture_coords_enabled"] == True):
					for i in range(0, len(geometry_file_dict["tex_coords"]), 2):
						file_writer.write('vt ' + str(geometry_file_dict["tex_coords"][i]) + ' ' + str(geometry_file_dict["tex_coords"][i + 1]) + ' ' + '\n\n')
			
					for i in range(0, len(geometry_file_dict["indices"]), 3):
						index0 = geometry_file_dict["indices"][i + 0] + offset
						index1 = geometry_file_dict["indices"][i + 1] + offset
						index2 = geometry_file_dict["indices"][i + 2] + offset
						index3 = geometry_file_dict["indices"][i + 0] + uv_offset
						index4 = geometry_file_dict["indices"][i + 1] + uv_offset
						index5 = geometry_file_dict["indices"][i + 2] + uv_offset
				
						file_writer.write('f ' + str(index0) + '/' + str(index3) + '/' + str(index0) + ' ' + str(index1) + "/" + str(index4) + '/' + str(index1) + ' ' + str(index2) + "/" + str(index5) + '/' + str(index2) + '\n')
				
				elif (geometry_file_dict["uv_texture_coords_enabled"] == False):
				
					for i in range(0, len(geometry_file_dict["indices"]), 3):
						index0 = geometry_file_dict["indices"][i + 0] + offset
						index1 = geometry_file_dict["indices"][i + 1] + offset
						index2 = geometry_file_dict["indices"][i + 2] + offset
				
						file_writer.write('f ' + str(index0) + '//' + str(index0) + ' ' + str(index1) + '//' + str(index1) + " " + str(index2) + '//' + str(index2) + '\n')
		
				offset += geometry_file_dict["vertex_count"]
		
				if (geometry_file_dict["uv_texture_coords_enabled"] == True):
					uv_offset += geometry_file_dict["vertex_count"]			
			
		file_writer.write('\n\n')
	
	file_writer.close()
	return True
	
	
def main():
	lxf_filename = sys.argv[1]
	
	export_to_obj(lxf_filename)
	
	
if __name__ == "__main__":
	main()
