#!/usr/bin/env python
import os
import sys
import time

def create(path):
	# Set the directory you want to start from
	rootDir = '.'
	for dirName, subdirList, fileList in os.walk(rootDir):
		print('Found directory: %s' % dirName)
		number_dirs = len(subdirList)
		number_files = len(fileList)
		number_entries = number_dirs + number_files
		print number_entries
		# Create four bytes from the integer
		four_bytes = number_entries.to_bytes(4, byteorder='big', signed=True)
		binary_file.write(b'\x00\x01') #Entry type (equals 1)
		binary_file.write(b'\x00\x00\x00\x00') #Unknown value (equals 0 or 7) The value 0 seems to be used for the root folder
		binary_file.write(dirName.encode('utf8')) #File name. (Unicode null-terminated text)
		binary_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
		binary_file.write(b'\x00\x00\x00\x00') #Block size (Always equals 20 so it equals the block header size)
		binary_file.write(four_bytes) #The number of sub-entries (files and folders)
		
			for fname in fileList:
				print('\t%s' % fname)
				file_size = os.path.getsize(fname)
				
				print("Last modified: %s" % time.ctime(os.path.getmtime(fname)))
				print("Created: %s" % time.ctime(os.path.getctime(fname)))
				
				binary_file.write(b'\x00\x10') #Entry type (equals 2)
				binary_file.write(b'\x00\x00\x00\x00') #Spacing/unknown value (0 or 7)
				binary_file.write(fname.encode('utf8')) #File name. (Unicode null-terminated text)
				binary_file.write(b'\x00\x00\x00\x00') #Spacing (Always equals 0)
				binary_file.write(file_size + 20) #File size (it is actually the block size because it includes the block header size (20))
				binary_file.write(b'\x00\x00\x00\x00\x00\x00\x00\x00') #Created, modified or accessed date
				binary_file.write(b'\x00\x00\x00\x00\x00\x00\x00\x00') #Created, modified or accessed date
				binary_file.write(b'\x00\x00\x00\x00\x00\x00\x00\x00') #Created, modified or accessed date
				
				
				

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
