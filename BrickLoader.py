#!/usr/bin/env python

#
# Version 0.1 - Copyright (c) 2019 by 
#
# Updates:
#
# License:
#		   -  MIT License
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
	def loadGeometryFile(fileToConvert):
	
		try:
			with open(fileToConvert, 'rb') as f:
	
				if(not(os.path.isfile(fileToConvert)) or os.path.splitext(fileToConvert)[1] != ".g"):
					print("\tERROR: The supplied file is not a LDD geometry .g file.")
					return False
				
				verticesList= []
				normalsList = []
				indicesList = []
				GeometryFileDict = dict()
				
				print fileToConvert
				skipData = f.read(4)
				vertexCount = struct.unpack("<L", f.read(4))[0]
				indexCount = struct.unpack("<L", f.read(4))[0]
				
				skipData = f.read(4)
				for i in range(0, 3*vertexCount):
					x = struct.unpack("f", f.read(4))[0]
					verticesList.append(x)
					x
				for i in range(0, 3*vertexCount):
					x = struct.unpack("f", f.read(4))[0]
					normalsList.append(x)
					
				for i in range(0, indexCount):
					x = struct.unpack("<L", f.read(4))[0]
					indicesList.append(x)
				
				GeometryFileDict["vertices"] = verticesList
				GeometryFileDict["normals"] = normalsList
				GeometryFileDict["indices"] = indicesList
				
				return GeometryFileDict
				
								
		except IOError as e:
			print('\tERROR: Failed to read .g file.')
			return False
			
			
	@staticmethod
	def OBJSaver(GeometryFileDict, fileToConvert):
		partNumber = os.path.splitext(os.path.basename(fileToConvert))[0]
		with open(partNumber + '.obj', 'w') as the_file:
			the_file.write('o brick_' + partNumber + '\n')
			the_file.write('g ' + partNumber + '\n')
			for i in range(0, len(GeometryFileDict["vertices"]), 3):
				the_file.write('v ' + str(GeometryFileDict["vertices"][i]) + ' ' + str(GeometryFileDict["vertices"][i + 1]) + ' ' + str(GeometryFileDict["vertices"][i + 2]) + ' ' + '\n')
			the_file.write('\n')
			for i in range(0, len(GeometryFileDict["normals"]), 3):
				the_file.write('vn ' + str(GeometryFileDict["normals"][i]) + ' ' + str(GeometryFileDict["normals"][i + 1]) + ' ' + str(GeometryFileDict["normals"][i + 2]) + ' ' + '\n')
			the_file.write('\n')
			for i in range(0, len(GeometryFileDict["indices"]), 3):
				index1 = GeometryFileDict["indices"][i + 0] + 1
				index2 = GeometryFileDict["indices"][i + 1] + 1
				index3 = GeometryFileDict["indices"][i + 2] + 1
				
				the_file.write('f ' + str(index1) + '//' + str(index1) + ' ' + str(index2) + '//' + str(index2) + " " + str(index3) + '//' + str(index3) + '\n')
				
			the_file.close()
		return True
		
myGeo = BrickLoader.loadGeometryFile('./liftmp/db/Primitives/LOD0/95342.g')

BrickLoader.OBJSaver(myGeo,'./liftmp/db/Primitives/LOD0/95342.g')
