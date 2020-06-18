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
		self.magic = 'LIFF'						#Magic Word (ASCI = 'LIFF')
		self.spacing1 = struct.pack('>I', 0)	#Spacing (Always equals 0)
		self.size = struct.pack('>I',3405691582)#0xCAFEBABE - Just to test and also to verify that header size is set correct later
		self.spacing2 = struct.pack('>H', 1)	#Value "1" (Int16 big endian)
		self.spacing3 = struct.pack('>I', 0)	#Spacing (Always equals 0)

	def setSize(self, size):
		self.size = struct.pack('>I', size)

	def getSize(self):
		return struct.unpack('>I', self.size)[0]
	
	def string(self):
		out = '{0}{1}{2}{3}{4}'.format(self.magic, self.spacing1, self.size, self.spacing2, self.spacing3)
		return out

class LIFBlock:
	
	'''
	LIF Block (20 bytes + data):
	2 bytes	Int16	Block start/header (always 1)
	2 bytes	Int16	Block type (1 to 5)
	4 bytes			Spacing1 (Always equals 0)
	4 bytes	Int32	Block size in bytes (includes header and data)
	4 bytes			Spacing2 (Equals 1 for block types 2,4 and 5)
	4 bytes			Spacing3 (Always equals 0)
	X bytes			The block content/data.
	The block type 1 is the "root block" and its size includes the remainder of the LIF file.
	The block type 2 contains the files content/data. The block content seems hard-coded and it is always 1 (Int16) and 0 (Int32).
	The block type 3 represents a folder. The block content is a hierarchy of type 3 and 4 blocks.
	The block type 4 represents a file. The block data is the file content/data.
	The block type 5 contains the files and folders names and some more information. The block content is a hierarchy of LIF entries.
	Note: The block header's is 20 bytes total. The data size is equal to the specified size - 20 bytes.
	'''
	
	def __init__(self, blocktype, data):
		self.blockheader = struct.pack('>H', 1)			#Block start/header (always 1)
		self.blocktype = struct.pack('>H', blocktype)	#Block type (1 to 5)
		self.spacing1 = struct.pack('>I', 0)			#Spacing (Always equals 0)
														#Block size in bytes (includes header and data) <- calculated later
		if blocktype == 1 or blocktype == 3:
			self.spacing2 = struct.pack('>I', 0)
		else:
			self.spacing2 = struct.pack('>I', 1)		#Spacing (Equals 1 for block types 2,4 and 5)
		self.spacing3 = struct.pack('>I', 0)			#Spacing (Always equals 0)
		if blocktype == 2:
			self.data = (b'\x00\x01\x00\x00\x00\x00')	#The block content seems hard-coded for blocktype 2 and is always 1 (Int16) and 0 (Int32)
		else:
			self.data = data
		
		self.size = struct.pack('>I',len(self.data)+20)	#Block size in bytes (includes header and data)

	def setSize(self, size):
		self.size = struct.pack('>I', size)

	def getSize(self):
		return struct.unpack('>I', self.size)[0]

	def string(self):
		out = '{0}{1}{2}{3}{4}{5}{6}'.format(self.blockheader, self.blocktype, self.spacing1, self.size, self.spacing2, self.spacing3, self.data)
		return out

def walkDir(walk_dir):
	# If your current working directory may change during script execution, it's recommended to
	# immediately convert program arguments to an absolute path. Then the variable root below will
	# be an absolute path as well. Example:
	# walk_dir = os.path.abspath(walk_dir)
	print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))
	fi_content_str = ''
	files_content_str = ''
	folders_content_str =''
	fo_dict = {}
	
	for root, subdirs, files in os.walk(walk_dir, topdown=False):
	
		#ignore hidden files and folders (starting with a dot .)
		files = [f for f in files if not f[0] == '.']
		subdirs[:] = [d for d in subdirs if not d[0] == '.']
	
		print('--\nroot = ' + root)
		
		files_content_str = ''
		for filename in files:
			file_path = os.path.join(root, filename)
			file_size = os.path.getsize(file_path)
			file_header_size = file_size + 20

			print('\t- file %s (full path: %s)' % (filename, file_path))

			with open(file_path, 'rb') as f:
				#FS: = Filesize (fixed to 3 digits) including 20 for header, FN = Filename (fixed to 8 chars), FC = File content | Header Size = 20 
				#FS:041FN:abc.txt FC:the file content..... 
				# 3  3  3    8	  3 = 20
				fi_content_str = 'FS:{0:0=3d}FN:{1:8.8}FC:{2}'.format(file_header_size, filename, f.read()) #Content of single file
				
			files_content_str = files_content_str + fi_content_str #Content of all files in current folder
		
		current_dir = os.path.normpath(root).split(os.sep)[-1] #Get the name of the current dir
		#DS: = Dir Size, DN = Dir Name, DC = Dir Content (either subdirs or files)
		if files_content_str != '': #Found at least one file
			fo_content_str = 'DS:{0:0=3d}DN:{1:8.8}DC:{2}'.format(len(files_content_str) + 20 , current_dir, files_content_str) #Content of files in current folder
			fo_dict[root] = fo_content_str
			print 'FOC: ' + fo_content_str +'\n\n'
		
		else: # Found a folder without files
			fo_content_str = 'DS:{0:0=3d}DN:{1:8.8}DC:{2}'.format(20 , current_dir, '') #Fixed size of 20, no files
			fo_dict[root] = fo_content_str
			print 'FOC (no File): ' + fo_content_str +'\n\n'
		
		fo_content_str = ''
		for subdir in subdirs:
			print('\t- subdirectory ' + os.path.join(root, subdir))
			fo_content_str =  fo_content_str + fo_dict[os.path.join(root, subdir)]
			print('\t- subdirectory ' + fo_content_str )
			#folders_content_str = 'DS:{0:0=3d}DN:{1:8.8}DC:{2}'.format(len(fo_dict[os.path.join(root, subdir)]) + 20 , current_dir, fo_dict[os.path.join(root, subdir)])
			
		#folders_content_str = folders_content_str + fo_content_str
		folders_content_str = 'DS:{0:0=3d}DN:{1:8.8}DC:{2}'.format(len(fo_content_str) + 20 , current_dir, fo_content_str)
		fo_dict[root] = fo_content_str + folders_content_str
		
		print 'FOCS: ' + fo_dict[root] +'\n\n'

	print folders_content_str 


def createa(path):
	rootDir = path
	for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
		print('Found directory: %s' % dirName)
		for fname in fileList:
			print('\t%s' % fname)

def create(path):
	rootDir = path
	test_file = open('_test.lif', "wb")
	lifblocks = [] #Array to hold all blocks (including the LIFF header at [0])
	fileblocks = []
	dict = {}
	tagged = False
	for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
	
		#ignore hidden files and folders (starting with a dot .)
		fileList = [f for f in fileList if not f[0] == '.']
		subdirList[:] = [d for d in subdirList if not d[0] == '.']
		
		for fname in fileList:
			fp = os.path.join(dirName, fname)
			print('\t%s' % fp)
			'''File Block (Block Type 4)'''
			fa = open(fp, "rb")
			file_data = list(fa.read())
			file_data_array = bytearray(file_data)
			fa.close()
			fileblocks.append(LIFBlock(blocktype=4, data=file_data_array))
			tagged = True
		data = ''
		
		for item in fileblocks:
			data = data + item.string()
		lifblocks.append(LIFBlock(blocktype=3, data=data))
		fileblocks = []
		if tagged:
			dict[dirName] = LIFBlock(blocktype=3, data=data)
		print('Found directory: %s' % dirName)
		if subdirList:
			print('Has sub directory: %s' % subdirList)
		else:
			print('Has no sub directory: %s' % subdirList)
			print dict[dirName]

	for item in lifblocks:
		test_file.write(item.string())
		#item.string()
	test_file.close()


def create1(path):
	filename = os.path.basename(os.path.normpath(path))
	test_file = open((filename + '.lif'), "wb")
	fh_file = open((filename + '_fh.lif'), "wb") #the file_hierarchy_file will be appended to the main file later.
	lifblocks = [] #Array to hold all blocks (including the LIFF header at [0])
	i = 0
	
	total_size = 0
	
	'''Header'''
	lifblocks.append(LIFHeader())
	i+=1

	'''Root Block (Block Type 1)'''
	lifblocks.append(LIFBlock(blocktype=1, data=''))
	lifblocks[i].setSize(3405697037) #0xCAFED00D - Just to test and also to verify that file content block size is set correct later
	i+=1

	'''File Content Block (Block Type 2)'''
	lifblocks.append(LIFBlock(blocktype=2, data=''))
	i+=1

	'''Root Directory Block (Block Type 3)'''
	lifblocks.append(LIFBlock(blocktype=3, data=''))
	lifblocks[i].setSize(3735928559) #0xDEADBEEF - Just to test and also to verify that block size is set correct later
	i+=1
	
	#Root directory (Entry type 1) 
	# write to file_hierarchy_file. This will be appended later 
	fh_file.write(b'\x00\x01') #Entry type (equals 1)
	fh_file.write(b'\x00\x00\x00\x00') #Unknown value (equals 0 or 7) The value 0 seems to be used for the root folder
	fh_file.write(b'\x00') #(add 0 terminator)
	#fh_file.write(f.encode('utf-16')[2:]) #File name. (Unicode null-terminated text) !!! Root directory has no name
	fh_file.write(b'\x00') #(add 0 terminator)
	fh_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
	fh_file.write(struct.pack('>I', 20)) #Block size (Always equals 20 so it equals the block header size)
	fh_file.write(struct.pack('>I', len([f for f in os.listdir(path) if not f.startswith('.')]))) #The number of sub-entries (files and folders)

	for dirpath, dirnames, filenames in os.walk(path):
	
		#ignore hidden files and folders (starting with a dot .)
		filenames = [f for f in filenames if not f[0] == '.']
		dirnames[:] = [d for d in dirnames if not d[0] == '.']
		
		number_entries = len(filenames) + len(dirnames)
		#print number_entries

		dirsize = 0
		
		for f in filenames:
			fp = os.path.join(dirpath, f)
			size = os.path.getsize(fp)
			size = size + 20 #Add header size
			
			'''File Block (Block Type 4)'''
			fa = open(fp, "rb")
			file_data = list(fa.read())
			file_data_array = bytearray(file_data)
			fa.close()
			
			lifblocks.append(LIFBlock(blocktype=4, data=file_data_array))
			i+=1
			
			# write to file_hierarchy_file. This will be appended later
			fh_file.write(b'\x00\x02') #Entry type (equals 2)
			fh_file.write(b'\x00\x00\x00\x05') #Spacing/unknown value (0 or 7)
			fh_file.write(b'\x00') #(add 0 terminator)
			fh_file.write(f.encode('utf-16')[2:]) #File name. (Unicode null-terminated text)
			fh_file.write(b'\x00') #(add 0 terminator)
			fh_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
			fh_file.write(struct.pack('>I', size)) #File size (it is actually the block size because it includes the block header size (20))
			fh_file.write(struct.pack('>Q', os.stat(fp)[9])) #Created, modified or accessed date
			fh_file.write(struct.pack('>Q', 18369614221190020847)) #Created, modified or accessed date. Set to 0xFEEDFACECAFEBEEF for testing
			fh_file.write(b'\x01\xce\xec\xee\x85\x3b\x50\xdb') #Created, modified or accessed date
			
			dirsize += size
			total_size += size
		
		dirsize = dirsize + 20 #Add header size
		#lifblocks[current_block_index].setSize(dirsize)
		
		
		print("\t", dirsize, dirpath)
	print("{0} bytes".format(total_size))
	
	
	fh_file.close()
	
	
	'''
	File hierarchy (Block Type 5)
	'''
	fa = open(filename + '_fh.lif', "rb")
	file_data = list(fa.read())
	file_data_array = bytearray(file_data)
	fa.close()
	fh_block = LIFBlock(blocktype=5, data=file_data_array)
	lifblocks.append(fh_block)
	i+=1
	
	#Headersize
	lifblocks[0].setSize(total_size + 20 + fh_block.getSize() + 26 + 18)
	lifblocks[1].setSize(total_size + 20 + fh_block.getSize() + 26)
	lifblocks[3].setSize(total_size + 20)
	
	for item in lifblocks:
		test_file.write(item.string())
		#item.string()
	test_file.close()
	os.remove(filename + '_fh.lif')


def create_old(path):
	i = 0
	blocksize = 0 #Used to calculate and add up the sizes of blocks later
	cur_foldersize = 0 #Used to calculate and add up the sizes per folder block later
	filename = os.path.basename(os.path.normpath(path))
	binary_file = open((filename + '_tmp.lif'), "wb")
	test_file = open((filename + '_test.lif'), "wb")
	fh_file = open((filename + '_fh.lif'), "wb") #the file_hierarchy_file will be appended to the main file later.
	lifblocks = [] #Array to hold all blocks (including the LIFF header at [0])
	
	'''
	Header
	'''
	lifblocks.append(LIFHeader())
	lifblocks[i].setSize(3405691582) #0xCAFEBABE - Just to test and also to verify that header size is set correct later
	i+=1

	'''
	Root Block (Block Type 1)
	'''
	lifblocks.append(LIFBlock(blocktype=1, data=''))
	lifblocks[i].setSize(3669732608) #0xDABBAD00 - Just to test and also to verify that root block size is set correct later
	i+=1

	'''
	File content Block (Block Type 2)
	'''
	lifblocks.append(LIFBlock(blocktype=2, data=''))
	lifblocks[i].setSize(3405697037) #0xCAFED00D - Just to test and also to verify that file content block size is set correct later
	i+=1

	'''
	Root directory block (Block Type 3)
	'''
	root_dir_block = LIFBlock(blocktype=3, data='')
	root_dir_block.setSize(3735928559) #0xDEADBEEF - Just to test and also to verify that block size is set correct later
	lifblocks.append(root_dir_block)
	i+=1
	
	binary_file.write(root_dir_block.string())
	
	# Set the directory you want to start from
	rootDir = path
	for dirName, subdirList, fileList in os.walk(rootDir):
	
		#ignore hidden files and folders (starting with a dot .)
		fileList = [f for f in fileList if not f[0] == '.']
		subdirList[:] = [d for d in subdirList if not d[0] == '.']
	
		print('Found directory: %s' % dirName)
		number_dirs = len(subdirList)
		number_files = len(fileList)
		number_entries = number_dirs + number_files
		
		'''
		Folder Block (Block Type 3)
		'''
		folder_block = LIFBlock(blocktype=3, data='')
		folder_block.setSize(3735929054) #0xDEADC0DE - Just to test and also to verify that folder size is set correct later
		lifblocks.append(folder_block)
		current_block_index = i #save the index to later adjust the size
		i+=1
		
		binary_file.write(folder_block.string())
		
		# write to file_hierarchy_file. This will be appended later 
		fh_file.write(b'\x00\x01') #Entry type (equals 1)
		fh_file.write(b'\x00\x00\x00\x00') #Unknown value (equals 0 or 7) The value 0 seems to be used for the root folder
		fh_file.write(dirName.encode('utf-16')) #File name. (Unicode null-terminated text)
		fh_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
		fh_file.write(struct.pack('>I', 20)) #Block size (Always equals 20 so it equals the block header size)
		fh_file.write(struct.pack('>I', number_entries)) #The number of sub-entries (files and folders)
		
		for fname in fileList:
			fp = os.path.join(dirName, fname)
			file_size = os.path.getsize(fp)

			#created = time.ctime(os.path.getctime(fname))
			#print os.stat(fname)[9]
			
			'''
			File block (Block Type 4)
			'''
			# Read the file to be added to the lif archive
			f = open(fp, "rb")
			file_data = list(f.read())
			file_data_array = bytearray(file_data)
			f.close()
			
			# Create lifblock with data of file just read
			file_block = LIFBlock(blocktype=4, data=file_data_array)
			#fileblock.setSize = file_size + 20
			
			binary_file.write(file_block.string())
			
			lifblocks.append(file_block)
			i+=1
			
			# write to file_hierarchy_file. This will be appended later 	
			fh_file.write(b'\x00\x10') #Entry type (equals 2)
			fh_file.write(b'\x00\x00\x00\x00') #Spacing/unknown value (0 or 7)
			fh_file.write(fname.encode('utf-16')) #File name. (Unicode null-terminated text)
			fh_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
			fh_file.write(struct.pack('>I', file_size + 20)) #File size (it is actually the block size because it includes the block header size (20))
			fh_file.write(struct.pack('>Q', os.stat(fp)[9])) #Created, modified or accessed date
			fh_file.write(struct.pack('>Q', 18369614221190020847)) #Created, modified or accessed date. Set to 0xFEEDFACECAFEBEEF for testing
			fh_file.write(b'\x00\x00\x00\x00\x00\x00\x00\x00') #Created, modified or accessed date
			print('\t%s' % fname)
			blocksize = blocksize + file_size + 20
			cur_foldersize = cur_foldersize + file_size + 20
		
		lifblocks[current_block_index].setSize(cur_foldersize)
		cur_foldersize = 0
	
	binary_file.close()
	fh_file.close()
	fh_file_size = os.path.getsize(filename + '_fh.lif')
	
	#lifblocks[0].setSize(blocksize + 18 + fh_file_size)# Size of file in header, which is all blocks + size of the file_hirarchy_file
	lifblocks[3].setSize(blocksize) # Size of file in 1st block
	lifblocks[2].setSize(lifblocks[3].getSize() + 20)
	lifblocks[1].setSize(lifblocks[2].getSize() + 20)
	lifblocks[0].setSize(lifblocks[1].getSize() + 18 + fh_file_size)
	
	
	for item in lifblocks:
		test_file.write(item.string())
		#item.string()
	test_file.close()
	
	#Concat files into final file
	with open(filename + '.lif','wb') as wfd:
		for f in [filename + '_test.lif', filename + '_fh.lif']:
			with open(f,'rb') as fd:
				shutil.copyfileobj(fd, wfd, 1024*1024*10)
	os.remove(filename + '_tmp.lif')
	#os.remove(filename + '_fh.lif')
	

#Detect if executable or not.
fileName = sys.argv[0].split(os.sep).pop()
if(fileName[-3:] == ".py" or fileName[-4:] == ".pyw"):
	runCommand = "python " + fileName
else:
	runCommand = fileName

if(len(sys.argv) > 1):
	for i in range(1, len(sys.argv)):
		walkDir(sys.argv[i])
else:
	print("LIF Creator 1.0\n\nThis program will create LIF archives from an adjacent folder.\n\nCOPYRIGHT:\n\t(C) 2020 sttng\n\nLICENSE:\n\tGNU GPLv3\n\tYou accept full responsibility for how you use this program.\n\nUSEAGE:\n\t" + runCommand + " <FILE_PATHS>")
