#!/usr/bin/env python

"""
    LIF Creator - LEGO Digital Designer LIF creator.

    Copyright (C) 202 sttng

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

class LIFBlock:
	
	'''
	LIF Block
	2 bytes	Int16	Block start/header (always 1)
	2 bytes	Int16	Block type (1 to 5)
	4 bytes		Spacing (Always equals 0)
	4 bytes	Int32	Block size in bytes (includes header and data)
	4 bytes		Spacing (Equals 1 for block types 2,4 and 5)
	4 bytes		Spacing (Always equals 0)
	X bytes		The block content/data.
	The block type 1 is the "root block" and its size includes the remainder of the LIF file.
	The block type 2 contains the files content/data. The block content seems hard-coded and it is always 1 (Int16) and 0 (Int32).
	The block type 3 represents a folder. The block content is a hierarchy of type 3 and 4 blocks.
	The block type 4 represents a file. The block data is the file content/data.
	The block type 5 contains the files and folders names and some more information. The block content is a hierarchy of LIF entries.
	Note: The block header's is 20 bytes total. The data size is equal to the specified size - 20 bytes.
	'''
	
	def __init__(self, typ, size, data):
		self.header = 1
		self.typ = typ
		self.spacing1 = 0
		self.size = len(data)
		if typ == 2 or typ == 4 or typ == 5:
			self.spacing2 = 1
		else:
			self.spacing2 = 0
		self.spacing3 = 0
		if typ == 2:
			self.data = (struct.pack('>H', 1)) + (struct.pack('>I', 0))
		else:
			self.data = data

	def string(self):
		out = '{0} {1} {2}'.format(self.header, self.typ, self.spacing1, self.size, self.spacing2, self.spacing3, self.data) 
		return out


def create(path):
	i = 0
	filename = os.path.basename(os.path.normpath(path))
	binary_file = open((filename + '.lif'), "wb")
	
	lifblocks = []
	'''
	LIF Header (18 bytes total):	
	4 bytes	Char[4]	Header (ASCI = 'LIFF')
	4 bytes		Spacing (Always equals 0)
	4 bytes	Int32	Total file size (Int32 big endian)
	2 bytes	Int16	Value "1" (Int16 big endian)
	4 bytes		Spacing (Always equals 0)
	'''		
	binary_file.write(b"LIFF")
	binary_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
	binary_file.write(b'\xff\xff\xff\xff') #Total file size (Int32 big endian)
	binary_file.write(struct.pack('>H', 1)) #Value "1" (Int16 big endian)
	binary_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
	
	'''
	Root Block (Block Type 1)
	2 bytes	Int16	Block start/header (always 1)
	2 bytes	Int16	Block type (1 to 5)
	4 bytes		Spacing (Always equals 0)
	4 bytes	Int32	Block size in bytes (includes header and data)
	4 bytes		Spacing (Equals 1 for block types 2,4 and 5)
	4 bytes		Spacing (Always equals 0)
	X bytes		The block content/data.
	'''

	lifblocks.append(LIFBlock(typ=1, size=123, data=''))
	i+=1
	binary_file.write(struct.pack('>H', 1)) #Block start/header (always 1)
	binary_file.write(struct.pack('>H', 1)) #Block type (1 to 5). 1 for Root Block
	binary_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
	binary_file.write(b'\xff\xff\xff\xff') #Block size in bytes (includes header and data)
	binary_file.write(b'\x00\x00\x00\x00') #Spacing (Equals 1 for block types 2,4 and 5)
	binary_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
	
	'''
	File content Block (Block Type 2)
	The block content seems hard-coded and it is always 1 (Int16) and 0 (Int32).
	'''
	lifblocks.append(LIFBlock(typ=2, size=123, data=''))
	i+=1
	binary_file.write(struct.pack('>H', 1)) #Block start/header (always 1)
	binary_file.write(struct.pack('>H', 2)) #Block type (1 to 5). 2 for File content Block
	binary_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
	binary_file.write(b'\xff\xff\xff\xff') #Block size in bytes (includes header and data)
	binary_file.write(struct.pack('>I', 1)) #Spacing (Equals 1 for block types 2,4 and 5)
	binary_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
	binary_file.write(struct.pack('>H', 1)) #The block content seems hard-coded and it is always 1 (Int16) and 0 (Int32).
	binary_file.write(struct.pack('>I', 0))
	
	'''
	Root directory block (Block Type 3)
	'''
	lifblocks.append(LIFBlock(typ=3, size=123, data=''))
	i+=1
	binary_file.write(struct.pack('>H', 1)) #Block start/header (always 1)
	binary_file.write(struct.pack('>H', 3)) #Block type (1 to 5). 3 for Root directory block 
	binary_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
	binary_file.write(b'\xff\xff\xff\xff') #Block size in bytes (includes header and data)
	binary_file.write(struct.pack('>I', 0)) #Spacing (Equals 1 for block types 2,4 and 5)
	binary_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
	
	# Set the directory you want to start from
	rootDir = path
	for dirName, subdirList, fileList in os.walk(rootDir):
		print('Found directory: %s' % dirName)
		number_dirs = len(subdirList)
		number_files = len(fileList)
		number_entries = number_dirs + number_files
		print number_entries
		
		'''
		Folder Block (Block Type 3)
		'''
		binary_file.write(struct.pack('>H', 1)) #Block start/header (always 1)
		binary_file.write(struct.pack('>H', 3)) #Block type (1 to 5). 3 for folder Block
		binary_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
		binary_file.write(b'\xff\xff\xff\xff') #Block size in bytes (includes header and data)
		binary_file.write(struct.pack('>I', 0)) #Spacing (Equals 1 for block types 2,4 and 5)
		binary_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
		
				
		# This one need to be written later in fact (concaneted to the file
		binary_file.write(b'\x00\x01') #Entry type (equals 1)
		binary_file.write(b'\x00\x00\x00\x00') #Unknown value (equals 0 or 7) The value 0 seems to be used for the root folder
		binary_file.write(dirName.encode('utf-16')) #File name. (Unicode null-terminated text)
		binary_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
		binary_file.write(b'\x00\x00\x00\x00') #Block size (Always equals 20 so it equals the block header size)
		binary_file.write(struct.pack('>I', number_entries)) #The number of sub-entries (files and folders)
		
		for fname in fileList:
			print('\t%s' % fname)
			file_size = os.path.getsize(fname)
				
			print("Last modified: %s" % time.ctime(os.path.getmtime(fname)))
			#created = time.ctime(os.path.getctime(fname))
			#print os.stat(fname)[9]
			
			
			'''
			File block (Block Type 4)
			'''
			binary_file.write(struct.pack('>H', 1)) #Block start/header (always 1)
			binary_file.write(struct.pack('>H', 4)) #Block type (1 to 5). 4 for File Block
			binary_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
			binary_file.write(b'\xff\xff\xff\xff') #Block size in bytes (includes header and data)
			binary_file.write(struct.pack('>I', 1)) #Spacing (Equals 1 for block types 2,4 and 5)
			binary_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
			
			f = open(fname, "rb")
			file_data = list(f.read())
			binary_file.write(str(file_data))
			f.close()
						
			# This one need to be written later in fact (concaneted to the file)	
			binary_file.write(b'\x00\x10') #Entry type (equals 2)
			binary_file.write(b'\x00\x00\x00\x00') #Spacing/unknown value (0 or 7)
			binary_file.write(fname.encode('utf-16')) #File name. (Unicode null-terminated text)
			binary_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
			binary_file.write(struct.pack('>I', file_size + 20)) #File size (it is actually the block size because it includes the block header size (20))
			binary_file.write(struct.pack('>Q', os.stat(fname)[9])) #Created, modified or accessed date
			binary_file.write(b'\x00\x00\x00\x00\x00\x00\x00\x00') #Created, modified or accessed date
			binary_file.write(b'\x00\x00\x00\x00\x00\x00\x00\x00') #Created, modified or accessed date
			print('\t%s' % fname)
	
	
	
	
	

	binary_file.close()

def extract(path):
    
    def uint32(offset):
        if(bytesAre == "str"):
            return (ord(fileData[offset]) * 16777216) + (ord(fileData[offset+1]) * 65536) + (ord(fileData[offset+2]) * 256) + ord(fileData[offset+3])
        else:
            return (fileData[offset] * 16777216) + (fileData[offset+1] * 65536) + (fileData[offset+2] * 256) + fileData[offset+3]
    
    def uint16(offset):
        if(bytesAre == "str"):
            return (ord(fileData[offset]) * 256) + ord(fileData[offset+1])
        else:
            return (fileData[offset] * 256) + fileData[offset+1]
    
    def recurse(prefix, offset):
        if(prefix == ""):
            offset += 36
        else:
            folderList.extend([prefix])
            offset += 4
            
        for i in range(uint32(offset)):
            offset += 4
            entryType = uint16(offset)#1 = directory, 2 = file
            offset += 6
            #Build the name.
            entryName = os.sep
            #Check both integer and byte for different versions of Python.
            while(fileData[offset+1] != 0 and fileData[offset+1] != b"\x00"):
                if(bytesAre == "str"):
                    entryName += fileData[offset+1]
                else:
                    entryName += chr(fileData[offset+1])
                offset += 2
            offset += 6
            
            if(entryType == 1):
                #Recurse through the director, and update the offset.
                packedFilesOffset[0] += 20
                offset = recurse(prefix + entryName, offset)
            elif(entryType == 2):
                #File offset.
                packedFilesOffset[0] += 20
                fileOffset = packedFilesOffset[0]
                #File size.
                fileSize = uint32(offset) - 20
                offset += 24
                packedFilesOffset[0] += fileSize
                fileList.extend([[prefix + entryName, fileOffset, fileSize]])
        #Return the offset at the end of this run to update parent runnings.
        return offset
    
    print("PROCESSING: " + path)
    #Open the file if valid.
    try:
        with open(path, "rb") as f:
            fileData = f.read()
    except IOError as e:
        print("\tERROR: Failed to read file.")
        return False
    
    if(len(fileData) < 4 or fileData[0:4] != b"LIFF"):
        print("\tERROR: Not a LIF file.")
        return False
    
    print("\tEXTRACTING: Please wait.")
    
    #Recurse through, creating a list of all the files.
    packedFilesOffset = [84]#Array for non-global function-modifiable variable.
    folderList = []
    fileList = []
    #Check if this version of Python treats bytes as int or str
    bytesAre = type(b'a'[0]).__name__    
    #Recuse through the archive.
    recurse("", (uint32(72)+64))
    
    #Create output path from input path.
    if(path[-4:].lower() == ".lif"):
        outFolder = path[:-4]
    else:
        outFolder = path
    #Create the first non-existant folder to extract to.
    if os.path.exists(outFolder):
        i = 1
        while(os.path.exists(outFolder + "_" + str(i))):
            i += 1            
        outFolder = outFolder + "_" + str(i)
    
    #Make the output folder.
    os.makedirs(outFolder)
    
    #Create all the folders we need to extract to.
    for a in folderList:
        if(a[0] == ""):
            continue
        if not os.path.exists(outFolder + a):
            os.makedirs(outFolder + a)
    
    #Loop through the list of files, saving them.
    for a in fileList:
        f = open((outFolder + a[0]), "wb")
        f.write(fileData[a[1]:a[1]+a[2]])
        f.close()
    
    print("\tCOMPLETE: " + str(len(fileList)) + " files in " + str(len(folderList)) + " folders extracted.")
    return True

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
    print("LIF Creator 1.0\n\nThis program will create LIF archives from an adjacent folder.\n\nCOPYRIGHT:\n\t(C) 2020 sttng\n\nLICENSE:\n\tGNU GPLv3\n\tYou accept full responsibility for how you use this program.\n\nUSEAGE:\n\t" + runCommand + " <FILE_PATHS>")
