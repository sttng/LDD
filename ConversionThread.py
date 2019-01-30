#!/usr/bin/env python

#
# Version 0.1 - Copyright (c) 2019 by 
#
# Updates:
#
# License:
#		   -  BSD 3-Clause License
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

#Locate db.lif on OSX
findDbLif = "mdfind -name db.lif"
pathToLif = commands.getoutput(findDbLif)

# define the name of the temp directory to be created
pathToLifTmpDir = os.getcwd() + '/liftmp'
pathToLifTmp = pathToLifTmpDir + '/db.lif'
print pathToLifTmpDir


class ConversionThread:

	@staticmethod
	def run():
		#print('\tExtracting Assets.lif..')
		#ConversionThread.extractLif('Assets.lif')
		try:
			os.mkdir(pathToLifTmpDir)
		except OSError:
			print ("Creation of the directory %s failed" % pathToLifTmpDir)
		else:
			print ("Successfully created the directory %s " % pathToLifTmpDir)
			shutil.copy2(pathToLif, pathToLifTmp)
			print('\tExtracting temp db.lif..')
			ConversionThread.extractLif(pathToLifTmp)
		
		filesToConvert = []
		filesToConvert = glob.glob(os.path.join(pathToLifTmpDir + '/db/Primitives/LOD0', '*.g') )
		print filesToConvert

	@staticmethod
	def extractLif(LIFFilePath):
	
		LIFExtractorCommand = 'python LIFExtractor.py ' + '\'' + LIFFilePath +'\''
		print LIFExtractorCommand
		try:
		#this is hacky, should rather import LIFExtractor.py
			os.system(LIFExtractorCommand)
				
		except IOError as e:
			print('\tERROR: Failed to read LIF file.')
			return False
				
ConversionThread.run()

#LIFReader.openLIFFile('~/Library/Application Support/LEGO Company/LEGO Digital Designer/db.lif')
