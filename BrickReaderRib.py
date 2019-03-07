#!/usr/bin/env python
 
#
# Version 0.1 - Copyright (c) 2019 by 
#
# Updates:
# Still untested code and probably doesn't work.
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
import BrickReader

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
path_to_lif_tmp_dir = os.getcwd() + '/liftmp'
path_to_lif_tmp = path_to_lif_tmp_dir + '/db.lif'


class BrickReaderRib:

	@staticmethod
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
				
		BrickReaderRib.export_to_rib(geometry_file_dict_list)
		return True


	@staticmethod
	def export_to_rib(geometry_file_dict_list):
		offset = 1
		uv_offset = 1
		partnumber = geometry_file_dict_list[0]["partnumber"]
		
		with open(partnumber + '.rib', 'w') as file_writer:
			file_writer.write('##RenderMan RIB-Structure 1.1 Entity')
		
			for geometry_file_dict in geometry_file_dict_list:
			
				file_writer.write('\nAttributeBegin #begin Brick ' + geometry_file_dict["partnumber"] + geometry_file_dict["part_extension"])
				file_writer.write('\nAttribute \"identifier\" \"uniform string name\" [\"' + geometry_file_dict["partnumber"] + geometry_file_dict["part_extension"] + '\"]'
								
				for i in range(0, len(geometry_file_dict["vertices"]), 3):
					file_writer.write('\n\t\t"P" [' + str(geometry_file_dict["vertices"][i]) + ' ' + str(geometry_file_dict["vertices"][i + 1]) + ' ' + str(geometry_file_dict["vertices"][i + 2]) + ' ' + ']')
		
				for i in range(0, len(geometry_file_dict["normals"]), 3):
					file_writer.write('\n\t\t"N" [' + str(geometry_file_dict["normals"][i]) + ' ' + str(geometry_file_dict["normals"][i + 1]) + ' ' + str(geometry_file_dict["normals"][i + 2]) + ' ' + ']')
		
				if (geometry_file_dict["uv_texture_coords_enabled"] == True):
					for i in range(0, len(geometry_file_dict["tex_coords"]), 2):
						file_writer.write('\n\t\t"facevarying float [2] uv0" [' + str(geometry_file_dict["tex_coords"][i]) + ' ' + str(geometry_file_dict["tex_coords"][i + 1]) + ' ' + ']')
			
					for i in range(0, len(geometry_file_dict["indices"]), 3):
						index0 = geometry_file_dict["indices"][i + 0] + offset
						index1 = geometry_file_dict["indices"][i + 1] + offset
						index2 = geometry_file_dict["indices"][i + 2] + offset
						index3 = geometry_file_dict["indices"][i + 0] + uv_offset
						index4 = geometry_file_dict["indices"][i + 1] + uv_offset
						index5 = geometry_file_dict["indices"][i + 2] + uv_offset
						#file_writer.write('f ' + str(index0) + '/' + str(index3) + '/' + str(index0) + ' ' + str(index1) + "/" + str(index4) + '/' + str(index1) + ' ' + str(index2) + "/" + str(index5) + '/' + str(index2) + '\n')
				
				elif (geometry_file_dict["uv_texture_coords_enabled"] == False):
				
					for i in range(0, len(geometry_file_dict["indices"]), 3):
						index0 = geometry_file_dict["indices"][i + 0] + offset
						index1 = geometry_file_dict["indices"][i + 1] + offset
						index2 = geometry_file_dict["indices"][i + 2] + offset
						#file_writer.write('f ' + str(index0) + '//' + str(index0) + ' ' + str(index1) + '//' + str(index1) + " " + str(index2) + '//' + str(index2) + '\n')
		
				offset += geometry_file_dict["vertex_count"]
		
				if (geometry_file_dict["uv_texture_coords_enabled"] == True):
					uv_offset += geometry_file_dict["vertex_count"]
				
				file_writer.write('\nAttributeEnd #end Brick ' + geometry_file_dict["partnumber"] + geometry_file_dict["part_extension"])
					
		file_writer.close()		
		return True
	

BrickReaderRib.read_brick(input_brick)
