#!/usr/bin/env python

#
# Version 0.1 - Copyright (c) 2019 by 
#
# Info:
# This script will read in  a.obj file, construct geometry from it
# and write out a rib file of it.
#
# Updates:
#
# License: MIT License
#
# Polygon "P" [ 1 1 0 0 4 5 0 9 0 ]
# Polygon "P" [ 0 1 0 0 8 0 4 4 0 ] "N" [ 1 0 0 1 0 0 0 1 0 ]
# RiPolygon (3, "P", (float *)p, "N", (float *)n, RI_NULL);
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


obj_file = sys.argv[1]


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
		verts.append(l)
	
	if 'vn ' in line and '.' in line:
		line = line.rstrip()
		l = ['%.3f' % float(num) for num in line.split(' ') if 'vn' not in num]
		normals.append(l)
	
	if 'f ' in line and '/' in line:
		l = []
		for nums in line.split(' '):
			if 'f' not in nums:
				l.append(int(nums.split('/')[0]))
		faces.append(l)

# Create polygons
f2.write('# Brick' + name)
f2.write('\nAttributeBegin')
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
	
f2.write('\nAttributeEnd\n')
f2.close()
