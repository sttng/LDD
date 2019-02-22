#!/usr/bin/env python

#
# Version 0.1 - Copyright (c) 2019 by 
#
# Info:
# This script will read in a.obj file, construct geometry from it
# and write out a rib file of it.
#
# Updates:
#
# License: MIT License
#
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
import argparse
import commands
import shutil
import array


obj_file = sys.argv[1]


class ObjToRib:

	@staticmethod
	def export_obj_to_rib(obj_file):

		f1 = open(obj_file)
		lines = f1.readlines()
		f1lines = []
		for line in lines:
			if '\n' in line:
				line = line.split('\n')[0]
			f1lines.append(line)
		f1.close()
		
		
		name = obj_file.split(".")
		name = name[0]
		f2 = open(name + '.rib', 'w')
		
		# Convert obj file lines to rib compatible format
		verts = []
		faces = []
		normals =[]
		for line in f1lines:
			if 'v ' in line and '.' in line:
				line = line.rstrip()
				l = ['%.3f' % float(num) for num in line.split(' ') if 'v' not in num]
				l[2] = ((-1) * float(l[2])) #obj is right handed, rib is left handed coordinate system -> the z-axis is inverted
				verts.append(l)
			
			if 'vn ' in line and '.' in line:
				line = line.rstrip()
				l = ['%.3f' % float(num) for num in line.split(' ') if 'vn' not in num]
				l[2] = ((-1) * float(l[2])) #obj is right handed, rib is left handed coordinate system -> the z-axis is inverted
				normals.append(l)
			
			if 'f ' in line and '/' in line:
				l = []
				for nums in line.split(' '):
					if 'f' not in nums:
						l.append(int(nums.split('/')[0]))
				faces.append(l)
		
		# Create polygons
		
		f2.write('##RenderMan RIB-Structure 1.1 Entity')
		f2.write('\nAttributeBegin #begin Brick ' + name)
		f2.write('\nAttribute \"identifier\" \"uniform string name\" [\"' + name + '\"]')
		
		for face in faces:
			f2.write('\n\tPolygon')
			
			newline = ''
			for i in xrange(0, len(face), 1):
				for j in xrange(0, len(verts[face[i]-1]), 1):
					newline += str(verts[face[i]-1][j]) + ' '
			f2.write('\n\t\t\"P\" [ ' + newline + ']')
			
			newline = ''
			for i in xrange(0, len(face), 1):
				for j in xrange(0, len(normals[face[i]-1]), 1):
					newline += str(normals[face[i]-1][j]) + ' '
			f2.write(' \"N\" [ ' + newline + ']')
			# Add code for uv texture coords later here
			#f2.write(' \"facevarying float [2] uv1\" [ ' + newline + ']')
			#f2.write(' \"facevarying float [2] uv2\" [ ' + newline + ']')
			
		f2.write('\nAttributeEnd #end Brick ' + name + '\n')
		f2.close()
		
		return True


#ObjToRib.export_obj_to_rib(obj_file)
