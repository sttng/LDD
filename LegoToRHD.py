#!/usr/bin/env python

#
# LegoToRHD Version 0.5.2.1 - Copyright (c) 2020 by m2m
# based on pyldd2obj Version 0.4.8 - Copyright (c) 2019 by jonnysp 
# LegoToRHD parses LXF files and command line parameters to create USDA compliant files.
# 
# Usage: ./LegoToRHD.py /Users/username/Documents/LEGO\ Creations/Models/mylxffile.lxf -np
#
# Updates:
# 0.5.2.1 corrected Windows path handling bugs
# 0.5.2 improved Windows and Python 3 compatibility
# 0.5.1 added reading correct focus distance from lxf file camera
# 0.5.0.3 improved custom2DField handling, adjusted logoonstuds height to better accommodate new custom bricks, fixed decorations bug, improved material assignments handling
# 0.5.0.2 db folder support for modifications (such as custom bricks) in addition to db.lif support
# 0.5.0.1 more logo on studs supported
# 0.5 initial logo on studs support
# 0.4.7 added brick seams via scale factor of 0.99 for each brick (experimental)
# 0.4.6 added nonormals switch (-nn), to ignore normals writing as some parts of LDD seem to have incorrect normals.
# 0.4.5 remove parts writing of normals for the time being
# 0.4.4 small optimization, removal of legacy code
# 0.4.3 added displayColor primvar and other fixes
# 0.4.2 added groundplane
# 0.4.1 small fix on textures
# 0.4 initial texture support - appear transparent however
# 0.3.6 improved efficiency with geo-file referencing
# 0.3.5 initial support for materials but without textures
# 0.3 support for all lxf files without textures
# 0.2 support for all parts without textures
# 0.1 initial version
# 
# License: MIT License
#

from pylddlib import *
import numpy as np
import uuid
import csv
import datetime
import shutil
import ParseCommandLine as cl
import random

__version__ = "0.5.2.1"

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
		self.r = round((float(r) / 255), 3)
		self.g = round((float(g) / 255), 3)
		self.b = round((float(b) / 255), 3)
		
	def string(self, decorationId):
		texture_strg = ''
		ref_strg = ''
		
		if decorationId != None and decorationId != '0':
		# We have decorations
			rgb_or_dec_str = '<../diffuseColor_texture.outputs:rgb>'
			ref_strg = '.connect'
			matId_or_decId = '{0}_{1}'.format(self.materialId, decorationId)
			
			texture_strg = '''
		def Shader "stAttrReader" 
		{{
			uniform token info:id = "UsdPrimvarReader_float2" 
			token inputs:varname = "st"
			float2 outputs:result
		}}

		def Shader "diffuseColor_texture"
		{{
			uniform token info:id = "UsdUVTexture"
			asset inputs:file = @{0}.png@
			float2 inputs:st.connect = <../stAttrReader.outputs:result>
			float3 outputs:rgb
		}}

'''.format(decorationId, round(random.random(), 3))
		
		else:
		# We don't have decorations
			rgb_or_dec_str = '({0}, {1}, {2})'.format(self.r, self.g, self.b)
			matId_or_decId = self.materialId
			
		if self.materialType == 'Transparent':
			#bxdf_mat_str = texture_strg + 
			bxdf_mat_str = '''#usda 1.0
(
	defaultPrim = "material_{0}"
)
def Xform "material_{0}" (
	assetInfo = {{
		asset identifier = @material_{0}.usda@
		string name = "material_{0}"
	}}
	kind = "component"

)
{{
	def Material "material_{0}a"
	{{
		
		token outputs:surface.connect = <surfaceShader.outputs:surface>
{1}		
		def Shader "surfaceShader"
		{{
			uniform token info:id = "UsdPreviewSurface"
			color3f inputs:diffuseColor{3} = {2}
			float inputs:metallic = 0
			float inputs:roughness = 0
			float inputs:opacity = 0.2
			token outputs:surface
		}}
		
	}}
}}\n'''.format(matId_or_decId, texture_strg, rgb_or_dec_str, ref_strg, round(random.random(), 3))
			
		elif self.materialType == 'Metallic':
			bxdf_mat_str = '''#usda 1.0
(
	defaultPrim = "material_{0}"
)
def Xform "material_{0}" (
	assetInfo = {{
		asset identifier = @material_{0}.usda@
		string name = "material_{0}"
	}}
	kind = "component"

)
{{
	def Material "material_{0}a"
	{{
		
		token outputs:surface.connect = <surfaceShader.outputs:surface>
{1}		
		def Shader "surfaceShader"
		{{
			uniform token info:id = "UsdPreviewSurface"
			color3f inputs:diffuseColor{3} = {2}
			float inputs:metallic = 1
			float inputs:roughness = 0
			token outputs:surface
		}}
		
	}}
}}\n'''.format(matId_or_decId, texture_strg, rgb_or_dec_str, ref_strg, round(random.random(), 3))
		
		else:
			bxdf_mat_str = '''#usda 1.0
(
	defaultPrim = "material_{0}"
)
def Xform "material_{0}" (
	assetInfo = {{
		asset identifier = @material_{0}.usda@
		string name = "material_{0}"
	}}
	kind = "component"

)
{{
	def Material "material_{0}a"
	{{
		
		token outputs:surface.connect = <surfaceShader.outputs:surface>
{1}		
		def Shader "surfaceShader"
		{{
			uniform token info:id = "UsdPreviewSurface"
			color3f inputs:diffuseColor{3} = {2}
			float inputs:metallic = 0
			float inputs:roughness = 0
			token outputs:surface
		}}
		
	}}
}}\n'''.format(matId_or_decId, texture_strg, rgb_or_dec_str, ref_strg, round(random.random(), 3))
		
		return bxdf_mat_str

class Converter:
	def LoadDBFolder(self, dbfolderlocation):
		self.database = DBFolderReader(folder=dbfolderlocation)

		if self.database.initok and self.database.fileexist(os.path.join(dbfolderlocation,'Materials.xml')) and self.database.fileexist(MATERIALNAMESPATH + 'EN/localizedStrings.loc'):
			self.allMaterials = Materials(data=self.database.filelist[os.path.join(dbfolderlocation,'Materials.xml')].read());
			self.allMaterials.setLOC(loc=LOCReader(data=self.database.filelist[MATERIALNAMESPATH + 'EN/localizedStrings.loc'].read()))
	
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
		#usedgeo = [] not used currently
		
		start_time = time.time()
		
		out = open(filename + ".usda", "w+")
		#zf = zipfile.ZipFile(filename + "_Bricks_Archive.zip", "w")
		#zfmat = zipfile.ZipFile(filename + "_Materials_Archive.zip", "w")
		
		assetsDir = filename + "_assets"
		
		if not os.path.exists(assetsDir):
			os.mkdir(assetsDir)
			#print("Directory " , assetsDir ,  " Created ")
		else:
			print('Directory {0} already exists'.format(assetsDir))
		
		total = len(self.scene.Bricks)
		current = 0
		currentpart = 0
		
		# miny used for floor plane later
		miny = 1000
		
		useplane = cl.useplane
		usenormal = cl.usenormal
		uselogoonstuds = cl.uselogoonstuds
		fstop = cl.args.fstop
		fov =  cl.args.fov
		
		out.write('''
{
	def Camera "Cam_Minus_1"
		{
			float4[] clippingPlanes = []
			float2 clippingRange = (0.15815565, 6045.622)
			float focalLength = 50
			float focusDistance = 5
			float fStop = 5.6
			float horizontalAperture = 41.4214
			float horizontalApertureOffset = 0
			float verticalAperture = 23.299536
			float verticalApertureOffset = 0
			token projection = "perspective"
		
			double3 xformOp:translate = (0, -2, 80)
			float3 xformOp:rotateXYZ = (-25, 45, 0)
			uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ"]
		}\n''')
		
		for cam in self.scene.Scenecamera:
			
			out.write('''
	def Camera "Cam_{0}"
		{{
			float4[] clippingPlanes = []
			float2 clippingRange = (0.15815565, 6045.622)
			float focalLength = 80
			float focusDistance = {18}
			float fStop = {20}
			float horizontalAperture = 41.4214
			float horizontalApertureOffset = 0
			float verticalAperture = 23.299536
			float verticalApertureOffset = 0
			token projection = "perspective"
		
			matrix4d xformOp:transform = ( ({1}, {2}, {3}, {4}), ({5}, {6}, {7}, {8}), ({9}, {10}, {11}, {12}), ({13}, {14}, {15}, {16}) )
			uniform token[] xformOpOrder = ["xformOp:transform"]
		}}\n'''.format(cam.refID, cam.matrix.n11, cam.matrix.n12, cam.matrix.n13, cam.matrix.n14, cam.matrix.n21, cam.matrix.n22, cam.matrix.n23, cam.matrix.n24, cam.matrix.n31, cam.matrix.n32, cam.matrix.n33, cam.matrix.n34, cam.matrix.n41, cam.matrix.n42, cam.matrix.n43, cam.matrix.n44, cam.fieldOfView, cam.distance, fov, fstop))

		for bri in self.scene.Bricks:
			current += 1

			for pa in bri.Parts:
				currentpart += 1

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
				uniqueId = str(uuid.uuid4().hex)
				material_string = '_' + '_'.join(pa.materials)
				written_obj = geo.designID + material_string
				
				if hasattr(pa, 'decoration'):
					decoration_string = '_' + '_'.join(pa.decoration)
					written_obj = written_obj + decoration_string
				
				if (len(pa.Bones) > flexflag):
					# Flex parts are "unique". Ensure they get a unique filename
					written_obj = written_obj + "_" + uniqueId
					# Create numpy matrix from them and create inverted matrix
					x = np.array([[n11,n21,n31,n41],[n12,n22,n32,n42],[n13,n23,n33,n43],[n14,n24,n34,n44]])
					x_inv = np.linalg.inv(x)
					
					# undoTransformMatrix not used currently. Might use later
					undoTransformMatrix = Matrix3D(n11=x_inv[0][0],n12=x_inv[0][1],n13=x_inv[0][2],n14=x_inv[0][3],n21=x_inv[1][0],n22=x_inv[1][1],n23=x_inv[1][2],n24=x_inv[1][3],n31=x_inv[2][0],n32=x_inv[2][1],n33=x_inv[2][2],n34=x_inv[2][3],n41=x_inv[3][0],n42=x_inv[3][1],n43=x_inv[3][2],n44=x_inv[3][3])
				
				out.write('''
		def "brick{0}_{1}" (
			add references = @./{2}/{1}.usda@
		)
		{{\n'''.format(currentpart, written_obj, assetsDir))
				
				if not (len(pa.Bones) > flexflag):
				# Flex parts don't need to be moved
					out.write('\t\t\tmatrix4d xformOp:transform = ( ({0}, {1}, {2}, {3}), ({4}, {5}, {6}, {7}), ({8}, {9}, {10}, {11}), ({12}, {13}, {14}, {15}) )\n'.format(n11, n12, n13, n14, n21, n22, n23, n24, n31, n32, n33, n34, n41, n42 ,n43, n44))	
					out.write('\t\t\tdouble3 xformOp:scale = ({0}, {0}, {0})\n'.format(random.uniform(0.995, 1.000)))
					out.write('\t\t\tuniform token[] xformOpOrder = ["xformOp:transform", "xformOp:scale"]\n')
					
					# miny used for floor plane later
					if miny > float(n42):
						miny = n42
											
				op = open(written_obj + ".usda", "w+")
				op.write('''#usda 1.0
(
	defaultPrim = "brick_{0}"
	upAxis = "Y"
)

def Xform "brick_{0}" (
	assetInfo = {{
		asset identifier = @{0}.usda@
		string name = "brick_{0}"
	}}
	kind = "component"

)
{{\n'''.format(written_obj))
				
				# transform -------------------------------------------------------
				decoCount = 0
				for part in geo.Parts:
					
					written_geo = str(geo.designID) + '_' + str(part)
					
					geo.Parts[part].outpositions = [elem.copy() for elem in geo.Parts[part].positions]
					geo.Parts[part].outnormals = [elem.copy() for elem in geo.Parts[part].normals]
					
					# translate / rotate only parts with more then 1 bone. This are flex parts
					if (len(pa.Bones) > flexflag):

						written_geo = written_geo + '_' + uniqueId
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

					op.write('\tdef "g{0}" (\n'.format(part))
					op.write('\t\tadd references = @./geo{0}.usda@\n\t)\n\t{{\n'.format(written_geo))
					
					gop = open(os.path.join(assetsDir,"geo" + written_geo + ".usda"), "w+")
					gop.write('''#usda 1.0
(
	defaultPrim = "geo{0}"
	upAxis = "Y"
)

def Xform "geo{0}" (
	assetInfo = {{
		asset identifier = @geo{0}.usda@
		string name = "geo{0}"
	}}
	kind = "component"
)
{{
	def Mesh "mesh{0}"
	{{\n'''.format(written_geo))
					
					gop.write('\t\tpoint3f[] points = [')
					fmt = ""
					for point in geo.Parts[part].outpositions:
						gop.write('{0}({1}, {2}, {3})'.format(fmt, point.x, point.y, point.z))
						fmt = ", "
						
					gop.write(']\n')

					if usenormal == True: # write normals in case flag True
						# WARNING: SOME PARTS MAY HAVE BAD NORMALS. FOR EXAMPLE MAYBE PART: (85861) PL.ROUND 1X1 W. THROUGHG. HOLE
						gop.write('\t\tnormal3f[] normals = [')
						fmt = ""
						for normal in geo.Parts[part].outnormals:
							gop.write('{0}({1}, {2}, {3})'.format(fmt, normal.x, normal.y, normal.z))
							fmt = ", "
							
						gop.write('] (\n')
						gop.write('\t\t\tinterpolation = "vertex"\n')
						gop.write('\t\t)\n')

					#try catch here for possible problems in materials assignment of various g, g1, g2, .. files in lxf file
					try:
						materialCurrentPart = pa.materials[part]
					except IndexError:
						print('WARNING: {0}.g{1} has NO material assignment in lxf. Replaced with color 9. Fix {0}.xml faces values.'.format(pa.designID, part))
						materialCurrentPart = '9'
					
					lddmatri = self.allMaterials.getMaterialRibyId(materialCurrentPart)
					matname = materialCurrentPart

					deco = '0'
					if hasattr(pa, 'decoration') and len(geo.Parts[part].textures) > 0:
						#if decoCount <= len(pa.decoration):
						if decoCount < len(pa.decoration):
							deco = pa.decoration[decoCount]
						decoCount += 1

					extfile = ''
					if not deco == '0':
						extfile = deco + '.png'
						matname += "_" + deco
						decofilename = DECORATIONPATH + deco + '.png'
						if not os.path.isfile(os.path.join(assetsDir, extfile)) and self.database.fileexist(decofilename):
							with open(os.path.join(assetsDir, extfile), "wb") as f:
								f.write(self.database.filelist[decofilename].read())
								f.close()

					if not matname in usedmaterials:
						usedmaterials.append(matname)
						outmat = open(os.path.join(assetsDir,"material_" + matname + ".usda"), "w+")
						
						if not deco == '0':
							outmat.write(lddmatri.string(deco))

						else:
							outmat.write(lddmatri.string(None))
						
						outmat.close()

					op.write('\n\t\tcolor3f[] primvars:displayColor = [({0}, {1}, {2})]\n'.format(lddmatri.r, lddmatri.g, lddmatri.b))
					op.write('\t\trel material:binding = <Material{0}/material_{0}a>\n'.format(matname))
					op.write('''\t\tdef "Material{0}" (
			add references = @./material_{0}.usda@
		)
		{{
		}}
	}}\n\n'''.format(matname))
					
					gop.write('\t\tint[] faceVertexCounts = [')
					fmt = ""
					for face in geo.Parts[part].faces:
						gop.write('{0}3'.format(fmt))
						fmt = ", "
					gop.write(']\n')
					
					gop.write('\t\tint[] faceVertexIndices = [')
					fmt = ""
					for face in geo.Parts[part].faces:
						gop.write('{0}{1},{2},{3}'.format(fmt, face.a , face.b, face.c))
						fmt = ", "
							
					gop.write(']\n')
					#gop.write('\n\t\tcolor3f[] primvars:displayColor = [(1, 0, 0)]\n')
							
					if len(geo.Parts[part].textures) > 0:
						
						gop.write('\n\t\tfloat2[] primvars:st = [')
						fmt = ""
						for text in geo.Parts[part].textures:
							gop.write('{0}({1}, {2})'.format(fmt, text.x, (-1) * text.y))
							fmt = ", "
							
						gop.write('] (\n')
						gop.write('\t\t\tinterpolation = "faceVarying"\n')
						gop.write('\t\t)\n')
					
						gop.write('\t\tint[] primvars:st:indices = [')
						fmt = ""
						for face in geo.Parts[part].faces:
							gop.write('{0}{1},{2},{3}'.format(fmt, face.a, face.b, face.c))
							fmt = ", "
							#out.write(face.string("f",indexOffset,textOffset))
						gop.write(']\n\n')
					
					gop.write('\t\tuniform token subdivisionScheme = "none"\n\t}\n')
					gop.write('}\n')
					gop.close()

				#Logo on studs
				if uselogoonstuds == True: # write logo on studs in case flag True
					a = 0
					for studs in geo.studsFields2D:
						a += 1
						if studs.type == 23:
							for i in range(len(studs.custom2DField)):
								for j in range(len(studs.custom2DField[0])):
									if studs.custom2DField[i][j] in LOGOONSTUDSCONNTYPE: #Valid Connection type which are "allowed" for logo on stud
										if not "logoonstuds" in writtenribs:
											writtenribs.append("logoonstuds")
											dest = shutil.copy('logoonstuds.usdc', assetsDir) 
										op.write('\tdef "stud{0}_{1}_{2}" (\n'.format(a, i, j))
										op.write('\t\tadd references = @./logoonstuds.usdc@\n\t)\n\t{')
										op.write('\t\tfloat xformOp:rotateY = 180')
										op.write('\n\t\tdouble3 xformOp:translate = ({0}, {1}, {2})'.format(-1 * studs.matrix.n41 + j * 0.4 + 0.0145, -1 * studs.matrix.n42 + 0.14, -1 * studs.matrix.n43 + i * 0.4 - 0)) #Values from trial and error: minx of bounding = -0.4, 0.46 =ty of field + 0.14
										op.write('\n\t\tmatrix4d xformOp:transform = ( ({0}, {1}, {2}, {3}), ({4}, {5}, {6}, {7}), ({8}, {9}, {10}, {11}), ({12}, {13}, {14}, {15}) )'.format(studs.matrix.n11, studs.matrix.n12, -1 * studs.matrix.n13, studs.matrix.n14, studs.matrix.n21, studs.matrix.n22, -1 * studs.matrix.n23, studs.matrix.n24, -1 * studs.matrix.n31, -1 * studs.matrix.n32, studs.matrix.n33, studs.matrix.n34, 0, 0, 0, studs.matrix.n44))
										op.write('\n\t\tdouble3 xformOp:scale = ({0}, {0}, {0})'.format(0.81))
										op.write('\n\t\tuniform token[] xformOpOrder = ["xformOp:transform","xformOp:translate","xformOp:scale", "xformOp:rotateY"]\n')
										op.write('\n\t\tcolor3f[] primvars:displayColor = [({0}, {1}, {2})]\n'.format(lddmatri.r, lddmatri.g, lddmatri.b))
										op.write('\t\trel material:binding = <Material{0}/material_{0}a>\n'.format(matname))
										op.write('''\t\tdef "Material{0}" (
				add references = @./material_{0}.usda@
			)
			{{
			}}
	}}\n\n'''.format(matname))

				op.write('}\n')
				# -----------------------------------------------------------------
				op.close()
								
				# Reset index for each part
				indexOffset = 1
				textOffset = 1
				
				out.write('\t\t}\n')
				
				if not written_obj in writtenribs:
					writtenribs.append(written_obj)
					#zf.write(written_obj + '.usda', compress_type=compression)
					dest = shutil.copy(written_obj + '.usda', assetsDir)
				
				os.remove(written_obj + '.usda')
						
		if useplane == True: # write the floor plane in case True
			out.write('''
	def Mesh "GroundPlane_1"
		{{
			float3[] extent = [ (-0.5, -0.1, -0.5), (0.5, 0.1, 0.5)]
			int[] faceVertexCounts = [4, 4]
			int[] faceVertexIndices = [0, 1, 4, 3, 1, 2, 5, 4]
			normal3f[] normals = [(0, 1, 0), (0, 1, 0), (0, 1, 0), (0, 1, 0), (0, 1, 0), (0, 1, 0)]
			point3f[] points = [(-0.5, 0, 0.5), (0, 0, 0.5), (0.5, 0, 0.5), (-0.5, 0, -0.5), (0, 0, -0.5), (0.5, 0, -0.5)]
			float[] primvars:ao = [0, 0.5, 1, 1, 0.1, 1] (
			interpolation = "vertex"
			)
			int[] primvars:ao:indices = [0, 1, 4, 3, 2, 5]
		
			texCoord2f[] primvars:st = [(0, 0), (0.5, 0), (0.5, 1), (0, 1), (1, 0), (1, 1)] (
				interpolation = "vertex"
			)
			int[] primvars:st:indices = [0, 1, 4, 3, 2, 5]
			texCoord2f[] primvars:st1 = [(0, 0), (0.5, 0), (0.5, 1), (0, 1), (1, 0), (1, 1)] (
				interpolation = "vertex"
			)
			int[] primvars:st1:indices = [0, 1, 4, 3, 2, 5]
			uniform token subdivisionScheme = "none"
		
			rel material:binding = </mat>
			
			double3 xformOp:translate = (0, {0}, 0)
			float3 xformOp:scale = (100, 1, 100)
			uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:scale"]
			
		}}\n\n'''.format(miny))
		
		#zf.close()
		#zfmat.close()
		out.write('}\n')
		sys.stdout.write('%s\r' % ('                                                                                                 '))
		print("--- %s seconds ---" % (time.time() - start_time))


def generate_rib_header(infile, srate, pixelvar, width, height, fov, fstop, searcharchive, searchtexture, integrator, integratorParams, useplane, usenormal, uselogoonstuds):
	cwd = os.getcwd()
	infile = os.path.realpath(infile.name)
	infile = os.path.splitext(os.path.basename(infile))[0]
	
	rib_header = '''#usda 1.0
(
	customLayerData = {{
		string creator = "Generated with LegoToRHD {0} on {1}"
	}}
	defaultPrim = "LXF_file"
	metersPerUnit = 1
	upAxis = "Y"
)

def Xform "LXF_file" (
	assetInfo = {{
		asset identifier = @{2}_Scene.usda@
		string name = "LXF_file"
	}}
	kind = "component"

)
'''.format(__version__, datetime.datetime.now(), infile)

	with open('rib_header.rib', 'w') as file_writer:
		file_writer.write(rib_header)
	file_writer.close()
	return True

def main():
	cl.ParseCommandLine('')
	lxf_filename = os.path.realpath(cl.args.infile.name)
	obj_filename = os.path.splitext(os.path.basename(lxf_filename))[0]
	generate_rib_header(cl.args.infile, cl.args.srate, cl.args.pixelvar, cl.args.width, cl.args.height, cl.args.fov, cl.args.fstop, cl.args.searcharchive, cl.args.searchtexture, cl.integrator, cl.integratorParams, cl.useplane, cl.usenormal, cl.uselogoonstuds)

	converter = Converter()
	print('LegoToRHD Version ' + __version__)
	if os.path.isdir(FindDBFolder()):
		print('Found DB folder. Will use DB folder instead of db.lif!')
		global PRIMITIVEPATH
		global GEOMETRIEPATH
		global DECORATIONPATH
		global MATERIALNAMESPATH
		setDBFolderVars(dbfolderlocation = FindDBFolder()) #Required to set in pylddlib... dirty !
		PRIMITIVEPATH = FindDBFolder() + '/Primitives/'
		GEOMETRIEPATH = FindDBFolder() + '/Primitives/LOD0/'
		DECORATIONPATH = FindDBFolder() + '/Decorations/'
		MATERIALNAMESPATH = FindDBFolder() + '/MaterialNames/'
		converter.LoadDBFolder(dbfolderlocation = FindDBFolder())
	
	elif os.path.exists(FindDatabase()):
		converter.LoadDatabase(databaselocation = FindDatabase())
		
	else:
		print('No LDD database found. Please install LEGO Digital-Designer.')
		os._exit()
	
	converter.LoadScene(filename=lxf_filename)
	converter.Export(filename=obj_filename)
	
	with open(obj_filename + '_Scene.usda','wb') as wfd:
		for f in ['rib_header.rib', obj_filename + '.usda']:
			with open(f,'rb') as fd:
				shutil.copyfileobj(fd, wfd, 1024*1024*10)
	os.remove(obj_filename + '.usda')
	os.remove('rib_header.rib')
		
	print("\nNow start usdcat to convert from usda to usdc with :\n./usdcat -f -o {0}{1}_Scene.usdc {0}{1}_Scene.usda".format(cl.args.searcharchive, '/' + obj_filename))
	print("\nFinally put the file into an usdz archive with:./usdzconvert {0}{1}_Scene.usdc\n".format(cl.args.searcharchive, '/' + obj_filename))

if __name__ == "__main__":
	main()
