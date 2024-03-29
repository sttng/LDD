#!/usr/bin/env python
 
#
# Version 0.1 - Copyright (c) 2019 by 
#
# Updates:
#
# License: MIT License
#

import os
import io
import sys
import glob
import platform
import subprocess
import binascii
import signal
import stat
import struct
import shutil
import argparse
import tempfile
import commands
import shutil
import array

input_brick = sys.argv[1]

#Locate db.lif on macOS
if platform.system() == 'Darwin':
	find_db_lif_command = "mdfind -name db.lif"
	path_to_lif = commands.getoutput(find_db_lif_command)
	
#Locate db.lif on Windows	
elif platform.system() == 'Windows':
	find_db_lif_command = "dir db.lif /s /p"
	path_to_lif = commands.getoutput(find_db_lif_command)
	
# define the name of the temp directory to be created
path_to_lif_tmp_dir = os.path.join(os.getcwd(), 'liftmp')
path_to_lif_tmp = os.path.join(path_to_lif_tmp_dir, 'db.lif')


class BrickReader:

	@staticmethod
	def read_brick(partnumber):
	
		files_to_convert = []
		files_to_convert = glob.glob(os.path.join(path_to_lif_tmp_dir, 'db', 'Primitives', 'LOD0', str(partnumber) + '.g*'))
		# Ensure that g is always the first, then g1, g2, ....
		files_to_convert.sort()
		geometry_file_dict_list = []
		
		if not files_to_convert:
			#print("Brick not found. Possibly assembly")
			return False
		#print 'Brick ' + partnumber + ' consist of ' + str(len(files_to_convert)) + ' files.\n'
		
		# Various similar extensions like g, .g1, .g2, ..., .g8 exist if the brick is composed of multiple parts.
		# The .g file is the 'base_brick' usually.
		for geometry_file in files_to_convert:
			
			brick = BrickReader.load_single_geometry_file(geometry_file)
			geometry_file_dict_list.append(brick)
				
		BrickReader.export_to_obj(geometry_file_dict_list)
		
		return True
		
	@staticmethod
	def load_single_geometry_file(geometry_file):
	
		try:
			with open(geometry_file, 'rb') as file_reader:
				
				vertices_list = []
				normals_list = []
				indices_list = []
				tex_coords_list = []
				geometry_file_dict = dict()
				
				partnumber = os.path.splitext(os.path.basename(geometry_file))[0]
				part_extension = os.path.splitext(os.path.basename(geometry_file))[1]
				geometry_file_dict["partnumber"] = partnumber
				geometry_file_dict["part_extension"] = part_extension
					
				fourcc = file_reader.read(4) 
				if(fourcc != "10GB"):
					print("\tERROR: Not a .gX file. Expected 10GB file header but read:" + fourcc)
					return False
					
				vertex_count = struct.unpack("<L", file_reader.read(4))[0]
				indices_count = struct.unpack("<L", file_reader.read(4))[0]
				geometry_file_dict["vertex_count"] = vertex_count
				geometry_file_dict["indices_count"] = indices_count
				
				# options flag:
				# options & 0x01 == uv_texture_coords_enabled then texture_coords_count = 2 * vertex_count
				# options & 0x10 == unknown
				# options & 0x20 == unknown
				# options & 0x02 == then vertices, normals
				# options & 0x08 == then vertices only ?
				options = binascii.hexlify(file_reader.read(4))
				
				for i in range(0, 3 * vertex_count):
					vertex = struct.unpack("f", file_reader.read(4))[0]
					vertices_list.append(vertex)
					
				for i in range(0, 3 * vertex_count):
					normal = struct.unpack("f", file_reader.read(4))[0]
					normals_list.append(normal)
					
				geometry_file_dict["vertices"] = vertices_list
				geometry_file_dict["normals"] = normals_list

				# uv_texture_coords_enabled
				if (options == '3b000000'):
							
					for i in range(0, 2 * vertex_count):
						tex_coord = struct.unpack("f", file_reader.read(4))[0]
						tex_coords_list.append(tex_coord)
						
					geometry_file_dict["uv_texture_coords_enabled"] = True
					geometry_file_dict["tex_coords"] = tex_coords_list
					# print partnumber + part_extension
					
				# no uv_texture_coords
				elif (options == '3a000000'):
					
					geometry_file_dict["uv_texture_coords_enabled"] = False
					# print partnumber + part_extension
				
				# no uv_texture_coords, flex part
				elif (options == '3e000000'):
					
					geometry_file_dict["uv_texture_coords_enabled"] = False
					#print 'Options: ' + options + ' in ' + partnumber + part_extension
				
				# uv_texture_coords, flex part
				elif (options == '3f000000'):
					
					for i in range(0, 2 * vertex_count):
						tex_coord = struct.unpack("f", file_reader.read(4))[0]
						tex_coords_list.append(tex_coord)
						
					geometry_file_dict["uv_texture_coords_enabled"] = True
					geometry_file_dict["tex_coords"] = tex_coords_list
					#print 'Options: ' + options + ' in ' + partnumber + part_extension
				
				else:
					print '\tERROR: Unknown Options: ' + options + ' in ' + partnumber + part_extension
					return false
				
				for i in range(0, indices_count):
					index = struct.unpack("<L", file_reader.read(4))[0]
					indices_list.append(index)
				
				geometry_file_dict["indices"] = indices_list
				
				return geometry_file_dict
									
		except IOError as e:
			print('\tERROR: Failed to read .gX file.')
			return False
	
	
	@staticmethod
	def export_to_obj(geometry_file_dict_list):
		primitive = 0
		offset = 1
		uv_offset = 1
		partnumber = geometry_file_dict_list[0]["partnumber"]
		
		with open(partnumber + '.obj', 'w') as file_writer:
			file_writer.write('o brick_' + partnumber + '\n')
		
			for geometry_file_dict in geometry_file_dict_list:
				
				file_writer.write('g ' + str(primitive) + '\n')
				file_writer.write('# From file: ' + geometry_file_dict["partnumber"] + geometry_file_dict["part_extension"] + '\n')
				
				for i in range(0, len(geometry_file_dict["vertices"]), 3):
					file_writer.write('v ' + str(geometry_file_dict["vertices"][i]) + ' ' + str(geometry_file_dict["vertices"][i + 1]) + ' ' + str(geometry_file_dict["vertices"][i + 2]) + '\n')
		
				for i in range(0, len(geometry_file_dict["normals"]), 3):
					file_writer.write('vn ' + str(geometry_file_dict["normals"][i]) + ' ' + str(geometry_file_dict["normals"][i + 1]) + ' ' + str(geometry_file_dict["normals"][i + 2]) + '\n')
		
				if (geometry_file_dict["uv_texture_coords_enabled"] == True):
					for i in range(0, len(geometry_file_dict["tex_coords"]), 2):
						file_writer.write('vt ' + str(geometry_file_dict["tex_coords"][i]) + ' ' + str(geometry_file_dict["tex_coords"][i + 1]) + '\n')
			
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
		
				primitive += 1
				offset += geometry_file_dict["vertex_count"]
		
				if (geometry_file_dict["uv_texture_coords_enabled"] == True):
					uv_offset += geometry_file_dict["vertex_count"]
					
		file_writer.close()
					
		return True
		
#BrickReader.read_brick(input_brick)
