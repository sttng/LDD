#!/usr/bin/env python

import getpass
import time, random
import sys
import argparse

obj_file = sys.argv[1]


def export_obj_to_rib(File) :
	Round = 6
	print "opening : "+File
	# open the file
	ip = open(File,'r')
	#grab the data as lines
	data=ip.readlines()
	verts=[]
	norm=[]
	text=[]
	face=[]
	face_d= {}
	group = 'no_group'
	# for each line check for one of our tokens
	for line in data :
		# we assume that our Tokens are always the first element of the line (which IIRC the rispec specifies)
		# so we split each line and look at the first element
		tokens=line.split()	
		# make sure we have a token to check against
		if(len(tokens) >0 ) :
			if(tokens[0] == 'g'):
				#print "found group"
				group = tokens[1]
			elif(tokens[0] == 'v'):
				#print "found vert"
				# create a tuple of the vertex point values
				vert=[round(float(tokens[1]),Round),round(float(tokens[2]),Round),round(float(tokens[3]),Round)]
				# then add it to our list
				verts+=[vert]
			elif(tokens[0] =="vn") :
				#print "found normal"
				# create a tuple of the normal values
				normal=[round(float(tokens[1]),Round),round(float(tokens[2]),Round),round(float(tokens[3]),Round)]
				# then add it to our list
				norm+=[normal]
			elif(tokens[0] =="vt") :
				#print "found texture"
				# create a tuple of the texture values
				#*****************************************************************
				# NOTE RENDERMAN Maps Textures in the T from top to bottom so we
				# calculate 1.0 - t here so the image will map properly
				#
				tx=[round(float(tokens[1]),Round),1-round(float(tokens[2]),Round)]
				#
				#*****************************************************************
				# then add it to our list
				text+=[tx]
			# now we have a face value
			elif(tokens[0] =="f") :
				# add the face to the list and we will process it later (see below)
				face+=[line]
				face_d[group] = face
			
	# close the file
	ip.close()

	# now we've grabbed all the data we can process each of the faces and write out the rib
	# Assume faces are group specific
	obj_group = {}{}
	for group in face_d.keys():
		face = face_d[group]
	
		for f in face :
			# create some empty data structures to be filled as we go
			vertices=[]
			normals=[]
			points=[] 
			tx=[]
			fd=f.split() 
			# the face is in the structure shown below Vert / TX / Norm we are gaurenteed to have a
			# Vert but the others may not be there
			#1/1/1 3/2/2 4/3/3 2/4/4 
			i = 0
			for perface in fd[1:] :
				index=perface.split("/")
				# get the point array index
				pind=int(index[0])-1
				points.append(round(float(verts[pind][0]),Round))
				points.append(round(float(verts[pind][1]),Round))
				points.append(round(float(verts[pind][2]),Round))
				points_str = ' '.join(map(str, points))
				obj_group[group][i]["P"] = points_str
				# check for textures and add if there
				if(index[1] !="") :
					tind=int(index[1])-1
					tx.append(round(float(text[tind][0]),Round))
					tx.append(round(float(text[tind][1]),Round))
					tx_str = ' '.join(map(str, tx))
					obj_group[group][i]["T"] = tx_str
				else:
					obj_group[group][i]["T"] = '' #just to ensure
				# check for normals and check they are there
				if(index[2] !="") :
					nind=int(index[2])-1
					normals.append(round(float(norm[nind][0]),Round))
					normals.append(round(float(norm[nind][1]),Round))
					normals.append(round(float(norm[nind][2]),Round))
					normals_str = ' '.join(map(str, normals))
					obj_group[group][i]["N"] = normals_str
				else:
					obj_group[group][i]["N"] = ''
				i += 1
				
		# Now the dict should have everything
		for group in obj_group.keys():
			for f in obj_group[group].keys():
				print obj_group[group][f]["P"]
				print obj_group[group][f]["T"]
				print obj_group[group][f]["N"]
			
		# create a dictionary to store the polygon data, we always have a point so we can add
		#this directly

		
export_obj_to_rib(obj_file)
