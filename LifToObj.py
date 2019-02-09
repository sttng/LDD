#!/usr/bin/env python
 
#
# Version 0.1 - Copyright (c) 2019 by 
#
# Updates:
#
# License: MIT License
#

@staticmethod
	def read_brick(partnumber):

	files_to_convert = []
	files_to_convert = glob.glob(os.path.join(path_to_lif_tmp_dir + '/db/Primitives/LOD0', partnumber + '.g*'))
	
	#various similar extensions like g, .g1, .g2, …, .g8 exist if the brick is composed of multiple parts. The .g file is the 'base_brick'
	for geometry_file in files_to_convert:
		
		if (os.path.splitext(files_to_convert)[1] == ".g"):
			base_brick = BrickReader.load_single_geometry_file(geometry_file)
		else:
			additional_primitive = BrickReader.load_single_geometry_file(geometry_file)
			
		base_brick = BrickReader.merge(base_brick, additional_primitive)

	return base_brick
	
@staticmethod
	def load_single_geometry_file(geometry_file):
	
	try:
			with open(geometry_file, 'rb') as file_reader:
				
				vertices_list = []
				normals_list = []
				indices_list = []
				geometry_file_dict = dict()
				
				partnumber = os.path.splitext(os.path.basename(geometry_file))[0]
				
				fourcc = file_reader.read(4) # should implement check on fourcc == GB10
				vertex_count = struct.unpack("<L", file_reader.read(4))[0]
				indices_count = struct.unpack("<L", file_reader.read(4))[0]
				# options flag:
				# 0x01 == uv_texture_coords_enabled then texture_coords_coubt = 2 * vertex_count
				# 0x10 == unknown
				# 0x20 == unknown
				# 0x02 == then probably, vertices, normals
				# 0x08 == then vertices only ?
				
				options = file_reader.read(4)
				print 'Options: ' + options
				if options == '0x01':
    			# uv_texture_coords_enabled
				elif options == '0x02':
				
					for i in range(0, 3*vertex_count):
						vertex = struct.unpack("f", file_reader.read(4))[0]
						vertices_list.append(vertex)
					
					for i in range(0, 3*vertex_count):
						normal = struct.unpack("f", file_reader.read(4))[0]
						normals_list.append(normal)
					
					for i in range(0, indices_count):
						index = struct.unpack("<L", file_reader.read(4))[0]
						indices_list.append(index)
				
					geometry_file_dict["vertices"] = vertices_list
					geometry_file_dict["normals"] = normals_list
					geometry_file_dict["indices"] = indices_list
					geometry_file_dict["partnumber"] = partnumber
				
				else:
					print 'unknown options: ' + options
				
				return geometry_file_dict
				
								
		except IOError as e:
			print('\tERROR: Failed to read .g file.')
			return False
 
	
	
