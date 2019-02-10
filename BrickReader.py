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
	geometry_file_dict_list = []
	
	
	#various similar extensions like g, .g1, .g2, …, .g8 exist if the brick is composed of multiple parts. The .g file is the 'base_brick'
	for geometry_file in files_to_convert:
		
		if (os.path.splitext(files_to_convert)[1] == ".g"):
			base_brick = BrickReader.load_single_geometry_file(geometry_file)
			geometry_file_dict_list.append(base_brick)
		else:
			additional_primitive = BrickReader.load_single_geometry_file(geometry_file)
			geometry_file_dict_list.append(additional_primitive)
			
		# base_brick = BrickReader.merge(base_brick, additional_primitive)
		

	return base_brick
	
@staticmethod
	def load_single_geometry_file(geometry_file):

	try:
		with open(geometry_file, 'rb') as file_reader:
				
			vertices_list = []
			normals_list = []
			indices_list = []
			tex_coords_list = []
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
			
			# uv_texture_coords_enabled
			if options == '0x01':
					
				for i in range(0, 3 * vertex_count):
					vertex = struct.unpack("f", file_reader.read(4))[0]
					vertices_list.append(vertex)
					
				for i in range(0, 3 * vertex_count):
					normal = struct.unpack("f", file_reader.read(4))[0]
					normals_list.append(normal)
						
				for i in range(0, 2 * vertex_count):
					tex_coord = struct.unpack("f", file_reader.read(4))[0]
					tex_coords_list.append(tex_coord)
					
				for i in range(0, indices_count):
					index = struct.unpack("<L", file_reader.read(4))[0]
					indices_list.append(index)
						
				geometry_file_dict["vertices"] = vertices_list
				geometry_file_dict["vertex_count"] = vertex_count
				geometry_file_dict["normals"] = normals_list
				geometry_file_dict["tex_coords"] = tex_coords_list
				geometry_file_dict["uv_texture_coords_enabled"] = true
				geometry_file_dict["indices"] = indices_list
				geometry_file_dict["partnumber"] = partnumber						
			# no uv_texture_coords
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
				geometry_file_dict["vertex_count"] = vertex_count
				geometry_file_dict["normals"] = normals_list
				geometry_file_dict["uv_texture_coords_enabled"] = false
				geometry_file_dict["indices"] = indices_list
				geometry_file_dict["partnumber"] = partnumber
				
			else:
				print 'Unknown Options: ' + options
				
			return geometry_file_dict
								
		except IOError as e:
			print('\tERROR: Failed to read .g file.')
			return False


@staticmethod
	def export_to_obj(geometry_file_dict_list):
	
	fragment = 0
	offset = 1
	uv_offset = 1
	partnumber = geometry_file_dict_list[0]["partnumber"]
	
	with open(partnumber + '.obj', 'w') as file_writer:
		file_writer.write('o brick_' + partnumber + '\n')
	
		for geometry_file_dict in geometry_file_dict_list:
		
			file_writer.write('g ' + fragment + '\n')
		
			for i in range(0, len(geometry_file_dict["vertices"]), 3):
				file_writer.write('v ' + str(geometry_file_dict["vertices"][i]) + ' ' + str(geometry_file_dict["vertices"][i + 1]) + ' ' + str(geometry_file_dict["vertices"][i + 2]) + ' ' + '\n\n')
	
			for i in range(0, len(geometry_file_dict["normals"]), 3):
				file_writer.write('vn ' + str(geometry_file_dict["normals"][i]) + ' ' + str(geometry_file_dict["normals"][i + 1]) + ' ' + str(geometry_file_dict["normals"][i + 2]) + ' ' + '\n\n')
	
				if (geometry_file_dict["uv_texture_coords_enabled"] == true):
					for i in range(0, len(geometry_file_dict["tex_coords"]), 2):
						file_writer.write('vt ' + str(geometry_file_dict["tex_coords"][i]) + ' ' + str(geometry_file_dict["tex_coords"][i + 1]) + ' ' + '\n\n')
			
					for i in range(0, len(geometry_file_dict["indices"]), 3):
						index0 = geometry_file_dict["indices"][i + 0] + offset
						index1 = geometry_file_dict["indices"][i + 1] + offset
						index2 = geometry_file_dict["indices"][i + 2] + offset
						index3 = geometry_file_dict["indices"][i + 0] + uv_offset
						index4 = geometry_file_dict["indices"][i + 1] + uv_offset
						index5 = geometry_file_dict["indices"][i + 2] + uv_offset
				
						file_writer.write('f ' + str(index0) + '/' + str(index3) + '/' + str(index0) + ' ' + str(index1) + "/" + str(index4) + '/' + str(index1) + ' ' + str(index2) + "/" + str(index5) + '/' + str(index2) + '\n')
	
				elif:
	
					for i in range(0, len(geometry_file_dict["indices"]), 3):
						index1 = geometry_file_dict["indices"][i + 0] + offset
						index2 = geometry_file_dict["indices"][i + 1] + offset
						index3 = geometry_file_dict["indices"][i + 2] + offset
				
						file_writer.write('f ' + str(index1) + '//' + str(index1) + ' ' + str(index2) + '//' + str(index2) + " " + str(index3) + '//' + str(index3) + '\n')
	
	fragment ++
	offset += geometry_file_dict["vertex_count"]
	
	if (geometry_file_dict["uv_texture_coords_enabled"] == true):
			uv_offset += geometry_file_dict["vertex_count"]
		
				
				file_writer.close()
				
		return True
