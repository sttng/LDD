#!/usr/bin/env python

#
# LegoToRHD Version 0.1 - Copyright (c) 2020 by m2m
# based on pyldd2obj Version 0.4.8 - Copyright (c) 2019 by jonnysp 
# LegoToRHD parses LXF files and command line parameters to creates a USDA compliant files.
# 
# Usage: ./LegoToRHD.py /Users/username/Documents/LEGO\ Creations/Models/mylfxfile.lxf -np
#
# Updates:
# 
# 0.1 Start
# 
# License: MIT License
#

from pyldd2obj import *
import numpy as np
import uuid
import csv
import datetime
import shutil
import ParseCommandLine as cl
import random

__version__ = "0.1"

compression = zipfile.ZIP_STORED #uncompressed archive for USDZ, otherwise would use ZIP_DEFLATED, the usual zip compression

class Materials:
	def __init__(self, data):
		self.MaterialsRi = {}
		material_id_dict = {}
		with open('lego_colors.csv', 'r') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			next(csvfile) # skip the first row
			for row in reader:
				material_id_dict[row[0]] = row[6], row[7], row[8], row[9]
		
		xml = minidom.parseString(data)
		for node in xml.firstChild.childNodes: 
			if node.nodeName == 'Material':
				
				self.MaterialsRi[node.getAttribute('MatID')] = MaterialRi(materialId=node.getAttribute('MatID'), r=int(material_id_dict[node.getAttribute('MatID')][0]), g=int(material_id_dict[node.getAttribute('MatID')][1]), b=int(material_id_dict[node.getAttribute('MatID')][2]), materialType=str(material_id_dict[node.getAttribute('MatID')][3]))

	def setLOC(self, loc):
		for key in loc.values:
			if key in self.MaterialsRi:
				self.MaterialsRi[key].name = loc.values[key]
		
	def getMaterialRibyId(self, mid):
		return self.MaterialsRi[mid]

class MaterialRi:
	def __init__(self, materialId, r, g, b, materialType):
		self.name = ''
		self.materialType = materialType
		self.materialId = materialId
		self.r = round((float(r) / 255), 2)
		self.g = round((float(g) / 255), 2)
		self.b = round((float(b) / 255), 2)
		
	def string(self, decorationId):
		texture_strg = ''
		ref_strg = ''
		
		if decorationId != None and decorationId != '0':
		# We have decorations
			rgb_or_dec_str = '"Blend{0}:resultRGB"'.format(decorationId)
			ref_strg = 'reference '
			
			texture_strg = '''Pattern "PxrManifold2D" "PxrManifold2D1"
	"float angle" [0]
	"float scaleS" [1]
	"float scaleT" [1]
	"int invertT" [1]
	
# txmake -t:8 -compression zip -mode clamp -resize up {0}.png {0}.tex
Pattern "PxrTexture" "Texture{0}"
	"string filename" ["{0}.tex"]
	"int invertT" [0]
	"int linearize" [1]
	"reference struct manifold" ["PxrManifold2D1:result"]
			
Pattern "PxrBlend" "Blend{0}"
	"int operation" [19]
	"reference color topRGB" ["Texture{0}:resultRGB"]
	"reference float topA" ["Texture{0}:resultA"]
	"color bottomRGB" [{1} {2} {3}]
	"float bottomA" [1]
	"int clampOutput" [1]\n\n'''.format(decorationId, self.r, self.g, self.b)
		
		else:
		# We don't have decorations
			rgb_or_dec_str = '{0} {1} {2}'.format(self.r, self.g, self.b)
			
		if self.materialType == 'Transparent':
			bxdf_mat_str = texture_strg + '''Pattern "PxrFractal" "Unevenness" 
	"int surfacePosition" [0]
	"int layers" [1]
	"float frequency" [0.8]
	"float lacunarity" [16.0]
	"float dimension" [5]
	"float erosion" [0.0]
	"float variation" [{3}]
	"int turbulent" [0]

Pattern "PxrNormalMap" "PxrNormalMap1"
	"float bumpScale" [-0.07]
	"reference color inputRGB" ["Unevenness:resultRGB"]
	#"string filename" ["Body_Normal.tex"]
	"normal bumpOverlay" [0 0 0]
	"int invertBump" [0]
	"int orientation" [2]
	"int flipX" [0]
	"int flipY" [0]
	"int firstChannel" [0]
	"int atlasStyle" [0]
	"int invertT" [1]
	"float blur" [0.0]
	"int lerp" [1]
	"int filter" [1]
	"int reverse" [0]
	"float adjustAmount" [0.0]
	"float surfaceNormalMix" [0.0]
	"int disable" [0]

Bxdf "PxrSurface" "Transparent {0}"
	"float diffuseGain" [0.5]
	"{1}color diffuseColor" [{2}]
	"int diffuseDoubleSided" [1]
	"color specularFaceColor" [0.2 0.2 0.2]
	"color specularEdgeColor" [0.2 0.2 0.2]
	"color specularIor" [1.585 1.585 1.585] # Polycarbonate IOR = 1.584 - 1.586
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
	"{1}color refractionColor" [{2}]
	"float glassRoughness" [0.05] 
	"float glassIor" [1.585] # Polycarbonate IOR = 1.584 - 1.586
	"int thinGlass" [1]
	"float glowGain" [0.0]
	"color glowColor" [1 1 1]
	"float presence" [1]\n
	"reference normal bumpNormal" ["PxrNormalMap1:resultN"]'''.format(self.materialId, ref_strg, rgb_or_dec_str, round(random.random(), 3))
			
		elif self.materialType == 'Metallic':
			bxdf_mat_str = texture_strg + '''Pattern "PxrFractal" "Unevenness" 
	"int surfacePosition" [0]
	"int layers" [1]
	"float frequency" [0.8]
	"float lacunarity" [16.0]
	"float dimension" [5]
	"float erosion" [0.0]
	"float variation" [{3}]
	"int turbulent" [0]

Pattern "PxrNormalMap" "PxrNormalMap1"
	"float bumpScale" [-0.07]
	"reference color inputRGB" ["Unevenness:resultRGB"]
	#"string filename" ["Body_Normal.tex"]
	"normal bumpOverlay" [0 0 0]
	"int invertBump" [0]
	"int orientation" [2]
	"int flipX" [0]
	"int flipY" [0]
	"int firstChannel" [0]
	"int atlasStyle" [0]
	"int invertT" [1]
	"float blur" [0.0]
	"int lerp" [1]
	"int filter" [1]
	"int reverse" [0]
	"float adjustAmount" [0.0]
	"float surfaceNormalMix" [0.0]
	"int disable" [0]

Bxdf "PxrSurface" "Metallic {0}"
	"float diffuseGain" [0.5]
	"{1}color diffuseColor" [{2}] 
	"int diffuseDoubleSided" [1]
	"color specularFaceColor" [0.8 0.8 0.8]
	"color specularIor"  [1.54 1.54 1.54] # ABS Refractive Index, Average value: 1.54
	"float specularRoughness" [0.25]
	"int specularDoubleSided" [0]
	"float presence" [1]
	"reference normal bumpNormal" ["PxrNormalMap1:resultN"]\n'''.format(self.materialId, ref_strg, rgb_or_dec_str, round(random.random(), 3))
		
		else:
			bxdf_mat_str = texture_strg + '''Pattern "PxrFractal" "Unevenness" 
	"int surfacePosition" [0]
	"int layers" [1]
	"float frequency" [0.8]
	"float lacunarity" [16.0]
	"float dimension" [5]
	"float erosion" [0.0]
	"float variation" [{3}]
	"int turbulent" [0]

Pattern "PxrNormalMap" "PxrNormalMap1"
	"float bumpScale" [-0.07]
	"reference color inputRGB" ["Unevenness:resultRGB"]
	#"string filename" ["Body_Normal.tex"]
	"normal bumpOverlay" [0 0 0]
	"int invertBump" [0]
	"int orientation" [2]
	"int flipX" [0]
	"int flipY" [0]
	"int firstChannel" [0]
	"int atlasStyle" [0]
	"int invertT" [1]
	"float blur" [0.0]
	"int lerp" [1]
	"int filter" [1]
	"int reverse" [0]
	"float adjustAmount" [0.0]
	"float surfaceNormalMix" [0.0]
	"int disable" [0]

Bxdf "PxrSurface" "Solid Material {0}" 
	"float diffuseGain" [0.5] 
	"{1}color diffuseColor" [{2}] 
	"int diffuseDoubleSided" [1]
	"color specularFaceColor" [0.1 0.1 0.15]
	"color specularIor" [1.54 1.54 1.54] # ABS Refractive Index, Average value: 1.54
	"float specularRoughness" [0.25]
	"int specularDoubleSided" [0]
	"float presence" [1]
	"reference normal bumpNormal" ["PxrNormalMap1:resultN"]\n'''.format(self.materialId, ref_strg, rgb_or_dec_str, round(random.random(), 3))
		
		return bxdf_mat_str

class Converter:
	def LoadDatabase(self,databaselocation):
		self.database = LIFReader(file=databaselocation)

		if self.database.initok and self.database.fileexist('/Materials.xml') and self.database.fileexist(MATERIALNAMESPATH + 'EN/localizedStrings.loc'):
			self.allMaterials = Materials(data=self.database.filelist['/Materials.xml'].read());
			self.allMaterials.setLOC(loc=LOCReader(data=self.database.filelist[MATERIALNAMESPATH + 'EN/localizedStrings.loc'].read()))

	def LoadScene(self,filename):
		if self.database.initok:
			self.scene = Scene(file=filename)

	def Export(self,filename):
		invert = Matrix3D() 
		#invert.n33 = -1 #uncomment to invert the Z-Axis
		
		indexOffset = 1
		textOffset = 1
		usedmaterials = []
		geometriecache = {}
		writtenribs = []
		
		start_time = time.time()
		
		out = open(filename + ".rib", "w+")
		zf = zipfile.ZipFile(filename + "_Bricks_Archive.zip", "w")
		zfmat = zipfile.ZipFile(filename + "_Materials_Archive.zip", "w")
		
		total = len(self.scene.Bricks)
		current = 0
		
		# minx used for floor plane later
		minx = 1000
		useplane = cl.useplane
		
		out.write('''# Camera Minus One
TransformBegin
	Translate 0 -2 80
	Rotate -25 1 0 0
	Rotate 45 0 1 0
	Camera "Cam--1"
		"float shutterOpenTime" [0] 
		"float shutterCloseTime" [1] 
		"int apertureNSides" [0] 
		"float apertureAngle" [0] 
		"float apertureRoundness" [0] 
		"float apertureDensity" [0] 
		"float dofaspect" [1] 
		"float nearClip" [0.100000001] 
		"float farClip" [10000]
TransformEnd\n\n''')
		
		for cam in self.scene.Scenecamera:
			
			out.write('''# Camera {0}
TransformBegin
	ConcatTransform [{1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16}]
	Camera "Cam-{0}"
		"float shutterOpenTime" [0] 
		"float shutterCloseTime" [1] 
		"int apertureNSides" [0] 
		"float apertureAngle" [0] 
		"float apertureRoundness" [0] 
		"float apertureDensity" [0] 
		"float dofaspect" [1] 
		"float nearClip" [0.100000001] 
		"float farClip" [10000]
TransformEnd\n'''.format(cam.refID, cam.matrix.n11, cam.matrix.n12, -1 * cam.matrix.n13, cam.matrix.n14, cam.matrix.n21, cam.matrix.n22, -1 * cam.matrix.n23, cam.matrix.n24, -1 * cam.matrix.n31, -1 * cam.matrix.n32, cam.matrix.n33, cam.matrix.n34, cam.matrix.n41, cam.matrix.n42 ,-1 * cam.matrix.n43, cam.matrix.n44))
		
		out.write('''
Display "{0}{1}{2}.beauty.001.exr" "openexr" "Ci,a,mse,albedo,albedo_var,diffuse,diffuse_mse,specular,specular_mse,zfiltered,zfiltered_var,normal,normal_var,forward,backward" "int asrgba" 1
	"string storage" ["scanline"]
	"string exrpixeltype" ["half"]
	"string compression" ["zips"]
	"float compressionlevel" [45]
	"string camera" ["Cam--1"]\n\n'''.format(os.getcwd(), os.sep, filename))
		
		out.write('WorldBegin\n\tScale 1 1 1\n')
		out.write('''\tAttributeBegin
		Attribute "visibility" "int indirect" [0] "int transmission" [0]
		Attribute "visibility" "int camera" [1]
		Rotate 50 0 1 0
		Rotate -90 1 0 0
		Light "PxrDomeLight" "domeLight" "string lightColorMap" ["islandsun_small.tex"]
	AttributeEnd\n\n''')

		for bri in self.scene.Bricks:
			current += 1

			for pa in bri.Parts:

				if pa.designID not in geometriecache:
					geo = Geometry(designID=pa.designID, database=self.database)
					progress(current ,total , "(" + geo.designID + ") " + geo.Partname, ' ')
					geometriecache[pa.designID] = geo
					
				else:
					geo = geometriecache[pa.designID]
					progress(current ,total , "(" + geo.designID + ") " + geo.Partname ,'-')
				
				# n11=a, n21=d, n31=g, n41=x,
				# n12=b, n22=e, n32=h, n42=y,
				# n13=c, n23=f, n33=i, n43=z,
				# n14=0, n24=0, n34=0, n44=1
				
				# Read out 1st Bone matrix values
				ind = 0
				n11 = pa.Bones[ind].matrix.n11
				n12 = pa.Bones[ind].matrix.n12
				n13 = pa.Bones[ind].matrix.n13
				n14 = pa.Bones[ind].matrix.n14
				n21 = pa.Bones[ind].matrix.n21
				n22 = pa.Bones[ind].matrix.n22
				n23 = pa.Bones[ind].matrix.n23
				n24 = pa.Bones[ind].matrix.n24
				n31 = pa.Bones[ind].matrix.n31
				n32 = pa.Bones[ind].matrix.n32
				n33 = pa.Bones[ind].matrix.n33
				n34 = pa.Bones[ind].matrix.n34
				n41 = pa.Bones[ind].matrix.n41
				n42 = pa.Bones[ind].matrix.n42
				n43 = pa.Bones[ind].matrix.n43
				n44 = pa.Bones[ind].matrix.n44
				
				# Only parts with more then 1 bone are flex parts and for these we need to undo the transformation later
				flexflag = 1
				if (len(pa.Bones) > flexflag):
					
					# Create numpy matrix from them and create inverted matrix
					x = np.array([[n11,n21,n31,n41],[n12,n22,n32,n42],[n13,n23,n33,n43],[n14,n24,n34,n44]])
					x_inv = np.linalg.inv(x)
					
					# undoTransformMatrix not used currently. Might use later
					undoTransformMatrix = Matrix3D(n11=x_inv[0][0],n12=x_inv[0][1],n13=x_inv[0][2],n14=x_inv[0][3],n21=x_inv[1][0],n22=x_inv[1][1],n23=x_inv[1][2],n24=x_inv[1][3],n31=x_inv[2][0],n32=x_inv[2][1],n33=x_inv[2][2],n34=x_inv[2][3],n41=x_inv[3][0],n42=x_inv[3][1],n43=x_inv[3][2],n44=x_inv[3][3])
				
				out.write("\tAttributeBegin\n")
				
				if not (len(pa.Bones) > flexflag):
				# Flex parts don't need to be moved
				# Renderman is lefthanded coordinate system, but LDD is right handed.
					#out.write("\t\tConcatTransform [{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15}]\n\t\tScale 1 1 1\n".format(n11, n12, -1 * n13, n14, n21, n22, -1 * n23, n24, -1 * n31, -1 * n32, n33, n34, n41, n42 ,-1 * n43, n44))
					out.write("\t\tdouble16 xformOp:transform = ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15})\n\t\tdouble3 xformOp:scale = (1, 1, 1)\n".format(n11, n12, -1 * n13, n14, n21, n22, -1 * n23, n24, -1 * n31, -1 * n32, n33, n34, n41, n42 ,-1 * n43, n44))	
					
					# minx used for floor plane later
					if minx > float(n43):
						minx = n43
				
				material_string = '_' + '_'.join(pa.materials)
				written_obj = geo.designID + material_string
				uniqueId = str(uuid.uuid4())
				
				if hasattr(pa, 'decoration'):
					decoration_string = '_' + '_'.join(pa.decoration)
					written_obj = written_obj + decoration_string
				
				if (len(pa.Bones) > flexflag):
				# Flex parts are "unique". Ensure they get a unique filename
					written_obj = written_obj + "_" + uniqueId
				
				op = open(written_obj + ".usda", "w+")
				op.write("#usda 1.0\n")
				
				# transform -------------------------------------------------------
				for part in geo.Parts:
					
					geo.Parts[part].outpositions = [elem.copy() for elem in geo.Parts[part].positions]
					geo.Parts[part].outnormals = [elem.copy() for elem in geo.Parts[part].normals]
					
					# translate / rotate only parts with more then 1 bone. This are flex parts
					if (len(pa.Bones) > flexflag):

						for i, b in enumerate(pa.Bones):
							# positions
							for j, p in enumerate(geo.Parts[part].outpositions):
								if (geo.Parts[part].bonemap[j] == i):
									p.transform( invert * b.matrix)
									
									#transform with inverted values (to undo the transformation)
									#geo.Parts[part].outpositions[j].transform(undoTransformMatrix)
									
							# normals
							for k, n in enumerate(geo.Parts[part].outnormals):
								if (geo.Parts[part].bonemap[k] == i):
									n.transformW( invert * b.matrix)
									
									#transform with inverted values (to undo the transformation)
									#geo.Parts[part].outnormals[k].transformW(undoTransformMatrix)

					op.write('def Mesh "brick_{0}_part_{1}"\n'.format(written_obj, part))
					op.write('{\n')
					
					op.write('\tpoint3f[] points = [')
					fmt = ""
					for point in geo.Parts[part].outpositions:
						op.write('{0}({1}, {2}, {3})'.format(fmt, point.x, point.y, point.z))
						fmt = ", "
						#op.write(point.string("v"))
					op.write(']\n')

					op.write('\tnormal3f[] normals = [')
					fmt = ""
					for normal in geo.Parts[part].outnormals:
						op.write('{0}({1}, {2}, {3})'.format(fmt, normal.x, normal.y, normal.z))
						fmt = ", "
						#op.write(normal.string("vn"))
					op.write('] (\n')
					op.write('\t\tinterpolation = "uniform"\n')
					op.write('\t)\n')

					op.write('\tfloat2[] primvars:st = [')
					fmt = ""
					for text in geo.Parts[part].textures:
						op.write('{0}({1}, {2})'.format(fmt, text.x, text.y))
						fmt = ", "
						#op.write(text.string("vt"))
					op.write('] (\n')
					op.write('\t\tinterpolation = "faceVarying"\n')
					op.write('\t)\n')

				decoCount = 0
				for part in geo.Parts:
					
					lddmatri = self.allMaterials.getMaterialRibyId(pa.materials[part])
					matname = pa.materials[part]

					deco = '0'
					if hasattr(pa, 'decoration') and len(geo.Parts[part].textures) > 0:
						if decoCount <= len(pa.decoration):
							deco = pa.decoration[decoCount]
						decoCount += 1
	
					extfile = ''
					if not deco == '0':
						extfile = deco + '.png'
						matname += "_" + deco
						decofilename = DECORATIONPATH + deco + '.png'
						if not os.path.isfile(extfile) and self.database.fileexist(decofilename):
							with open(extfile, "wb") as f:
								f.write(self.database.filelist[decofilename].read())
								f.close()

					if not matname in usedmaterials:
						usedmaterials.append(matname)
						outmat = open("material_" + matname + ".usda", "w+")
						
						if not deco == '0':
							outmat.write(lddmatri.string(deco))

						else:
							outmat.write(lddmatri.string(None))
						
						outmat.close()
						zfmat.write("material_" + matname + ".usda", compress_type=compression)
						os.remove("material_" + matname + ".usda")

					op.write('#ReadArchive "' + filename + '_Materials_Archive.zip!material_' + matname + '.usda"\n')
					op.write('color3f[] primvars:displayColor = [(1, 0, 0)]')
					
					op.write('\tint[] faceVertexCounts = [')
					fmt = ""
					for face in geo.Parts[part].faces:
						op.write('{0}3'.format(fmt))
						fmt = ", "
					op.write(']\n')
					
					op.write('\tint[] faceVertexIndices = [')
					fmt = ""
					# USD requires 0 started index, thats why -1
					for face in geo.Parts[part].faces:
						op.write('{0}{1},{2},{3}'.format(fmt, face.a + indexOffset - 1, face.b + indexOffset - 1, face.c + indexOffset - 1))
						fmt = ", "
						#out.write(face.string("f",indexOffset))
					op.write(']\n\n')
					
					if len(geo.Parts[part].textures) > 0:
						op.write('\tint[] primvars:st:indices = [')
						fmt = ""
						# USD requires 0 started index, thats why -1
						for face in geo.Parts[part].faces:
							op.write('{0}{1},{2},{3}'.format(fmt, face.a + textOffset - 1, face.b + textOffset - 1, face.c + textOffset - 1))
							fmt = ", "
							#out.write(face.string("f",indexOffset,textOffset))  
						op.write(']\n\n')
					
					op.write('\tuniform token subdivisionScheme = "none"\n}')

					indexOffset += len(geo.Parts[part].outpositions)
					textOffset += len(geo.Parts[part].textures) 
				# -----------------------------------------------------------------
				op.close()
								
				# Reset index for each part
				indexOffset = 1
				textOffset = 1
				
				out.write('\t\tAttribute "identifier" "name" ["'+ written_obj + '"]\n')
				out.write('\t\tReadArchive "' + filename +'_Bricks_Archive.zip!'+ written_obj + '.rib"\n')
				out.write('\tAttributeEnd\n\n')
				
				if not written_obj in writtenribs:
						writtenribs.append(written_obj)
						zf.write(written_obj + '.usda', compress_type=compression)
				
				os.remove(written_obj + '.usda')
						
		if useplane == True: # write the floor plane in case True
			out.write('''\tAttributeBegin
		Attribute "identifier" "string name" ["groundplane"]
		Translate {0} 0 10
		Scale 200 1 200
		Polygon "P" [-0.5 0 -0.5  -0.5 0 0.5  0.5 0 0.5  0.5 0 -0.5]
		"st" [0 0  0 1  1 1  1 0]
	AttributeEnd\n\n'''.format(minx))
		
		zf.close()
		zfmat.close()
		out.write('WorldEnd')
		sys.stdout.write('%s\r' % ('                                                                                                 '))
		print("--- %s seconds ---" % (time.time() - start_time))

def FindRmtree():
	if os.name =='posix':
		rmtree = os.getenv('RMANTREE')
		if rmtree is not None:
			return str(rmtree)
		else:
			print("RMANTREE environment variable not set correctly. Set with: export RMANTREE=/Applications/Pixar/RenderManProServer-22.6/")
			exit()
	else:
		rmtree = os.getenv('RMANTREE')
		if rmtree is not None:
			return str(rmtree)
		else:
			print('RMANTREE environment variable not set correctly. Set with: setx RMANTREE "C:\Program Files\Pixar\RenderManProServer-22.6\" /M')
			exit()


def generate_rib_header(infile, srate, pixelvar, width, height, fov, fstop, searcharchive, searchtexture, integrator, integratorParams, useplane):
	cwd = os.getcwd()
	infile = os.path.realpath(infile.name)
	infile = os.path.splitext(os.path.basename(infile))[0]
	
	rib_header = '''# Generated with LegoToRHD {0} on {1}
#usda 1.0
(
    defaultPrim = "LXF_file"
)

def Xform "LXF_file" (
    assetInfo = {
        asset identifier = @LXF_file.usda@
        string name = "LXF_file"
    }
    kind = "component"

)
'''.format(__version__, datetime.datetime.now(), str(searcharchive) + os.sep, FindRmtree(), str(searchtexture) + os.sep, pixelvar, width, height, str(cwd) + os.sep + str(infile), integrator, srate, fov)

	with open('rib_header.rib', 'w') as file_writer:
		file_writer.write(rib_header)
	file_writer.close()
	return True

def main():
	cl.ParseCommandLine('')
	lxf_filename = os.path.realpath(cl.args.infile.name)
	obj_filename = os.path.splitext(os.path.basename(lxf_filename))[0]
	generate_rib_header(cl.args.infile, cl.args.srate, cl.args.pixelvar, cl.args.width, cl.args.height, cl.args.fov, cl.args.fstop, cl.args.searcharchive, cl.args.searchtexture, cl.integrator, cl.integratorParams, cl.useplane)

	# Clean up before writing
	if os.path.exists(obj_filename + "_Materials_Archive.zip"):
		os.remove(obj_filename + "_Materials_Archive.zip")
	if os.path.exists(obj_filename + "_Bricks_Archive.zip"):
		os.remove(obj_filename + "_Bricks_Archive.zip")

	converter = Converter()
	print("LegoToR Version " + __version__)
	if os.path.exists(FindDatabase()):
		converter.LoadDatabase(databaselocation = FindDatabase())
		converter.LoadScene(filename=lxf_filename)
		converter.Export(filename=obj_filename)
		
		with open(obj_filename + '_Scene.rib','wb') as wfd:
			for f in ['rib_header.rib', obj_filename + '.rib']:
				with open(f,'rb') as fd:
					shutil.copyfileobj(fd, wfd, 1024*1024*10)
		os.remove(obj_filename + '.rib')
		os.remove('rib_header.rib')
		
		print "\nNow start Renderman with (for preview):\n./prman -d it -t:-2 {0}{1}_Scene.rib".format(cl.args.searcharchive, os.sep + obj_filename)
		print "Or start Renderman with (for final mode without preview):\n./prman -t:-2 -checkpoint 1m {0}{1}_Scene.rib".format(cl.args.searcharchive, os.sep + obj_filename)
		print "\nFinally denoise the final output with:./denoise {0}{1}.beauty.001.exr\n".format(cl.args.searcharchive, os.sep + obj_filename)
		
	else:
		print("no LDD database found please install LEGO-Digital-Designer")

if __name__ == "__main__":
	main()
