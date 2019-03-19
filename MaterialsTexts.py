#!/usr/bin/env python

#
# Version 0.1 - Copyright (c) 2019 by 
#
# Info:
# Creates bxdf string for materials and decorations.
#
# Updates:
#
# License: MIT License
#
#

import os
import sys
import argparse
import csv
import zipfile

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
		if (material_id == '0'):
			# If mat is 0 we are processing it like the 1st mat.
			material_id = material_ids[0]
		
		color_r, color_g, color_b, material_type = material_id_dict[material_id]
				
		#try:
		#	color_r, color_g, color_b, material_type = material_id_dict[material_id]
		#except KeyError as e:
		#	print "material_ids_to_ri" + material_id
		#	color_r, color_g, color_b = [100, 100, 100]
		#	print 'Warning da: Material_ID ' + e.args[0] + ' not found.'
				
		color_r = round((float(color_r) / 255),2)
		color_g = round((float(color_g) / 255),2)
		color_b = round((float(color_b) / 255),2)
		
		bxdf_mat[i] = gen_pxrsurface(color_r, color_g, color_b, material_id, material_type, None)
		i += 1
	
	return bxdf_mat


def decoration_ids_to_ri(material_id_list, decoration_id_list):
	# Materials and Decorations come in the form:
	# materials="24,0,0,0" decoration="55125,0,600053"
	# This means: 
	# Main brick has color 24, 3 sub-bricks have the same color as the main brick.
	# Sub brick 1 and 3 have decorations (55125, 600053), sub brick 2 doesn't (0)
	material_ids = material_id_list
	decoration_ids = decoration_id_list
	# Insert 0 at the beginning. Assume decorations are never for the "main" brick (the .g brick).
	# "55125,0,600053" -> "0,55125,0,600053"
	decoration_ids.insert(0, '0')
	
	material_id_dict = {}
	with open('lego_colors.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(csvfile) # skip the first row
		for row in reader:
			material_id_dict[row[0]] = row[6], row[7], row[8], row[9]
			
	bxdf_mat = {}
	
	i = 0
	for material_id in material_ids:
		
		# Under the assumption the 1st mat is never 0
		if (material_id == '0'):
			# If mat is 0 we are processing it like the 1st mat.
			material_id = material_ids[0]
		
		color_r, color_g, color_b, material_type = material_id_dict[material_id]
		#try:
		#	color_r, color_g, color_b, material_type = material_id_dict[material_id]
		#except KeyError as e:
		#	color_r, color_g, color_b = [100, 100, 100]
		#	material_type = 'Transparent'
		#	print 'decoration_ids_to_ri' + material_id + 'aaa'
		#	print 'Warning here: Material_ID ' + e.args[0] + ' not found.'
				
		color_r = round((float(color_r) / 255),2)
		color_g = round((float(color_g) / 255),2)
		color_b = round((float(color_b) / 255),2)
		
		bxdf_mat[i] = gen_pxrsurface(color_r, color_g, color_b, material_id, material_type, decoration_ids[i])
		i += 1
		
	return bxdf_mat
	
def gen_pxrsurface(r, g, b, material_id, material_type, decoration_id):

	texture_strg = ''
	ref_strg = ''
	
	if decoration_id != None and decoration_id != '0':
	# We have decorations
		mat_rib_name = 'material_' + material_id + '_' + decoration_id
		rgb_or_dec_str = '"Blend' + decoration_id + ':resultRGB"'
		ref_strg = 'reference '
		texture_strg = '''\tPattern "PxrManifold2D" "PxrManifold2D1"
		"float angle" [0]
		"float scaleS" [1]
		"float scaleT" [1]
		"int invertT" [1]
			
	# txmake -mode clamp ./liftmp/db/Decorations/''' + decoration_id + '''.png ''' + decoration_id + '''.tex
	Pattern "PxrTexture" "Texture''' + decoration_id + '''"
		"string filename" ["''' + decoration_id + '''.tex"]
		"int invertT" [0]
		"int linearize" [1]
		"reference struct manifold" ["PxrManifold2D1:result"]
		
	Pattern "PxrBlend" "Blend''' + decoration_id + '''"
		"int operation"  [19]
		"reference color topRGB" ["Texture''' + decoration_id + ''':resultRGB"]
		"reference float topA" ["Texture''' + decoration_id + ''':resultA"]
		"color bottomRGB" [''' + str(r) + ''' ''' + str(g) + ''' ''' + str(b) + ''']
		"float bottomA" [1]
		"int clampOutput" [1]\n\n'''
	
	else:
	# We don't have decorations
		mat_rib_name = 'material_' + material_id
		rgb_or_dec_str = str(r) + ' ' + str(g) + ' ' + str(b)
		
	if material_type == 'Transparent':
		bxdf_mat_str = texture_strg + '''\tBxdf "PxrSurface" "Transparent ''' + material_id + '''"
		"float diffuseGain" [0]
		"color diffuseColor" [0.5 0.5 0.5]
		"int diffuseDoubleSided" [1]
		"int diffuseBackUseDiffuseColor" [1]
		"color diffuseBackColor" [1 1 1]
		"''' + ref_strg + '''color specularFaceColor" [''' + rgb_or_dec_str + ''']
		"color specularEdgeColor" [0.2 0.2 0.2]
		"color specularIor"  [1.585 1.585 1.585] # Polycarbonate IOR = 1.584 - 1.586
		"float specularRoughness" [0.25]
		"int specularDoubleSided" [1]
		"color clearcoatFaceColor" [0 0 0]
		"color clearcoatEdgeColor" [0 0 0]
		"color clearcoatIor" [1.5 1.5 1.5]
		"color clearcoatExtinctionCoeff" [0.0 0.0 0.0]
		"float clearcoatRoughness" [0.0]
		"float iridescenceFaceGain" [0]
		"float iridescenceEdgeGain" [0]
		"color iridescencePrimaryColor" [1 0 0]
		"color iridescenceSecondaryColor" [0 0 1]
		"float iridescenceRoughness" [0.2]
		"float fuzzGain" [0.0]
		"color fuzzColor" [1 1 1]
		"float fuzzConeAngle" [8]
		"float refractionGain" [1]
		"float reflectionGain" [0.2]
		"''' + ref_strg + '''color refractionColor" [''' + rgb_or_dec_str + ''']
		"float glassRoughness" [0.25] 
		"float glassIor" [1.585] # Polycarbonate IOR = 1.584 - 1.586
		"int thinGlass" [1] 
		"float glowGain" [0.0] 
		"color glowColor" [1 1 1] 
		"float presence" [1]\n'''
		
	elif material_type == 'Metallic':
		bxdf_mat_str = texture_strg + '''\tBxdf "PxrSurface" "Metallic ''' + material_id + '''"
		"float diffuseGain" [1.0]
		"''' + ref_strg + '''color diffuseColor" [''' + rgb_or_dec_str + '''] 
		"int diffuseDoubleSided" [1]
		"color specularFaceColor" [0.8 0.8 0.8]
		"color specularIor"  [1.54 1.54 1.54] # ABS Refractive Index, Average value: 1.54
		"float specularRoughness" [0.25]
		"int specularDoubleSided" [0]
		"float presence" [1]\n'''
	
	else:
		bxdf_mat_str = texture_strg + '''\tBxdf "PxrSurface" "Solid Material ''' + material_id + '''" 
		"float diffuseGain" [1.0] 
		"''' + ref_strg + '''color diffuseColor" [''' + rgb_or_dec_str + '''] 
		"int diffuseDoubleSided" [1]
		"color specularFaceColor" [0.1 0.1 0.15]
		"color specularIor" [1.54 1.54 1.54] # ABS Refractive Index, Average value: 1.54
		"float specularRoughness" [0.25]
		"int specularDoubleSided" [0]
		"float presence" [1]\n'''
	
	# Write out Materials to seperate rib files
	mr = open(mat_rib_name + '.rib', 'w')
	mr.write(bxdf_mat_str)
	mr.close()
	z = zipfile.ZipFile("Material_Archive.zip", "a")
	z.write(mat_rib_name + '.rib')
	z.close()
	os.remove(mat_rib_name + '.rib')
	#return bxdf_mat_str
	return 'ReadArchive "Material_Archive.zip!' + mat_rib_name + '.rib"\n'

#materials="24,0,0,0"
#material_ids = materials.split(',')		
#a = material_ids_to_ri(material_ids)
#print a
