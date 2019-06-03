#!/usr/bin/env python
#
# pyldd2obj Version 0.4.3 - Copyright (c) 2019 by jonnysp 
#
# License: MIT License
#

import os
import sys
import math
import struct
import zipfile
from xml.dom import minidom
import time
import numpy as np
import uuid
import csv
import datetime
import shutil
import ParseCommandLine as cl
from _version import __version__

compression = zipfile.ZIP_DEFLATED

if sys.version_info < (3, 0):
	reload(sys)
	sys.setdefaultencoding('utf-8')

PRIMITIVEPATH = '/Primitives/'
GEOMETRIEPATH = PRIMITIVEPATH + 'LOD0/'
DECORATIONPATH = '/Decorations/'
MATERIALNAMESPATH = '/MaterialNames/'

class Matrix3D(object):
	def __init__(self, n11=1,n12=0,n13=0,n14=0,n21=0,n22=1,n23=0,n24=0,n31=0,n32=0,n33=1,n34=0,n41=0,n42=0,n43=0,n44=1):
		self.n11 = n11
		self.n12 = n12
		self.n13 = n13
		self.n14 = n14
		self.n21 = n21
		self.n22 = n22
		self.n23 = n23
		self.n24 = n24
		self.n31 = n31
		self.n32 = n32
		self.n33 = n33
		self.n34 = n34
		self.n41 = n41
		self.n42 = n42
		self.n43 = n43
		self.n44 = n44

	def __str__(self):
		return '[{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15}]'.format(self.n11, self.n12, self.n13,self.n14,self.n21, self.n22, self.n23,self.n24,self.n31, self.n32, self.n33,self.n34,self.n41, self.n42, self.n43,self.n44)

	def rotate(self,angle=0,axis=0):
		c = math.cos(angle)
		s = math.sin(angle)
		t = 1 - c

		tx = t * axis.x
		ty = t * axis.y
		tz = t * axis.z

		sx = s * axis.x
		sy = s * axis.y
		sz = s * axis.z

		self.n11 = c + axis.x * tx
		self.n12 = axis.y * tx + sz
		self.n13 = axis.z * tx - sy
		self.n14 = 0

		self.n21 = axis.x * ty - sz
		self.n22 = c + axis.y * ty
		self.n23 = axis.z * ty + sx
		self.n24 = 0

		self.n31 = axis.x * tz + sy
		self.n32 = axis.y * tz - sx
		self.n33 = c + axis.z * tz
		self.n34 = 0

		self.n41 = 0
		self.n42 = 0
		self.n43 = 0
		self.n44 = 1

class Point3D(object):
	def __init__(self, x=0,y=0,z=0):
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		return '[{0},{1},{2}]'.format(self.x, self.y,self.z)

	def string(self,prefix = "v"):
		return '{0} {1:f} {2:f} {3:f}\n'.format(prefix ,self.x , self.y, self.z)

	def transformW(self,matrix):
		x = matrix.n11 * self.x + matrix.n21 * self.y + matrix.n31 * self.z
		y = matrix.n12 * self.x + matrix.n22 * self.y + matrix.n32 * self.z
		z = matrix.n13 * self.x + matrix.n23 * self.y + matrix.n33 * self.z
		self.x = x
		self.y = y
		self.z = z

	def transform(self,matrix):
		x = matrix.n11 * self.x + matrix.n21 * self.y + matrix.n31 * self.z + matrix.n41
		y = matrix.n12 * self.x + matrix.n22 * self.y + matrix.n32 * self.z + matrix.n42
		z = matrix.n13 * self.x + matrix.n23 * self.y + matrix.n33 * self.z + matrix.n43
		self.x = x
		self.y = y
		self.z = z

	def copy(self):
		return Point3D(x=self.x,y=self.y,z=self.z)

class Point2D(object):
	def __init__(self, x=0,y=0):
		self.x = x
		self.y = y
	def __str__(self):
		return '[{0},{1}]'.format(self.x, self.y * -1)
	def string(self,prefix="t"):
		return '{0} {1:f} {2:f}\n'.format(prefix , self.x, self.y * -1 )
	def copy(self):
		return Point2D(x=self.x,y=self.y)

class Face(object):
	def __init__(self,a=0,b=0,c=0):
		self.a = a
		self.b = b
		self.c = c
	def string(self,prefix="f", indexOffset=0 ,textureoffset=0):
		if textureoffset == 0:
			return prefix + ' {0}//{0} {1}//{1} {2}//{2}\n'.format(self.a + indexOffset, self.b + indexOffset, self.c + indexOffset)
		else:
			return prefix + ' {0}/{3}/{0} {1}/{4}/{1} {2}/{5}/{2}\n'.format(self.a + indexOffset, self.b + indexOffset, self.c + indexOffset,self.a + textureoffset, self.b + textureoffset, self.c + textureoffset)
	def __str__(self):
		return '[{0},{1},{2}]'.format(self.a, self.b, self.c)

class Group(object):
	def __init__(self, node):
		self.partRefs = node.getAttribute('partRefs').split(',')
		
class Bone(object):
	def __init__(self, node):
		self.refID = node.getAttribute('refID')
		(a, b, c, d, e, f, g, h, i, x, y, z) = map(float, node.getAttribute('transformation').split(','))
		self.matrix = Matrix3D(n11=a,n12=b,n13=c,n14=0,n21=d,n22=e,n23=f,n24=0,n31=g,n32=h,n33=i,n34=0,n41=x,n42=y,n43=z,n44=1)

class Part(object):
	def __init__(self, node):
		self.isGrouped = False
		self.GroupIDX = 0
		self.Bones = []
		self.refID = node.getAttribute('refID')
		self.designID = node.getAttribute('designID')
		self.materials = list(map(str, node.getAttribute('materials').split(',')))
		self.decoration = False
		
		lastm = '0'
		for i, m in enumerate(self.materials):
			if (m == '0'):
				self.materials[i] = lastm
			else:
				lastm = m
		if node.hasAttribute('decoration'):
			self.decoration = list(map(str,node.getAttribute('decoration').split(',')))
		for childnode in node.childNodes:
			if childnode.nodeName == 'Bone':
				self.Bones.append(Bone(node=childnode)) 

class Brick(object):
	def __init__(self, node):
		self.refID = node.getAttribute('refID')
		self.designID = node.getAttribute('designID')
		self.Parts = []
		for childnode in node.childNodes:
			if childnode.nodeName == 'Part':
				self.Parts.append(Part(node=childnode))

class SceneCamera(object):
	def __init__(self, node):
		self.refID = node.getAttribute('refID')
		(a, b, c, d, e, f, g, h, i, x, y, z) = map(float, node.getAttribute('transformation').split(','))
		self.matrix = Matrix3D(n11=a,n12=b,n13=c,n14=0,n21=d,n22=e,n23=f,n24=0,n31=g,n32=h,n33=i,n34=0,n41=x,n42=y,n43=z,n44=1)
		self.fieldOfView = float(node.getAttribute('fieldOfView'))
		self.distance = float(node.getAttribute('distance'))

class Scene(object):
	def __init__(self, file):
		self.Name = ''
		self.Version = ''
		self.Bricks = []
		self.Scenecamera = []
		self.Groups = []

		data = ''
		if file.endswith('.lxfml'):
			with open(file, "rb") as file:
				data = file.read()
		elif file.endswith('.lxf'):
			zf = zipfile.ZipFile(file, 'r')
			data = zf.read('IMAGE100.LXFML')
		else:
			return

		xml = minidom.parseString(data)
		self.Name = xml.firstChild.getAttribute('name')
				
		for node in xml.firstChild.childNodes: 
			if node.nodeName == 'Meta':
				for childnode in node.childNodes:
					if childnode.nodeName == 'BrickSet':
						self.Version = str(childnode.getAttribute('version'))
			elif node.nodeName == 'Cameras':
				for childnode in node.childNodes:
					if childnode.nodeName == 'Camera':
						self.Scenecamera.append(SceneCamera(node=childnode))
			elif node.nodeName == 'Bricks':
				for childnode in node.childNodes:
					if childnode.nodeName == 'Brick':
						self.Bricks.append(Brick(node=childnode))
			elif node.nodeName == 'GroupSystems':
				for childnode in node.childNodes:
					if childnode.nodeName == 'GroupSystem':
						for childnode in childnode.childNodes:
							if childnode.nodeName == 'Group':
								self.Groups.append(Group(node=childnode))

		for i in range(len(self.Groups)):
			for brick in self.Bricks:
				for part in brick.Parts:
					if part.refID in self.Groups[i].partRefs:
						part.isGrouped = True
						part.GroupIDX = i

		print('Scene "'+ self.Name + '" Brickversion: ' + str(self.Version))

class GeometrieReader(object):
	def __init__(self, data):
		self.offset = 0
		self.data = data
		self.positions = []
		self.normals = []
		self.textures = []
		self.faces = []
		self.bonemap = {}
		self.texCount = 0
		self.outpositions = []
		self.outnormals = []

		if self.readInt() == 1111961649:
			self.valueCount = self.readInt()
			self.indexCount = self.readInt()
			self.faceCount = int(self.indexCount / 3)
			options = self.readInt()

			for i in range(0, self.valueCount):
				self.positions.append(Point3D(x=self.readFloat(),y= self.readFloat(),z=self.readFloat()))

			for i in range(0, self.valueCount):
				 self.normals.append(Point3D(x=self.readFloat(),y= self.readFloat(),z=self.readFloat()))

			if (options & 3) == 3:
				self.texCount = self.valueCount
				for i in range(0, self.valueCount):
					self.textures.append(Point2D(x=self.readFloat(), y=self.readFloat()))

			for i in range(0, self.faceCount):
				self.faces.append(Face(a=self.readInt(),b=self.readInt(),c=self.readInt()))

			if (options & 48) == 48:
				num = self.readInt()
				self.offset += (num * 4) + (self.indexCount * 4)
				num = self.readInt()
				self.offset += (3 * num * 4) + (self.indexCount * 4)

			bonelength = self.readInt()
			self.bonemap = [0] * self.valueCount

			if (bonelength > self.valueCount) or (bonelength > self.faceCount):
				datastart = self.offset
				self.offset += bonelength
				for i in range(0, self.valueCount):
					boneoffset = self.readInt() + 4
					self.bonemap[i] = self.read_Int(datastart + boneoffset)
	
	def read_Int(self,_offset):
		if sys.version_info < (3, 0):
			return struct.unpack_from('i', self.data, _offset)[0]
		else:
			return int.from_bytes(self.data[_offset:_offset + 4], byteorder='little')

	def readInt(self):
		if sys.version_info < (3, 0):
			ret = struct.unpack_from('i', self.data, self.offset)[0]
		else:
			ret = int.from_bytes(self.data[self.offset:self.offset + 4], byteorder='little')
		self.offset += 4
		return ret

	def readFloat(self):
		ret = struct.unpack_from('f', self.data, self.offset)[0]
		self.offset += 4
		return ret

class Geometrie(object):
	def __init__(self, designID, database):
		self.designID = designID
		self.Parts = {}
		self.Partname = ''
		GeometrieLocation = '{0}{1}{2}'.format(GEOMETRIEPATH, designID,'.g')
		GeometrieCount = 0
		while str(GeometrieLocation) in database.filelist:
			self.Parts[GeometrieCount] = GeometrieReader(data=database.filelist[GeometrieLocation].read())
			GeometrieCount += 1
			GeometrieLocation = '{0}{1}{2}{3}'.format(GEOMETRIEPATH, designID,'.g',GeometrieCount)

		primitive = Primitive(data = database.filelist[PRIMITIVEPATH + designID + '.xml'].read())
		self.Partname = primitive.designname
		# preflex
		for part in self.Parts:
			# transform
			for i, b in enumerate(primitive.Bones):
				# positions
				for j, p in enumerate(self.Parts[part].positions):
					if (self.Parts[part].bonemap[j] == i):
						self.Parts[part].positions[j].transform(b.matrix)
				# normals
				for k, n in enumerate(self.Parts[part].normals):
					if (self.Parts[part].bonemap[k] == i):
						self.Parts[part].normals[k].transformW(b.matrix)

	def valuecount(self):
		count = 0
		for part in self.Parts:
			count += self.Parts[part].valueCount
		return count

	def facecount(self):
		count = 0
		for part in self.Parts:
			count += self.Parts[part].faceCount
		return count

	def texcount(self):
		count = 0
		for part in self.Parts:
			count += self.Parts[part].texCount
		return count

class Bone2():
	def __init__(self,boneId=0, angle=0, ax=0, ay=0, az=0, tx=0, ty=0, tz=0):
		self.boneId = boneId
		rotationMatrix = Matrix3D()
		rotationMatrix.rotate(angle = -angle * math.pi / 180.0,axis = Point3D(x=ax,y=ay,z=az))
		p = Point3D(x=tx,y=ty,z=tz)
		p.transformW(rotationMatrix)
		rotationMatrix.n41 -= p.x
		rotationMatrix.n42 -= p.y
		rotationMatrix.n43 -= p.z
		self.matrix = rotationMatrix

class Primitive():
	def __init__(self,data):
		self.designname = ''
		self.Bones = []
		xml = minidom.parseString(data)
		for node in xml.firstChild.childNodes: 
			if node.nodeName == 'Flex': 
				for node in node.childNodes:
					if node.nodeName == 'Bone':
						self.Bones.append(Bone2(boneId=int(node.getAttribute('boneId')), angle=float(node.getAttribute('angle')), ax=float(node.getAttribute('ax')), ay=float(node.getAttribute('ay')), az=float(node.getAttribute('az')), tx=float(node.getAttribute('tx')), ty=float(node.getAttribute('ty')), tz=float(node.getAttribute('tz'))))
			elif node.nodeName == 'Annotations':
				for childnode in node.childNodes:
					if childnode.nodeName == 'Annotation' and childnode.hasAttribute('designname'):
						self.designname = childnode.getAttribute('designname')

class LOCReader(object):
	def __init__(self, data):
		self.offset = 0
		self.values = {}
		self.data = data
		if sys.version_info < (3, 0):
			if ord(self.data[0]) == 50 and ord(self.data[1]) == 0:
				self.offset += 2
				while self.offset < len(self.data):
					key = self.NextString().replace('Material', '')
					value = self.NextString()
					self.values[key] = value
		else:
			if int(self.data[0]) == 50 and int(self.data[1]) == 0:
				self.offset += 2
				while self.offset < len(self.data):
					key = self.NextString().replace('Material', '')
					value = self.NextString()
					self.values[key] = value

	def NextString(self):
		out = ''
		if sys.version_info < (3, 0):
			t = ord(self.data[self.offset])
			self.offset += 1
			while not t == 0:
				out = '{0}{1}'.format(out,chr(t))
				t = ord(self.data[self.offset])
				self.offset += 1
		else:
			t = int(self.data[self.offset])
			self.offset += 1
			while not t == 0:
				out = '{0}{1}'.format(out,chr(t))
				t = int(self.data[self.offset])
				self.offset += 1

		return out

class Materials(object):
	def __init__(self, data):
		self.Materials = {}
		
		#Added
		self.MaterialsRi = {}
		material_id_dict = {}
		with open('lego_colors.csv', 'r') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			next(csvfile) # skip the first row
			for row in reader:
				material_id_dict[row[0]] = row[6], row[7], row[8], row[9]
		#Added end
		
		xml = minidom.parseString(data)
		for node in xml.firstChild.childNodes: 
			if node.nodeName == 'Material':
				self.Materials[node.getAttribute('MatID')] = Material(r=int(node.getAttribute('Red')), g=int(node.getAttribute('Green')), b=int(node.getAttribute('Blue')), a=int(node.getAttribute('Alpha')), mtype=str(node.getAttribute('MaterialType')))
				
				self.MaterialsRi[node.getAttribute('MatID')] = MaterialRi(materialid=node.getAttribute('MatID'), r=int(material_id_dict[node.getAttribute('MatID')][0]), g=int(material_id_dict[node.getAttribute('MatID')][1]), b=int(material_id_dict[node.getAttribute('MatID')][2]), mattype=str(material_id_dict[node.getAttribute('MatID')][3]))

	def setLOC(self, loc):
		for key in loc.values:
			if key in self.Materials:
				self.Materials[key].name = loc.values[key]

	def getMaterialbyId(self, mid):
		return self.Materials[mid]
		
	def getMaterialRibyId(self, mid):
		return self.MaterialsRi[mid]

class Material(object):
	def __init__(self, r, g, b, a, mtype):
		self.name = ''
		self.mattype = mtype
		self.r = float(r)
		self.g = float(g)
		self.b = float(b)
		self.a = float(a)

	def string(self, prefix=""):
		out = '''"{0}color diffuseColor" [{1} {2} {3}]\n'''.format(prefix, self.r / 255, self.g / 255,self.b / 255)
		#out += self.mattype
		if self.a < 255:
			out += 'Ni 1.575\n' + 'd {0}'.format(0.05) + '\n' + 'Tr {0}\n'.format(0.05)
		return out

class MaterialRi(object):
	def __init__(self, materialid, r, g, b, mattype):
		self.name = ''
		self.mattype = mattype
		self.materialid = materialid
		self.r = round((float(r) / 255),2)
		self.g = round((float(g) / 255),2)
		self.b = round((float(b) / 255),2)
		
	def string(self, decoration_id):
		texture_strg = ''
		ref_strg = ''
		
		if decoration_id != None and decoration_id != '0':
		# We have decorations
			rgb_or_dec_str = '"Blend{0}:resultRGB"'.format(decoration_id)
			
			ref_strg = 'reference '
			texture_strg = '''\tPattern "PxrManifold2D" "PxrManifold2D1"
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
			"int operation"  [19]
			"reference color topRGB" ["Texture{0}:resultRGB"]
			"reference float topA" ["Texture{0}:resultA"]
			"color bottomRGB" [{1} {2} {3}]
			"float bottomA" [1]
			"int clampOutput" [1]\n\n'''.format(decoration_id, self.r, self.g, self.b)
		
		else:
		# We don't have decorations
			rgb_or_dec_str = '{0} {1} {2}'.format(self.r, self.g, self.b)
			
		if self.mattype == 'Transparent':
			bxdf_mat_str = texture_strg + '''\tBxdf "PxrSurface" "Transparent {0}"
			"float diffuseGain" [0]
			"color diffuseColor" [0.5 0.5 0.5]
			"int diffuseDoubleSided" [1]
			"int diffuseBackUseDiffuseColor" [1]
			"color diffuseBackColor" [1 1 1]
			"{1}color specularFaceColor" [{2}]
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
			"{1}color refractionColor" [{2}]
			"float glassRoughness" [0.25] 
			"float glassIor" [1.585] # Polycarbonate IOR = 1.584 - 1.586
			"int thinGlass" [1] 
			"float glowGain" [0.0] 
			"color glowColor" [1 1 1] 
			"float presence" [1]\n'''.format(self.materialid, ref_strg, rgb_or_dec_str)
			
		elif self.mattype == 'Metallic':
			bxdf_mat_str = texture_strg + '''\tBxdf "PxrSurface" "Metallic {0}"
			"float diffuseGain" [1.0]
			"{1}color diffuseColor" [{2}] 
			"int diffuseDoubleSided" [1]
			"color specularFaceColor" [0.8 0.8 0.8]
			"color specularIor"  [1.54 1.54 1.54] # ABS Refractive Index, Average value: 1.54
			"float specularRoughness" [0.25]
			"int specularDoubleSided" [0]
			"float presence" [1]\n'''.format(self.materialid, ref_strg, rgb_or_dec_str)
		
		else:
			bxdf_mat_str = texture_strg + '''\tBxdf "PxrSurface" "Solid Material {0}" 
			"float diffuseGain" [1.0] 
			"{1}color diffuseColor" [{2}] 
			"int diffuseDoubleSided" [1]
			"color specularFaceColor" [0.1 0.1 0.15]
			"color specularIor" [1.54 1.54 1.54] # ABS Refractive Index, Average value: 1.54
			"float specularRoughness" [0.25]
			"int specularDoubleSided" [0]
			"float presence" [1]\n'''.format(self.materialid, ref_strg, rgb_or_dec_str)
		
		return bxdf_mat_str


class DBinfo(object):
	def __init__(self, data):
		xml = minidom.parseString(data)
		self.Version = xml.getElementsByTagName('Bricks')[0].attributes['version'].value
		print('DB Version: ' + str(self.Version))

class LIFFile():
	def __init__(self, name, offset, size, handle):
		self.handle = handle
		self.name = name
		self.offset = offset
		self.size = size

	def read(self):
		self.handle.seek(self.offset, 0)
		return self.handle.read(self.size)

class LIFReader(object):
	def __init__(self, file):
		self.packedFilesOffset = 84
		self.filelist = {}
		self.initok = False
		self.location = file
		self.dbinfo = None

		try:
			self.filehandle = open(self.location, "rb")
			self.filehandle.seek(0, 0)
		except Exception as e:
			self.initok = False
			print("Database FAIL")
			return
		else:
			if self.filehandle.read(4).decode() == "LIFF":
				self.parse(prefix='', offset=self.readInt(offset=72) + 64)
				if self.fileexist('/Materials.xml') and self.fileexist('/info.xml'):
					self.dbinfo = DBinfo(data=self.filelist['/info.xml'].read())
					print("Database OK.")
					self.initok = True
				else:
					print("Database ERROR")
			else:
				print("Database FAIL")
				self.initok = False

	def fileexist(self,filename):
		return filename in self.filelist

	def parse(self, prefix='', offset=0):
		if prefix == '':
			offset += 36
		else:
			offset += 4

		count = self.readInt(offset=offset)

		for i in range(0, count):
			offset += 4
			entryType = self.readShort(offset=offset)
			offset += 6

			entryName = '{0}{1}'.format(prefix,'/');
			self.filehandle.seek(offset + 1, 0)
			if sys.version_info < (3, 0):
				t = ord(self.filehandle.read(1))
			else:
				t = int.from_bytes(self.filehandle.read(1), byteorder='big')

			while not t == 0:
				entryName ='{0}{1}'.format(entryName,chr(t))
				self.filehandle.seek(1, 1)
				if sys.version_info < (3, 0):
					t = ord(self.filehandle.read(1))
				else:
					t = int.from_bytes(self.filehandle.read(1), byteorder='big')

				offset += 2

			offset += 6
			self.packedFilesOffset += 20

			if entryType == 1:
				offset = self.parse(prefix=entryName, offset=offset)
			elif entryType == 2:
				fileSize = self.readInt(offset=offset) - 20
				self.filelist[entryName] = LIFFile(name=entryName, offset=self.packedFilesOffset, size=fileSize, handle=self.filehandle)
				offset += 24
				self.packedFilesOffset += fileSize

		return offset

	def readInt(self, offset=0):
		self.filehandle.seek(offset, 0)
		if sys.version_info < (3, 0):
			return struct.unpack('>i', self.filehandle.read(4))[0]
		else:
			return int.from_bytes(self.filehandle.read(4), byteorder='big')

	def readShort(self, offset=0):
		self.filehandle.seek(offset, 0)
		if sys.version_info < (3, 0):
			return struct.unpack('>h', self.filehandle.read(2))[0]
		else:
			return int.from_bytes(self.filehandle.read(2), byteorder='big')

class Converter(object):
	def LoadDatabase(self,databaselocation):
		self.database = LIFReader(file=databaselocation)

		if self.database.initok and self.database.fileexist('/Materials.xml') and self.database.fileexist(MATERIALNAMESPATH + 'EN/localizedStrings.loc'):
			self.allMaterials = Materials(data=self.database.filelist['/Materials.xml'].read());
			self.allMaterials.setLOC(loc=LOCReader(data=self.database.filelist[MATERIALNAMESPATH + 'EN/localizedStrings.loc'].read()))

	def LoadScene(self,filename):
		if self.database.initok:
			self.scene = Scene(file=filename)

	def Export(self,filename):
		start_time = time.time()

		indexOffset = 1
		textOffset = 1
		usedmaterials = []
		geometriecache = {}
		writtenribs = []

		out = open(filename + ".rib", "w+")
		zf = zipfile.ZipFile(filename + "_Bricks_Archive.zip", "w")
		zfmat = zipfile.ZipFile(filename + "_Materials_Archive.zip", "w")
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

			for pa in bri.Parts:

				if pa.designID not in geometriecache:
					geo = Geometrie(designID=pa.designID, database=self.database)
					geometriecache[pa.designID] = geo
					print(" (" + geo.designID + ") " + geo.Partname)
				else:
					geo = geometriecache[pa.designID]
					print("-(" + geo.designID + ") " + geo.Partname)
				
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
					out.write("\t\tConcatTransform [{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15}]\n\t\tScale 1 1 1\n".format(n11, n12, -1 * n13, n14, n21, n22, -1 * n23, n24, -1 * n31, -1 * n32, n33, n34, n41, n42 ,-1 * n43, n44))
					
					if minx > float(n43):
						minx = n43
				
				uniqueId = str(uuid.uuid4())
				material_string = '_' + '_'.join(pa.materials)
				written_obj = geo.designID + material_string
				
				if pa.decoration:
					decoration_string = '_' + '_'.join(pa.decoration)
					written_obj = written_obj + decoration_string
				
				if (len(pa.Bones) > flexflag):
				# Flex parts are "unique". Ensure they get a unique filename
					written_obj = written_obj + "_" + uniqueId
				
				out2 = open(written_obj + ".obj", "w+")
				out2.write("o brick_" + geo.designID + '\n')
				
				op = open(written_obj + ".rib", "w+")
				op.write("##RenderMan RIB-Structure 1.1 Entity\n")
				
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
									geo.Parts[part].outpositions[j].transform(b.matrix)
									
									#transform with inverted values (to undo the transformation)
									#geo.Parts[part].outpositions[j].transform(undoTransformMatrix)
									
							# normals
							for k, n in enumerate(geo.Parts[part].normals):
								if (geo.Parts[part].bonemap[k] == i):
									geo.Parts[part].outnormals[k].transformW(b.matrix)
									
									#transform with inverted values (to undo the transformation)
									#geo.Parts[part].outnormals[k].transformW(undoTransformMatrix)

				decoCount = 0
				for part in geo.Parts:
					
					out2.write("g " + str(part) + '\n')
					
					if not part == 0:
						out2.write("# From file: " + geo.designID + ".g" + str(part) + '\n')
					else:
						out2.write("# From file: " + geo.designID + ".g\n")
					
					for point in geo.Parts[part].outpositions:
						out2.write(point.string("v"))

					for normal in geo.Parts[part].outnormals:
						out2.write(normal.string("vn"))

					for text in geo.Parts[part].textures:
						#out.write(text.string("vt"))
						# Renderman and obj st y coordinates are inverted
						out2.write('vt {0} {1}\n'.format(text.x, text.y))

					lddmat = self.allMaterials.getMaterialbyId(pa.materials[part])
					lddmatri = self.allMaterials.getMaterialRibyId(pa.materials[part])
					#matname = lddmat.name
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

								if os.path.exists(FindRmtree()):
									txmake_cmd = FindRmtree() + 'bin/txmake -t:8 -compression zip -mode clamp -resize up {0} {1}.tex'.format(extfile, deco)
									os.system(txmake_cmd)
								else:
									print("RMANTREE environment variable not set correctly. Set with: export RMANTREE=/Applications/Pixar/RenderManProServer-22.5/")

					if not matname in usedmaterials:
						usedmaterials.append(matname)
						outmat = open("material_" + matname + ".rib", "w+")
						
						if not deco == '0':
							outmat.write(lddmatri.string(deco))

						else:
							outmat.write(lddmatri.string(None))
						
						outmat.close()
						zfmat.write("material_" + matname + ".rib", compress_type=compression)
						os.remove("material_" + matname + ".rib")
						
					#out.write("usemtl " + matname + '\n')
					
					op.write('AttributeBegin #begin Brick {0}.{1}\nAttribute "identifier" "uniform string name" ["Brick {0}.{1}"]\n'.format(written_obj, part))
					op.write('ReadArchive "' + filename + '_Materials_Archive.zip!material_' + matname + '.rib"\n')
					
					for face in geo.Parts[part].faces:
						op.write('\tPolygon\n')
						# NOTE RENDERMAN is left handed coordinate system, obj is right handed -> z-axis inverted
						op.write('\t\t"P" [ {0} {1} {2} {3} {4} {5} {6} {7} {8} ]\n'.format(geo.Parts[part].outpositions[face.a].x, geo.Parts[part].outpositions[face.a].y, (-1) * geo.Parts[part].outpositions[face.a].z, geo.Parts[part].outpositions[face.b].x, geo.Parts[part].outpositions[face.b].y, (-1) * geo.Parts[part].outpositions[face.b].z, geo.Parts[part].outpositions[face.c].x, geo.Parts[part].outpositions[face.c].y, (-1) * geo.Parts[part].outpositions[face.c].z))
						
						op.write('\t\t"N" [ {0} {1} {2} {3} {4} {5} {6} {7} {8} ]\n'.format(geo.Parts[part].outnormals[face.a].x, geo.Parts[part].outnormals[face.a].y, (-1) * geo.Parts[part].outnormals[face.a].z, geo.Parts[part].outnormals[face.b].x, geo.Parts[part].outnormals[face.b].y, (-1) * geo.Parts[part].outnormals[face.b].z, geo.Parts[part].outnormals[face.c].x, geo.Parts[part].outnormals[face.c].y, (-1) * geo.Parts[part].outnormals[face.c].z))
						
						if len(geo.Parts[part].textures) > 0:
							#out.write(face.string("f",indexOffset,textOffset))
							out2.write(face.string("f",indexOffset,textOffset))
							
							# NOTE RENDERMAN Maps Textures in the T from top to bottom so we
							# calculate 1.0 - t here so the image will map properly
							
							op.write('\t\t"st" [ {0} {1} {2} {3} {4} {5} ]\n'.format(geo.Parts[part].textures[face.a].x, 1 - geo.Parts[part].textures[face.a].y, geo.Parts[part].textures[face.b].x, 1 - geo.Parts[part].textures[face.b].y, geo.Parts[part].textures[face.c].x, 1 - geo.Parts[part].textures[face.c].y))
							
						else:
							#out.write(face.string("f",indexOffset))
							out2.write(face.string("f",indexOffset))
							
					op.write('AttributeEnd #end Brick {0}.{1}\n\n'.format(written_obj, part))

					indexOffset += len(geo.Parts[part].outpositions)
					textOffset += len(geo.Parts[part].textures) 
				# -----------------------------------------------------------------
				op.close()
				out2.write('\n')
				out2.close()
				
				# Reset index for each part
				indexOffset = 1
				textOffset = 1
				
				out.write('\t\tAttribute "identifier" "name" ["'+ written_obj + '"]\n')
				out.write('\t\tReadArchive "' + filename +'_Bricks_Archive.zip!'+ written_obj + '.rib"\n')
				out.write('\tAttributeEnd\n\n')
				
				if not written_obj in writtenribs:
						writtenribs.append(written_obj)
						zf.write(written_obj + '.rib', compress_type=compression)
				
				os.remove(written_obj + '.rib')
				os.remove(written_obj + '.obj')
		
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
		print("--- %s seconds ---" % (time.time() - start_time))


def FindDatabase():
	if os.name =='posix':
		return str(os.path.join(str(os.getenv('USERPROFILE') or os.getenv('HOME')),'Library','Application Support','LEGO Company','LEGO Digital Designer','db.lif'))
	else:
		return str(os.path.join(str(os.getenv('USERPROFILE') or os.getenv('HOME')),'AppData','Roaming','LEGO Company','LEGO Digital Designer','db.lif'))


def FindRmtree():
	if os.name =='posix':
		return str(os.getenv('RMANTREE'))
	else:
		return str(os.getenv('RMANTREE'))


# rib "header" generating routine
def generate_rib_header(infile, srate, pixelvar, width, height, fov, fstop, searcharchive, searchtexture, integrator, integratorParams, useplane):
	#print ('shading rate {} pivel variance {} using {} {}'.format(srate,pixelvar,integrator,integratorParams))
	cwd = os.getcwd()
	infile = os.path.realpath(infile.name)
	infile = os.path.splitext(os.path.basename(infile))[0]
	
	rib_header = '''##RenderMan RIB
# Generated with LegoToR {0} on {1}
version 3.04
Option "searchpath" "string archive" ["{2}"] "string texture" [".:@:{3}lib/RenderManAssetLibrary/EnvironmentMaps/Outdoor/GriffithObservatory.rma:{4}"]
Option "Ri" "int Frame" [1]
	"float PixelVariance" [{5}]
	"string PixelFilterName" ["gaussian"]
	"float[2] PixelFilterWidth" [2 2]
	"int[2] FormatResolution" [{6} {7}]
	"float FormatPixelAspectRatio" [1]
	"float[2] Clipping" [0.1 10000]
	"float[4] ScreenWindow" [-1 1 -0.5625 0.5625]
	"float[2] Shutter" [0 0]
Option "bucket" "string order" ["circle"]
Option "statistics" "int level" [1] "string xmlfilename" ["{8}.xml"]

{9}
Hider "raytrace" "int minsamples" [32] "int maxsamples" [64] "float darkfalloff" [0.025] "int incremental" [1] "string pixelfiltermode" ["importance"]
ShadingRate {10}

# Beauty
DisplayChannel "color Ci"
DisplayChannel "float a"
DisplayChannel "color mse" "string source" "color Ci" "string statistics" "mse"
 
# Shading
DisplayChannel "color albedo" "string source" "color lpe:nothruput;noinfinitecheck;noclamp;unoccluded;overwrite;C(U2L)|O"
DisplayChannel "color albedo_var" "string source" "color lpe:nothruput;noinfinitecheck;noclamp;unoccluded;overwrite;C(U2L)|O" "string statistics" "variance"
DisplayChannel "color diffuse" "string source" "color lpe:C(D[DS]*[LO])|O"
DisplayChannel "color diffuse_mse" "string source" "color lpe:C(D[DS]*[LO])|O" "string statistics" "mse"
DisplayChannel "color specular" "string source" "color lpe:CS[DS]*[LO]"
DisplayChannel "color specular_mse" "string source" "color lpe:CS[DS]*[LO]" "string statistics" "mse"
 
# Geometry
DisplayChannel "float zfiltered" "string source" "float z" "string filter" "gaussian"
DisplayChannel "float zfiltered_var" "string source" "float z" "string filter" "gaussian" "string statistics" "variance"
DisplayChannel "normal normal" "string source" "normal Nn"
DisplayChannel "normal normal_var" "string source" "normal Nn" "string statistics" "variance"
DisplayChannel "vector forward" "string source" "vector motionFore"
DisplayChannel "vector backward" "string source" "vector motionBack"

Projection "PxrCamera" "float fov" [{11}] "float fStop" [3.5] "float focalLength" [0.8] "float focalDistance" [5] "point focus1" [0.0 0.0 -1] "point focus2" [1 0.0 -1] "point focus3" [1 1 -1]\n'''.format(__version__, datetime.datetime.now(), str(searcharchive) + os.sep, FindRmtree(), str(searchtexture) + os.sep, pixelvar, width, height, str(cwd) + os.sep + str(infile), integrator, srate, fov)

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
		
	#except Exception as e:
	#	print("Missing Paramenter:" + str(cl.args.infile) + " infile.lfx exportname (without extension)")
	#	return

	converter = Converter()
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
		
	else:
		print("no LDD database found please install LEGO-Digital-Designer")

if __name__ == "__main__":
	main()
