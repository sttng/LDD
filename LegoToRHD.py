#!/usr/bin/env python

#
# LegoToRHD Version 0.3 - Copyright (c) 2020 by m2m
# based on pyldd2obj Version 0.4.8 - Copyright (c) 2019 by jonnysp 
# LegoToRHD parses LXF files and command line parameters to creates a USDA compliant files.
# 
# Usage: ./LegoToRHD.py /Users/username/Documents/LEGO\ Creations/Models/mylfxfile.lxf -np
#
# Updates:
# 
# 0.3 support for all lxf files without textures
# 0.2 support for all parts without textures
# 0.1 initial version
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

__version__ = "0.3"

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
			rgb_or_dec_str = '({0}, {1}, {2})'.format(self.r, self.g, self.b)
			
		if self.materialType == 'Transparent':
			bxdf_mat_str = texture_strg + '''def Material "Material1"
	{{
		def Shader "pbr"
			{{
				uniform token info:id = "UsdPreviewSurface"
				color3f inputs:diffuseColor = {2}
				float inputs:metallic = 1
				float inputs:roughness = 0
				token outputs:surface
			}}
		token outputs:surface.connect = <…/Material1/pbr.outputs:surface>
	}}\n'''.format(self.materialId, ref_strg, rgb_or_dec_str, round(random.random(), 3))
			
		elif self.materialType == 'Metallic':
			bxdf_mat_str = texture_strg + '''def Material "Material1"
	{{
		def Shader "pbr"
			{{
				uniform token info:id = "UsdPreviewSurface"
				color3f inputs:diffuseColor = {2}
				float inputs:metallic = 1
				float inputs:roughness = 0
				token outputs:surface
			}}
		token outputs:surface.connect = <…/Material1/pbr.outputs:surface>
	}}\n'''.format(self.materialId, ref_strg, rgb_or_dec_str, round(random.random(), 3))
		
		else:
			bxdf_mat_str = texture_strg + '''def Material "Material1"
	{{
		def Shader "pbr"
			{{
				uniform token info:id = "UsdPreviewSurface"
				color3f inputs:diffuseColor = {2}
				float inputs:metallic = 1
				float inputs:roughness = 0
				token outputs:surface
			}}
		token outputs:surface.connect = <…/Material1/pbr.outputs:surface>
	}}\n'''.format(self.materialId, ref_strg, rgb_or_dec_str, round(random.random(), 3))
		
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
		
		out = open(filename + ".usda", "w+")
		#zf = zipfile.ZipFile(filename + "_Bricks_Archive.zip", "w")
		zfmat = zipfile.ZipFile(filename + "_Materials_Archive.zip", "w")
		
		assetsDir = filename + "_assets"
		
		if not os.path.exists(assetsDir):
			os.mkdir(assetsDir)
			#print("Directory " , assetsDir ,  " Created ")
		else:
			print("Directory " , assetsDir ,  " already exists")
		
		total = len(self.scene.Bricks)
		current = 0
		currentpart = 0
		
		# minx used for floor plane later
		minx = 1000
		useplane = cl.useplane
		
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
			float focalLength = 50
			float focusDistance = 5
			float fStop = 5.6
			float horizontalAperture = 41.4214
			float horizontalApertureOffset = 0
			float verticalAperture = 23.299536
			float verticalApertureOffset = 0
			token projection = "perspective"
		
			matrix4d xformOp:transform = ( ({1}, {2}, {3}, {4}), ({5}, {6}, {7}, {8}), ({9}, {10}, {11}, {12}), ({13}, {14}, {15}, {16}) )	
			uniform token[] xformOpOrder = ["xformOp:transform"]
		}}\n'''.format(cam.refID, cam.matrix.n11, cam.matrix.n12, cam.matrix.n13, cam.matrix.n14, cam.matrix.n21, cam.matrix.n22, cam.matrix.n23, cam.matrix.n24, cam.matrix.n31, cam.matrix.n32, cam.matrix.n33, cam.matrix.n34, cam.matrix.n41, cam.matrix.n42, cam.matrix.n43, cam.matrix.n44))

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
					#out.write('\t\t\tdouble3 xformOp:scale = (1, 1, 1)\n')
					out.write('\t\t\tuniform token[] xformOpOrder = ["xformOp:transform"]\n')
					
					# minx used for floor plane later
					if minx > float(n43):
						minx = n43
											
				op = open(written_obj + ".usda", "w+")
				op.write('''#usda 1.0
(
	defaultPrim = "brick_{0}"
	upAxis = "X"
)

def Xform "brick_{0}" (
	assetInfo = {{
		asset identifier = @brick_{0}.usda@
		string name = "brick_{0}"
	}}
	kind = "component"

)
{{\n'''.format(written_obj))
				
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

					op.write('\tdef Mesh "brick_{0}_part_{1}"\n{{\n'.format(written_obj, part))
					
					op.write('\t\tpoint3f[] points = [')
					fmt = ""
					for point in geo.Parts[part].outpositions:
						op.write('{0}({1}, {2}, {3})'.format(fmt, point.x, point.y, point.z))
						fmt = ", "
						#op.write(point.string("v"))
					op.write(']\n')

					op.write('\t\tnormal3f[] normals = [')
					fmt = ""
					for normal in geo.Parts[part].outnormals:
						op.write('{0}({1}, {2}, {3})'.format(fmt, normal.x, normal.y, normal.z))
						fmt = ", "
						#op.write(normal.string("vn"))
					op.write('] (\n')
					op.write('\t\t\tinterpolation = "uniform"\n')
					op.write('\t\t)\n')

					op.write('\t\tfloat2[] primvars:st = [')
					fmt = ""
					for text in geo.Parts[part].textures:
						op.write('{0}({1}, {2})'.format(fmt, text.x, text.y))
						fmt = ", "
						#op.write(text.string("vt"))
					op.write('] (\n')
					op.write('\t\t\tinterpolation = "faceVarying"\n')
					op.write('\t\t)\n')

					decoCount = 0
				#for part in geo.Parts:
					
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
					op.write('\t#rel material:binding = </{0}/{1}>\n'.format(filename, matname))
					op.write('\tcolor3f[] primvars:displayColor = [(1, 0, 0)]\n')
					
					op.write('\t\tint[] faceVertexCounts = [')
					fmt = ""
					for face in geo.Parts[part].faces:
						op.write('{0}3'.format(fmt))
						fmt = ", "
					op.write(']\n')
					
					op.write('\t\tint[] faceVertexIndices = [')
					fmt = ""
					for face in geo.Parts[part].faces:
						if len(geo.Parts[part].textures) > 0:
							op.write('{0}{1},{2},{3}'.format(fmt, face.a + indexOffset - 1, face.b + indexOffset - 1, face.c + indexOffset - 1))
							fmt = ", "
							#out.write(face.string("f",indexOffset,textOffset))  
						else:
							op.write('{0}{1},{2},{3}'.format(fmt, face.a + indexOffset - 1, face.b + indexOffset - 1, face.c + indexOffset - 1))
							fmt = ", "
							#out.write(face.string("f",indexOffset))
	
					op.write(']\n')
					op.write('\t\tuniform token subdivisionScheme = "none"\n\t}\n')

					indexOffset = 1
					textOffset = 1
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
	def "GroundPlane_1" (
		add references = @./assets/GroundPlane_1.usd@
		)
		{{
			double3 xformOp:translate = ({0}, 0, 10)
			float3 xformOp:scale = (200, 1, 200)
			uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:scale"]
		}}\n\n'''.format(minx))
		
		#zf.close()
		zfmat.close()
		out.write('}\n')
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
	
	rib_header = '''#usda 1.0
(
	defaultPrim = "LXF_file"
	upAxis = "X"
	doc = """Generated with LegoToRHD {0} on {1}"""
)

def Xform "LXF_file" (
	assetInfo = {{
		asset identifier = @LXF_file.usda@
		string name = "LXF_file"
	}}
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
		
		with open(obj_filename + '_Scene.usda','wb') as wfd:
			for f in ['rib_header.rib', obj_filename + '.usda']:
				with open(f,'rb') as fd:
					shutil.copyfileobj(fd, wfd, 1024*1024*10)
		os.remove(obj_filename + '.usda')
		os.remove('rib_header.rib')
		
		print "\nNow start Renderman with (for preview):\n./prman -d it -t:-2 {0}{1}_Scene.rib".format(cl.args.searcharchive, os.sep + obj_filename)
		print "Or start Renderman with (for final mode without preview):\n./prman -t:-2 -checkpoint 1m {0}{1}_Scene.rib".format(cl.args.searcharchive, os.sep + obj_filename)
		print "\nFinally denoise the final output with:./denoise {0}{1}.beauty.001.exr\n".format(cl.args.searcharchive, os.sep + obj_filename)
		
	else:
		print("No LDD database found. Please install LEGO Digital-Designer.")

if __name__ == "__main__":
	main()
