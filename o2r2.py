#!/usr/bin/env python

import getpass
import time, random
import sys
import argparse

obj_file = sys.argv[1]


def ObjToRib(ri,File,Round) :
	print "opening : "+File
	# open the file
	ip = open(File,'r')
	#grab the data as lines
	data=ip.readlines()
	verts=[]
	norm=[]
	text=[]
	face=[]
	# for each line check for one of our tokens
	for line in data :
		# we assume that our Tokens are always the first element of the line (which IIRC the rispec specifies)
		# so we split each line and look at the first element
		tokens=line.split()	
		# make sure we have a token to check against
		if(len(tokens) >0 ) :
			if(tokens[0] =="v") :
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
			
	# close the file
	ip.close()

	# now we've grabbed all the data we can process each of the faces and write out the rib
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
		for perface in fd[1:] :
			index=perface.split("/")
			# get the point array index
			pind=int(index[0])-1
			points.append(round(float(verts[pind][0]),Round))
			points.append(round(float(verts[pind][1]),Round))
			points.append(round(float(verts[pind][2]),Round))
			# check for textures and add if there
			if(index[1] !="") :
				tind=int(index[1])-1
				tx.append(round(float(text[tind][0]),Round))
				tx.append(round(float(text[tind][1]),Round))
			# check for normals and check they are there
			if(index[2] !="") :
				nind=int(index[2])-1
				normals.append(round(float(norm[nind][0]),Round))
				normals.append(round(float(norm[nind][1]),Round))
				normals.append(round(float(norm[nind][2]),Round))
		
		# create a dictionary to store the polygon data, we always have a point so we can add
		#this directly
		PolyData={ri.P:points}
		# now see if we have any texture co-ordinates and add them to the dictionary if we do
		if index[1] !="" :
			PolyData[ri.ST]=tx
		# check for normals and add them to the dictionary as well
		if index[2] !="" :
			PolyData[ri.N]=normals
		# finally we generate the Polygon from the data
		ri.Polygon(PolyData)  #{ri.P:points,ri.N:normals,ri.ST:tx})
