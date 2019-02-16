#!/usr/bin/env python

import os
import sys
import re
import unicodedata
import operator


from xml.dom.minidom import parseString
from operator import attrgetter


def parsing(lxfml_filename):
	"""
	Takes in the lxfml file generated by the user and parses it to identify
	all of the bricks and positions created in the LDD program
	"""
	lines = []
	if lxfml_filename != "" and os.path.isfile(lxfml_filename):
		lxfml_file = open(lxfml_filename)
		lines = lxfml_file.read()
		lxfml_file.close()
	else:
		print "ERROR: no input lxfml file has been specified"
		return

	bricks = []
	trans_xyz =[]
	
	dom = parseString(lines)
	elements = dom.getElementsByTagName('Brick')
	
	ribfile = os.path.splitext(os.path.basename(lxfml_filename))[0]
	with open(ribfile + '.rib', 'w') as file_writer:
	
		for element in elements:
			element = element.toxml()
			
			# designID
			regexp = re.search('designID="...."', element)
			
			if regexp:
				regexp = regexp.group(0)
				designID = regexp.replace('designID=','').replace('"','')
				print designID
				
			# Transformation
			regexp = re.search('transformation=".*"', element)
			if regexp:
				regexp = regexp.group(0)
				transformation = regexp.replace('transformation=','').replace('"','')
				
				transformation_array = transformation.split(',')
				#print transformation_array
				
				trans_xyz = (transformation_array[9], transformation_array[10], transformation_array[11])
				
				print trans_xyz
				orientation = []
				for i in range(9):
					orientation.append(int(round(float(transformation_array[i]), 1)))
				
				file_writer.write('\tTransformBegin\n')
				file_writer.write('\t\tTranslate ' + trans_xyz[0] + ' ' + trans_xyz[1] + ' ' + trans_xyz[2] + '\n')
				file_writer.write('\t\tScale 1 1 1\n')
				file_writer.write('\t\tReadArchive \"'+ designID + '.rib\"\n')
				file_writer.write('\tTransformEnd\n')
				
			# Add the brick to the list
			#bricks.append(Brick(x, y, z, orientation, designID))
		
		#return bricks
	
	
	
	
		
			
	file_writer.close()
	
def main():
	lxfml_filename = "IMAGE100.LXFML"

	bricks = parsing(lxfml_filename)
	
	
if __name__ == "__main__":
	main()