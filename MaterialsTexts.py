#!/usr/bin/env python

#
# Version 0.1 - Copyright (c) 2019 by 
#
# Info:
#
#
# Updates:
#
# License: MIT License
#
#


import sys
import argparse
import csv

#file = sys.argv[1]

def material_ids_to_ri(material_id_list):
	material_ids = material_id_list
	
	material_id_dict = {}
	with open('lego_colors.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(csvfile) # skip the first row
		for row in reader:
			material_id_dict[row[0]] = row[6], row[7], row[8]
	i = 0
	bxdf_mat = {}
	for material_id in material_ids:
		
		# Under the assumption the 1st mat is never 0
		if (int(material_id) == 0):
			bxdf_mat[i] = bxdf_mat[0]
			i += 1
			continue
				
		try:
			color_r, color_g, color_b = material_id_dict[material_id]	
		except KeyError as e:
			color_r, color_g, color_b = [100, 100, 100]
			print 'Warning: Material_ID ' + e.args[0] + ' not found.'
					
		color_r = round((float(color_r) / 255),2)
		color_g = round((float(color_g) / 255),2)
		color_b = round((float(color_b) / 255),2)
		
		bxdf_mat[i] = '\t\tBxdf "PxrSurface" "Material' + material_id + '" "float diffuseGain" [1.0] "color diffuseColor" [' + str(color_r) + ' ' + str(color_g) + ' ' + str(color_b) + '] "int diffuseDoubleSided" [1] "color specularFaceColor" [0.1 0.1 0.15] "float specularRoughness" [0.2] "int specularDoubleSided" [0] "float presence" [1]\n'
		i += 1
	
	return bxdf_mat


materials="24,0,0,0"
material_ids = materials.split(',')
		
a = material_ids_to_ri(material_ids)
print a