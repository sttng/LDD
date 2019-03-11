#!/usr/bin/env python

#
# Version 0.1 - Copyright (c) 2019 by 
#
# Info:
# This script will read in a.obj file, construct geometry from it
# and write out a .rib entity file of it. RIB Entity Files are incomplete 
# as they do not contain enough information to render them. RIB Entity 
# Files need to be integrated or added to into "legal," or complete, RIB Files.
#
# Updates:
#
# License: MIT License
#
#

import getpass
import time, random
import sys
import argparse
import collections
import MaterialsTexts

obj_file = sys.argv[1]


def export_obj_to_rib(obj_file, material_id_list):
	if (material_id_list):
		bxdf_mat = MaterialsTexts.material_ids_to_ri(material_id_list)
	
	material_string = '_'.join(material_id_list)
	
		
	Round = 6
	# open the file
	ip = open(obj_file,'r')
	#grab the data as lines
	data = ip.readlines()
	verts = []
	norm = []
	text = []
	face = []
	face_d = {}
	group = 'no_group'
	name = obj_file.split(".")
	name = name[0]
	name = name + '_' + material_string
	# for each line check for one of our tokens
	for line in data:
		# we assume that our Tokens are always the first element of the line (which IIRC the rispec specifies)
		# so we split each line and look at the first element
		tokens=line.split()	
		# make sure we have a token to check against
		if(len(tokens) >0 ) :
			if(tokens[0] == 'g'):
				#print "found group"
				group = tokens[1]
				# Reset face list in case new group is found, so data of the 'old' face group isn't spilled to the 'new'  group.
				face = []
			elif(tokens[0] == 'v'):
				#print "found vert"
				# create a tuple of the vertex point values
				#*****************************************************************
				# NOTE RENDERMAN is left handed coordinate system, obj is right handed -> z-axis inverted
				#
				vert = [round(float(tokens[1]), Round),round(float(tokens[2]), Round), (-1) * round(float(tokens[3]), Round)]
				# then add it to our list
				verts += [vert]
			elif(tokens[0] == 'vn'):
				#print "found normal"
				# create a tuple of the normal values
				#*****************************************************************
				# NOTE RENDERMAN is left handed coordinate system, obj is right handed -> z-axis inverted
				#
				normal = [round(float(tokens[1]), Round),round(float(tokens[2]), Round), (-1) * round(float(tokens[3]), Round)]
				# then add it to our list
				norm += [normal]
			elif(tokens[0] == 'vt'):
				#print "found texture"
				# create a tuple of the texture values
				#*****************************************************************
				# NOTE RENDERMAN Maps Textures in the T from top to bottom so we
				# calculate 1.0 - t here so the image will map properly
				#
				tx = [round(float(tokens[1]),Round),1-round(float(tokens[2]),Round)]
				#
				#*****************************************************************
				# then add it to our list
				text += [tx]
			# now we have a face value
			elif(tokens[0] == 'f'):
				# add the face to the list and we will process it later (see below)
				face += [line]
				face_d[group] = face
			
	# close the file
	ip.close()

	# now we've grabbed all the data we can process each of the faces and write out the rib
	# Assume faces are group specific
	nested_dict = lambda: collections.defaultdict(nested_dict)
	obj_group = nested_dict()	
	
	for group in face_d.keys():
		face = face_d[group]
		i = 0
		for f in face :
			# create some empty data structures to be filled as we go
			vertices = []
			normals = []
			points = [] 
			tx = []
			fd = f.split() 
			# the face is in the structure shown below Vert / TX / Norm we are gaurenteed to have a
			# Vert but the others may not be there
			#1/1/1 3/2/2 4/3/3 2/4/4 
			
			for perface in fd[1:] :
				index=perface.split("/")
				# get the point array index
				pind=int(index[0])-1
				points.append(round(float(verts[pind][0]),Round))
				points.append(round(float(verts[pind][1]),Round))
				points.append(round(float(verts[pind][2]),Round))
				# check for textures and add if there
				if(index[1] != "") :
					tind=int(index[1])-1
					tx.append(round(float(text[tind][0]),Round))
					tx.append(round(float(text[tind][1]),Round))
				# check for normals and check they are there
				if(index[2] != "") :
					nind=int(index[2])-1
					normals.append(round(float(norm[nind][0]),Round))
					normals.append(round(float(norm[nind][1]),Round))
					normals.append(round(float(norm[nind][2]),Round))
					normals_str = ' '.join(map(str, normals))
					
			points_str = ' '.join(map(str, points))
			obj_group[group][i]["P"] = points_str
			# now see if we have any texture co-ordinates and add them to the dictionary if we do
			if index[1] != "" :
				tx_str = ' '.join(map(str, tx))
				obj_group[group][i]["T"] = tx_str
			else:
				obj_group[group][i]["T"] = '' #just to ensure there is no dict error later
			# check for normals and add them to the dictionary as well
			if index[2] != "" :
				obj_group[group][i]["N"] = normals_str
			else:
				obj_group[group][i]["N"] = '' #just to ensure no dict error later
			i += 1
				
	# Now the dict should have everything
	
	op = open(name + '.rib', 'w')
	
	op.write('##RenderMan RIB-Structure 1.1 Entity\n')
	# Later this should cover obj. files with no groups also. Currently however the LXF
	# (LIF) to OBJ exporter writes groups in any case, so we asume we have.
	for group in obj_group.keys():
		op.write('AttributeBegin #begin Brick ' + name + '_' + material_string + '.' + group + '\n')
		op.write('Attribute "identifier" "uniform string name" ["Brick ' + name + '_' + material_string + '.' + group + '"]\n')
		op.write(bxdf_mat[int(group)])
		uv_num = 1
		for f in obj_group[group].keys():
			op.write('\tPolygon\n')
			op.write('\t\t"P" [ ' + str(obj_group[group][f]["P"]) + ' ]\n')
			# check for textures
			if(str(obj_group[group][f]["T"]) != ''):
				op.write('\t\t"facevarying float [2] uv' + str(uv_num) + '" [ ' + str(obj_group[group][f]["T"]) + ' ]\n')
				uv_num += 1
			# check for normals
			if(str(obj_group[group][f]["N"]) != ''):
				op.write('\t\t"N" [ ' + str(obj_group[group][f]["N"]) + ' ]\n')

		op.write('AttributeEnd #end Brick ' + name + '.' + group + '\n\n')

		
#export_obj_to_rib(obj_file)
