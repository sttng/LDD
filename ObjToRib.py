#!/usr/bin/env python

#
# Version 0.1 - Copyright (c) 2019 by 
#
# Info:
# This script will read in .obj files, construct geometry from them
# and write out a rib file for each of them.
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

from subprocess import call
from os import listdir
from os.path import isfile, join, splitext

# file information
template_path = os.getcwd() + '/templates'
obj_path = template_path + '/obj_files'
rib_path = template_path + '/rib_files'


# get .obj file list
obj_files_list = [ f for f in listdir(obj_path) if isfile(join(obj_path,f)) and '.obj' in f]


# read template file to allow easy adjustment later
t = open(template_path + '/template.rib')
temp = t.readlines()
template = []
for line in temp:
	if '\n' in line:
		line = line.split('\n')[0]
	template.append(line)

for obj_file in obj_files_list:
	# read and store .obj file
	f1 = open(obj_path + '/' + obj_file)
	lines = f1.readlines()
	f1lines = []
	for line in lines:
		if '\n' in line:
			line = line.split('\n')[0]
		f1lines.append(line)
	f1.close()


	# create and append rib file based on template
	name = splitext(obj_file)[0]
	f2 = open(rib_path + '/' + name + '.rib', 'w')
	lineNum = 0
	for line in template:
		lineNum += 1
		if ('RENAME' in line):
			n = splitext(fileName)[0]
			f2.write('\t\"' + n + '.jpg\"\n')
		else:
			f2.write(line + '\n')
			if 'WorldBegin' in line:
				break


	# convert obj file lines to rib compatible format
	verts = []
	faces = []
	for line in f1lines:
		if 'v ' in line and '.' in line:
			line = line.rstrip()
			l = ['%.3f' % float(num) for num in line.split(' ') if 'v' not in num]
			verts.append(l)
		if 'f ' in line and '/' in line:
			l = []
			for nums in line.split(' '):
				if 'f' not in nums:
					l.append(int(nums.split('/')[0]))
			faces.append(l)
	
	# create polygons
	f2.write('\nAttributeBegin')
	f2.write('\nSurface \"matte\"')
	f2.write('\nColor [ 1 1 1 ]')
	for face in faces:
		f2.write('\n\tPolygon')
		newline = ''
		for i in xrange(0, len(face), 1):
			for j in xrange(0, len(verts[face[i]-1]), 1):
				newline += str(verts[face[i]-1][j]) + ' '
		f2.write("\n\t\t\"P\" [ " + newline + "]")
	f2.write('\nAttributeEnd')
	
	
	# finish and close file
	for i in range(lineNum, len(template)):
		f2.write(template[i] + '\n')
	f2.close()
