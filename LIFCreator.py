#!/usr/bin/env python

"""
	LIF Creator - LEGO Digital Designer LIF Creator.

	Copyright (C) 2020 sttng

	You accept full responsibility for how you use this program.

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


import os
import sys
import struct
import time
import shutil

if sys.version_info < (3, 0):
	reload(sys)
	sys.setdefaultencoding('utf-8')

class LIFHeader:
	'''
	LIF Header (18 bytes total):
	4 bytes	Char[4]	Header (ASCI = 'LIFF')
	4 bytes	Int32	Spacing (Always equals 0)
	4 bytes	Int32	Total file size (Int32 big endian)
	2 bytes	Int16	Value "1" (Int16 big endian)
	4 bytes	Int32	Spacing (Always equals 0)
	'''
	
	def __init__(self):
		self.magic = b'LIFF'			#Magic Word (ASCI = 'LIFF')
		self.spacing1 = struct.pack('>I', 0)	#Spacing (Always equals 0)
		self.size = struct.pack('>I',3405691582)#0xCAFEBABE - Just to test and also to verify that header size is set correct later
		self.spacing2 = struct.pack('>H', 1)	#Value "1" (Int16 big endian)
		self.spacing3 = struct.pack('>I', 0)	#Spacing (Always equals 0)

	def setSize(self, size):
		self.size = struct.pack('>I', size)

	def getSize(self):
		return struct.unpack('>I', self.size)[0]
	
	def string(self):
		out = self.magic + self.spacing1 + self.size + self.spacing2 + self.spacing3
		return out

class LIFBlock:	
	'''
	LIF Block (20 bytes + data):
	2 bytes	Int16	Block start/header (always 1)
	2 bytes	Int16	Block type (1 to 5)
	4 bytes		Spacing1 (Always equals 0)
	4 bytes	Int32	Block size in bytes (includes header and data)
	4 bytes		Spacing2 (Equals 1 for block types 2,4 and 5)
	4 bytes		Spacing3 (Always equals 0)
	X bytes		The block content/data.
	
	The block type 1 is the "root block" and its size includes the remainder of the LIF file.
	The block type 2 contains the files content/data. The block content seems hard-coded and it is always 1 (Int16) and 0 (Int32).
	The block type 3 represents a folder. The block content is a hierarchy of type 3 and 4 blocks.
	The block type 4 represents a file. The block data is the file content/data.
	The block type 5 contains the files and folders names and some more information. 
	The block content is a hierarchy of LIF entries.
	Note: The block header is 20 bytes total. The data size is equal to the specified size - 20 bytes.
	'''
	
	def __init__(self, blocktype, data):
		self.blockheader = struct.pack('>H', 1)		#Block start/header (always 1)
		self.blocktype = struct.pack('>H', blocktype)	#Block type (1 to 5)
		self.spacing1 = struct.pack('>I', 0)		#Spacing (Always equals 0)
								#Block size in bytes (includes header and data) <- calculated later
		if blocktype == 1 or blocktype == 3:
			self.spacing2 = struct.pack('>I', 0)
		else:
			self.spacing2 = struct.pack('>I', 1)	#Spacing (Equals 1 for block types 2,4 and 5)
		self.spacing3 = struct.pack('>I', 0)		#Spacing (Always equals 0)
		if blocktype == 2:
			self.data = b'\x00\x01\x00\x00\x00\x00'	#The block content seems hard-coded for blocktype 2 and is always 1 (Int16) and 0 (Int32)
		else:
			self.data = data
		
		self.size = struct.pack('>I',len(self.data)+20)	#Block size in bytes (includes header and data)

	def setSize(self, size):
		self.size = struct.pack('>I', size)

	def getSize(self):
		return struct.unpack('>I', self.size)[0]

	def string(self):
		out = self.blockheader + self.blocktype + self.spacing1 + self.size + self.spacing2 + self.spacing3 + self.data
		return out
		
class LIFDirEntry:
	'''
	SIZE	TYPE	DESCRIPTION
	2 bytes	Int16	Entry type (equals 1)
	4 bytes	Int32	Unknown value (equals 0 or 7) The value 0 seems to be used for the root folder.
	N bytes	Char[]	Folder name. (Unicode null-terminated text)
	4 bytes	Spacing	(Always equals 0)
	4 bytes	Int32?	Block size (Always equals 20 so it equals the block header size)
	4 bytes	Int32	The number of sub-entries (files and folders)
	'''

	def __init__(self, rootind, name, entries):
		self.entrytype = struct.pack('>H', 1)		#Entry type (equals 1)
		self.rootind = struct.pack('>I', rootind) 	#Unknown value (equals 0 or 7) The value 0 seems to be used for the root folder.
		self.name = b'\x00' + name.encode('utf-16')[2:] + b'\x00'
		self.spacing1 = struct.pack('>I', 0)		#Spacing (Always equals 0)
		self.size = struct.pack('>I', 20)		#Block size (Always equals 20 so it equals the block header size)
		self.entries = struct.pack('>I',entries)	#The number of sub-entries (files and folders)

	def string(self):
		out = self.entrytype + self.rootind + self.name + self.spacing1 + self.size + self.entries
		return out


class LIFFileEntry:
	'''
	SIZE	TYPE	DESCRIPTION
	2 bytes	Int16	Entry type (equals 2)
	4 bytes	Int32	Spacing/unknown value (0 or 7)
	N bytes	Char[]	File name. (Unicode null-terminated text)
	4 bytes	Spacing	(Always equals 0)
	4 bytes	Int32	File size (it is actually the block size because it includes the block header size (20))
	8 bytes	Long	Created, modified or accessed date
	8 bytes	Long	Created, modified or accessed date
	8 bytes	Long	Created, modified or accessed date
	'''

	def __init__(self, name, size):
		self.entrytype = struct.pack('>H', 2)		#Entry type (equals 2)
		self.unknwown = struct.pack('>I', 7)		#Spacing/unknown value (0 or 7).
		self.name = b'\x00' + name.encode('utf-16')[2:] + b'\x00'
		self.spacing1 = struct.pack('>I', 0)		#Spacing (Always equals 0)
		self.size = struct.pack('>I', size)		#File size (it is actually the block size because it includes the block header size (20))
		self.created = struct.pack('>Q', 18369614221190020847)	#Created, modified or accessed date
		self.modified = struct.pack('>Q', 18369614221190020847)	#Created, modified or accessed date. Set to 0xFEEDFACECAFEBEEF for testing
		self.accessed = b'\x01\xce\xec\xee\x85\x3b\x50\xdb' 	#Created, modified or accessed date

	def string(self):
		out = self.entrytype + self.unknwown + self.name + self.spacing1 + self.size +self.created + self.modified + self.accessed
		return out


def createLif(walk_dir):
	outfile = os.path.basename(os.path.normpath(walk_dir))
	number_of_files = 0
	print('LIF Creator 1.1')
	print('Choosen directory: {0}'.format(os.path.normpath(walk_dir)))
	
	#Create the first non-existant file to write to.
	if os.path.exists(outfile + '.lif'):
		i = 1
		while(os.path.exists(outfile + "_" + str(i) + '.lif')):
			i += 1
		outfile = outfile + "_" + str(i)
	
	start_time = time.time()
	
	fi_content_str = b''
	fo_dict = {}
	fh_dict = {}
	for root, subdirs, files in os.walk(walk_dir, topdown=False):
		#ignore hidden files and folders (starting with a dot .)
		files = [f for f in files if not f[0] == '.']
		subdirs[:] = [d for d in subdirs if not d[0] == '.']
		
		files_content_str = b''
		files_fh_str = b''
		for filename in files:
			file_path = os.path.join(root, filename)
			
			sys.stdout.write('\tPROCESSING: {0}          \r'.format(filename))
			sys.stdout.flush()
			#print('Processing: {0}'.format(file_path))
			
			with open(file_path, 'rb') as f:
				current_data = f.read()
				currenFileBlock = LIFBlock(blocktype=4, data=current_data) #Content of single file: Block Type 4
				currenFileEntry = LIFFileEntry(name=filename, size=currenFileBlock.getSize())
				fi_content_str = currenFileBlock.string()
				fh_content_str = currenFileEntry.string()
				
			files_content_str = files_content_str + fi_content_str #Content of all files in current folder
			files_fh_str = files_fh_str + fh_content_str
		
		subfolders_content_str = b''
		subfolders_fh_str = b''
		for subdir in subdirs:
			subfolders_content_str = subfolders_content_str + fo_dict[os.path.join(root, subdir)]
			subfolders_fh_str = subfolders_fh_str + fh_dict[os.path.join(root, subdir)]
			fo_dict.pop(os.path.join(root, subdir), None) #Drop item from fo dict, its no longer needed
			fh_dict.pop(os.path.join(root, subdir), None) #Drop item from fh dict, its no longer needed
			
		currenBlock = LIFBlock(blocktype=3, data=files_content_str + subfolders_content_str) #Block Type 3
		number_entries = len(files) + len(subdirs)
		currenDirEntry = LIFDirEntry(rootind=7, name=os.path.basename(root) , entries=number_entries)
		fo_dict[root] = currenBlock.string()
		fh_dict[root] = currenDirEntry.string() + files_fh_str + subfolders_fh_str
		
		number_of_files = number_of_files + len(files)
	
	'''Root directory block (Block Type 3)'''
	#rootDirBlock = LIFBlock(blocktype=3, data=fo_dict[root])
	rootDirBlock= fo_dict[root]
	
	'''File Content Block (Block Type 2)'''
	fileContentBlock = LIFBlock(blocktype=2, data='')
	
	'''File hierarchy (Block Type 5)'''
	fhBlock = LIFBlock(blocktype=5, data=fh_dict[root])
	
	'''Root Block (Block Type 1)'''
	rootBlock = LIFBlock(blocktype=1, data=fileContentBlock.string() + rootDirBlock + fhBlock.string())
	
	'''Header'''
	headerBlock = LIFHeader()
	headerBlock.setSize(len(rootBlock.string()) + 18)
	
	print('\n\tCOMPLETED: {0} files processed. Will now write {1}.lif.'.format(str(number_of_files), outfile))
	lif_file = open((outfile + '.lif'), "wb")
	lif_file.write(headerBlock.string())
	lif_file.write(rootBlock.string())
	lif_file.close()
	print("--- %s seconds ---" % (time.time() - start_time))

if(len(sys.argv) > 1):
	for i in range(1, len(sys.argv)):
		createLif(sys.argv[i])
else:
	print("LIF Creator 1.1\n\nThis program will create LIF archives from an adjacent folder.\n\nCOPYRIGHT:\n\t(C) 2020 sttng\n\nLICENSE:\n\tGNU GPLv3\n\tYou accept full responsibility for how you use this program.\n\nUSEAGE:\n\t" + runCommand + " <FILE_PATHS>")
