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
			material_id_dict[row[0]] = row[6], row[7], row[8], row[9]
			
	i = 0
	bxdf_mat = {}
	for material_id in material_ids:
		
		# Under the assumption the 1st mat is never 0
		if (int(material_id) == 0):
			bxdf_mat[i] = bxdf_mat[0]
			i += 1
			continue
				
		try:
			color_r, color_g, color_b, material_type = material_id_dict[material_id]
		except KeyError as e:
			color_r, color_g, color_b = [100, 100, 100]
			print 'Warning: Material_ID ' + e.args[0] + ' not found.'
				
		color_r = round((float(color_r) / 255),2)
		color_g = round((float(color_g) / 255),2)
		color_b = round((float(color_b) / 255),2)
		
		if material_type == 'Transparent':
			bxdf_mat[i] = '\t\tBxdf "PxrSurface" "Transparent ' + material_id + '" "float diffuseGain" [0] "color diffuseColor" [0.5 0.5 0.5] "int diffuseDoubleSided" [1] "int diffuseBackUseDiffuseColor" [1] "color diffuseBackColor" [1 1 1] "color specularFaceColor" [' + str(color_r) + ' ' + str(color_g) + ' ' + str(color_b) + '] "color specularEdgeColor" [0.2 0.2 0.2] "float specularRoughness" [0.1]    "int specularDoubleSided" [1] "color clearcoatFaceColor" [0 0 0] "color clearcoatEdgeColor" [0 0 0] "color clearcoatIor" [1.5 1.5 1.5] "color clearcoatExtinctionCoeff" [0.0 0.0 0.0] "float clearcoatRoughness" [0.0] "float iridescenceFaceGain" [0] "float iridescenceEdgeGain" [0] "color iridescencePrimaryColor" [1 0 0] "color iridescenceSecondaryColor" [0 0 1] "float iridescenceRoughness" [0.2] "float fuzzGain" [0.0] "color fuzzColor" [1 1 1] "float fuzzConeAngle" [8] "float refractionGain" [1] "float reflectionGain" [0.2] "color refractionColor" [1 1 1] "float glassRoughness" [0.1] "float glassIor" [1.49] "int thinGlass" [1] "float glowGain" [0.0] "color glowColor" [1 1 1] "float presence" [1]'
		
		elif material_type == 'Metallic':
			bxdf_mat[i] = '\t\tBxdf "PxrSurface" "Metallic ' + material_id + '" "float diffuseGain" [0] "color diffuseColor" [1 1 1] "int diffuseDoubleSided" [1] "int diffuseBackUseDiffuseColor" [1] "color diffuseBackColor" [0.18 0.18 0.18] "color specularFaceColor" [' + str(color_r) + ' ' + str(color_g) + ' ' + str(color_b) + '] "float specularRoughness" [.39] "float presence" [1] "float reflectionGain" [.7]\n'
		
		else:
			bxdf_mat[i] = '\t\tBxdf "PxrSurface" "Material ' + material_id + '" "float diffuseGain" [1.0] "color diffuseColor" [' + str(color_r) + ' ' + str(color_g) + ' ' + str(color_b) + '] "int diffuseDoubleSided" [1] "color specularFaceColor" [0.1 0.1 0.15] "float specularRoughness" [0.2] "int specularDoubleSided" [0] "float presence" [1]\n'
		i += 1
	
	return bxdf_mat


def decoration_ids_to_ri(material_id_list, decoration_id_list):
	material_ids = material_id_list
	decoration_ids = decoration_id_list
	# Insert 0 at the beginning. Decorations are never for the "main" brick, the .g brick.
	decoration_ids.insert(0, "0")
	
	print decoration_ids
	
	material_id_dict = {}
	with open('lego_colors.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(csvfile) # skip the first row
		for row in reader:
			material_id_dict[row[0]] = row[6], row[7], row[8], row[9]
			
	i = 0
	bxdf_mat = {}
	
	# materials="24,0,0,0" decoration="0,55125,0,600053"
	
	for i, material_id in enumerate(material_ids):
		print "here" + str(i)
		
		# Under the assumption the 1st mat is never 0
		if (int(material_id) == 0):
			# IF mat is 0 we are processing it like the 1st ma.
			material_id = material_ids[0]
				
		try:
			color_r, color_g, color_b, material_type = material_id_dict[material_id]
		except KeyError as e:
			color_r, color_g, color_b = [100, 100, 100]
			print 'Warning: Material_ID ' + e.args[0] + ' not found.'
				
		color_r = round((float(color_r) / 255),2)
		color_g = round((float(color_g) / 255),2)
		color_b = round((float(color_b) / 255),2)
		
		if decoration_ids[i] != '0':
		# We have a decoration
			if material_type == 'Transparent':
				bxdf_mat[i] = '\t\tBxdf "PxrSurface" "Trans Decoration ' + material_id + '" "float diffuseGain" [0] "color diffuseColor" [0.5 0.5 0.5] "int diffuseDoubleSided" [1] "int diffuseBackUseDiffuseColor" [1] "color diffuseBackColor" [1 1 1] "color specularFaceColor" [' + str(color_r) + ' ' + str(color_g) + ' ' + str(color_b) + '] "color specularEdgeColor" [0.2 0.2 0.2] "float specularRoughness" [0.1]    "int specularDoubleSided" [1] "color clearcoatFaceColor" [0 0 0] "color clearcoatEdgeColor" [0 0 0] "color clearcoatIor" [1.5 1.5 1.5] "color clearcoatExtinctionCoeff" [0.0 0.0 0.0] "float clearcoatRoughness" [0.0] "float iridescenceFaceGain" [0] "float iridescenceEdgeGain" [0] "color iridescencePrimaryColor" [1 0 0] "color iridescenceSecondaryColor" [0 0 1] "float iridescenceRoughness" [0.2] "float fuzzGain" [0.0] "color fuzzColor" [1 1 1] "float fuzzConeAngle" [8] "float refractionGain" [1] "float reflectionGain" [0.2] "color refractionColor" [1 1 1] "float glassRoughness" [0.1] "float glassIor" [1.49] "int thinGlass" [1] "float glowGain" [0.0] "color glowColor" [1 1 1] "float presence" [1]'
			
			elif material_type == 'Metallic':
				bxdf_mat[i] = '\t\tBxdf "PxrSurface" "Metallic Decoration' + material_id + '" "float diffuseGain" [0] "color diffuseColor" [1 1 1] "int diffuseDoubleSided" [1] "int diffuseBackUseDiffuseColor" [1] "color diffuseBackColor" [0.18 0.18 0.18] "color specularFaceColor" [' + str(color_r) + ' ' + str(color_g) + ' ' + str(color_b) + '] "float specularRoughness" [.39] "float presence" [1] "float reflectionGain" [.7]\n'
			
			else:
				bxdf_mat[i] = '\t\tBxdf "PxrSurface" "Material Decoration' + material_id + '" "float diffuseGain" [1.0] "color diffuseColor" [' + str(color_r) + ' ' + str(color_g) + ' ' + str(color_b) + '] "int diffuseDoubleSided" [1] "color specularFaceColor" [0.1 0.1 0.15] "float specularRoughness" [0.2] "int specularDoubleSided" [0] "float presence" [1]\n'

		if decoration_ids[i] == '0':
		# No decoration
			if material_type == 'Transparent':
				bxdf_mat[i] = '\t\tBxdf "PxrSurface" "Transparent ' + material_id + '" "float diffuseGain" [0] "color diffuseColor" [0.5 0.5 0.5] "int diffuseDoubleSided" [1] "int diffuseBackUseDiffuseColor" [1] "color diffuseBackColor" [1 1 1] "color specularFaceColor" [' + str(color_r) + ' ' + str(color_g) + ' ' + str(color_b) + '] "color specularEdgeColor" [0.2 0.2 0.2] "float specularRoughness" [0.1]    "int specularDoubleSided" [1] "color clearcoatFaceColor" [0 0 0] "color clearcoatEdgeColor" [0 0 0] "color clearcoatIor" [1.5 1.5 1.5] "color clearcoatExtinctionCoeff" [0.0 0.0 0.0] "float clearcoatRoughness" [0.0] "float iridescenceFaceGain" [0] "float iridescenceEdgeGain" [0] "color iridescencePrimaryColor" [1 0 0] "color iridescenceSecondaryColor" [0 0 1] "float iridescenceRoughness" [0.2] "float fuzzGain" [0.0] "color fuzzColor" [1 1 1] "float fuzzConeAngle" [8] "float refractionGain" [1] "float reflectionGain" [0.2] "color refractionColor" [1 1 1] "float glassRoughness" [0.1] "float glassIor" [1.49] "int thinGlass" [1] "float glowGain" [0.0] "color glowColor" [1 1 1] "float presence" [1]'
			
			elif material_type == 'Metallic':
				bxdf_mat[i] = '\t\tBxdf "PxrSurface" "Metallic ' + material_id + '" "float diffuseGain" [0] "color diffuseColor" [1 1 1] "int diffuseDoubleSided" [1] "int diffuseBackUseDiffuseColor" [1] "color diffuseBackColor" [0.18 0.18 0.18] "color specularFaceColor" [' + str(color_r) + ' ' + str(color_g) + ' ' + str(color_b) + '] "float specularRoughness" [.39] "float presence" [1] "float reflectionGain" [.7]\n'
			
			else:
				bxdf_mat[i] = '\t\tBxdf "PxrSurface" "Material ' + material_id + '" "float diffuseGain" [1.0] "color diffuseColor" [' + str(color_r) + ' ' + str(color_g) + ' ' + str(color_b) + '] "int diffuseDoubleSided" [1] "color specularFaceColor" [0.1 0.1 0.15] "float specularRoughness" [0.2] "int specularDoubleSided" [0] "float presence" [1]\n'
	
	return bxdf_mat

#materials="24,0,0,0"
#material_ids = materials.split(',')		
#a = material_ids_to_ri(material_ids)
#print a
