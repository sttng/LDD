#!/usr/bin/env python
import os
import sys

def create(path):
	# Set the directory you want to start from
	rootDir = '.'
	for dirName, subdirList, fileList in os.walk(rootDir):
		print('Found directory: %s' % dirName)
			for fname in fileList:
				print('\t%s' % fname)

#Detect if executable or not.
fileName = sys.argv[0].split(os.sep).pop()
if(fileName[-3:] == ".py" or fileName[-4:] == ".pyw"):
	runCommand = "python " + fileName
else:
	runCommand = fileName

if(len(sys.argv) > 1):
	for i in range(1, len(sys.argv)):
		create(sys.argv[i])
else:
	print("LIF Creator 1.0\n\nThis program will create LIF archives from a folder.\n\nCOPYRIGHT:\n\t(C) 2020 sttng\n\nLICENSE:\n\tGNU GPLv3\n\tYou accept full responsibility for how you use this program.\n\nUSEAGE:\n\t" + runCommand + " <FILE_PATH>")
