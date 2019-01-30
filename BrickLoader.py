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
import zipfile
import commands
import shutil

class BrickLoader:

	@staticmethod
	def load_geometry_file(file_to_convert):
	
		try:
			with open(file_to_convert, 'rb') as file_reader:
	
				if(not(os.path.isfile(file_to_convert)) or os.path.splitext(file_to_convert)[1] != ".g"):
					print("\tERROR: The supplied file is not a LDD geometry .g file.")
					return False
				
				vertices_list= []
				normals_list = []
				indices_list = []
				geometry_file_dict = dict()
				
				partnumber = os.path.splitext(os.path.basename(file_to_convert))[0]
				
				skip = file_reader.read(4)
				vertex_count = struct.unpack("<L", file_reader.read(4))[0]
				indices_count = struct.unpack("<L", file_reader.read(4))[0]
				
				skip = file_reader.read(4)
				for i in range(0, 3*vertex_count):
					vertex = struct.unpack("f", file_reader.read(4))[0]
					vertices_list.append(vertex)
					
				for i in range(0, 3*vertex_count):
					normal = struct.unpack("f", file_reader.read(4))[0]
					normals_list.append(normal)
					
				for i in range(0, indices_count):
					index = struct.unpack("<L", file_reader.read(4))[0]
					indices_list.append(index)
				
				geometry_file_dict["vertices"] = vertices_list
				geometry_file_dict["normals"] = normals_list
				geometry_file_dict["indices"] = indices_list
				geometry_file_dict["partnumber"] = partnumber
				
				return geometry_file_dict
				
								
		except IOError as e:
			print('\tERROR: Failed to read .g file.')
			return False
			
			
	@staticmethod
	def obj_saver(geometry_file_dict):
		partnumber = geometry_file_dict["partnumber"]
		with open(partnumber + '.obj', 'w') as file_writer:
			file_writer.write('o brick_' + partnumber + '\n')
			file_writer.write('g ' + partnumber + '\n')
			for i in range(0, len(geometry_file_dict["vertices"]), 3):
				file_writer.write('v ' + str(geometry_file_dict["vertices"][i]) + ' ' + str(geometry_file_dict["vertices"][i + 1]) + ' ' + str(geometry_file_dict["vertices"][i + 2]) + ' ' + '\n\n')
			
			for i in range(0, len(geometry_file_dict["normals"]), 3):
				file_writer.write('vn ' + str(geometry_file_dict["normals"][i]) + ' ' + str(geometry_file_dict["normals"][i + 1]) + ' ' + str(geometry_file_dict["normals"][i + 2]) + ' ' + '\n\n')
			
			for i in range(0, len(geometry_file_dict["indices"]), 3):
				index1 = geometry_file_dict["indices"][i + 0] + 1
				index2 = geometry_file_dict["indices"][i + 1] + 1
				index3 = geometry_file_dict["indices"][i + 2] + 1
				
				file_writer.write('f ' + str(index1) + '//' + str(index1) + ' ' + str(index2) + '//' + str(index2) + " " + str(index3) + '//' + str(index3) + '\n')
				
			file_writer.close()
		return True
		
#myGeo = BrickLoader.load_geometry_file('./liftmp/db/Primitives/LOD0/95342.g')
#BrickLoader.obj_saver(myGeo)
