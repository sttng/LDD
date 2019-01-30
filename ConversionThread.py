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
from BrickLoader import BrickLoader

#Locate db.lif on OSX
find_db_lif_command = "mdfind -name db.lif"
path_to_lif = commands.getoutput(find_db_lif_command)

# define the name of the temp directory to be created
path_to_lif_tmp_dir = os.getcwd() + '/liftmp'
path_to_lif_tmp = path_to_lif_tmp_dir + '/db.lif'

class ConversionThread:

	@staticmethod
	def run():
		#print('\tExtracting Assets.lif..')
		#ConversionThread.extractLif('Assets.lif')
		try:
			os.mkdir(path_to_lif_tmp_dir)
		except OSError:
			print ("Creation of the directory %s failed" % path_to_lif_tmp_dir)
		else:
			print ("Successfully created the directory %s" % path_to_lif_tmp_dir)
			shutil.copy2(path_to_lif, path_to_lif_tmp)
			print('\tExtracting temp db.lif..')
			ConversionThread.extract_lif(path_to_lif_tmp)
		
		files_to_convert = []
		files_to_convert = glob.glob(os.path.join(path_to_lif_tmp_dir + '/db/Primitives/LOD0', '*.g'))
		
		for geometry_file in files_to_convert:
			my_geo = BrickLoader.load_geometry_file(geometry_file)
			BrickLoader.obj_saver(my_geo)


	@staticmethod
	def extract_lif(LIFFilePath):
	
		lif_extractor_command = 'python LIFExtractor.py ' + '\'' + LIFFilePath +'\''
		print lif_extractor_command
		try:
		#this is hacky, should rather import LIFExtractor.py
			os.system(lif_extractor_command)
				
		except IOError as e:
			print('\tERROR: Failed to read LIF file.')
			return False
				
ConversionThread.run()

#LIFReader.openLIFFile('~/Library/Application Support/LEGO Company/LEGO Digital Designer/db.lif')
