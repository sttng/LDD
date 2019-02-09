#!/usr/bin/env python
 
#
# Version 0.1 - Copyright (c) 2019 by 
#
# Updates:
#
# License: MIT License
#

@staticmethod
	def read_brick(part_no):

	files_to_convert = []
	files_to_convert = glob.glob(os.path.join(path_to_lif_tmp_dir + '/db/Primitives/LOD0', part_no + '.g*'))
	
	#various similar extensions like g, .g1, .g2, …, .g8 exist if the brick is composed of multiple parts. The .g file is the 'base_brick'
	for geometry_file in files_to_convert:
	
	filename, file_extension = os.path.splitext(files_to_convert)
	
	if ('.g' in file_extension):
		base_brick = BrickReader.load_single_geometry_file(geometry_file)
			
	else:
		additional_primitive = BrickReader.load_single_geometry_file(geometry_file)
			
	base_brick = BrickReader.merge(base_brick, additional_primitive)

	return base_brick
	
@staticmethod
	def load_single_geometry_file(geometry_file):
	
	
