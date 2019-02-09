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

		