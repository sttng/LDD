#!/usr/bin/env python
#
# pyldd2obj Version 0.4.8 - Copyright (c) 2019 by jonnysp 
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

if sys.version_info < (3, 0):
	reload(sys)
	sys.setdefaultencoding('utf-8')

PRIMITIVEPATH = '/Primitives/'
GEOMETRIEPATH = PRIMITIVEPATH + 'LOD0/'
DECORATIONPATH = '/Decorations/'
MATERIALNAMESPATH = '/MaterialNames/'

class Matrix3D:
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

	def __mul__(self, other): 
		return Matrix3D(
			self.n11 * other.n11 + self.n21 * other.n12 + self.n31 * other.n13 + self.n41 * other.n14,
			self.n12 * other.n11 + self.n22 * other.n12 + self.n32 * other.n13 + self.n42 * other.n14,
			self.n13 * other.n11 + self.n23 * other.n12 + self.n33 * other.n13 + self.n43 * other.n14,
			self.n14 * other.n11 + self.n24 * other.n12 + self.n34 * other.n13 + self.n44 * other.n14,
			self.n11 * other.n21 + self.n21 * other.n22 + self.n31 * other.n23 + self.n41 * other.n24,
			self.n12 * other.n21 + self.n22 * other.n22 + self.n32 * other.n23 + self.n42 * other.n24,
			self.n13 * other.n21 + self.n23 * other.n22 + self.n33 * other.n23 + self.n43 * other.n24,
			self.n14 * other.n21 + self.n24 * other.n22 + self.n34 * other.n23 + self.n44 * other.n24,
			self.n11 * other.n31 + self.n21 * other.n32 + self.n31 * other.n33 + self.n41 * other.n34,
			self.n12 * other.n31 + self.n22 * other.n32 + self.n32 * other.n33 + self.n42 * other.n34,
			self.n13 * other.n31 + self.n23 * other.n32 + self.n33 * other.n33 + self.n43 * other.n34,
			self.n14 * other.n31 + self.n24 * other.n32 + self.n34 * other.n33 + self.n44 * other.n34,
			self.n11 * other.n41 + self.n21 * other.n42 + self.n31 * other.n43 + self.n41 * other.n44,
			self.n12 * other.n41 + self.n22 * other.n42 + self.n32 * other.n43 + self.n42 * other.n44,
			self.n13 * other.n41 + self.n23 * other.n42 + self.n33 * other.n43 + self.n43 * other.n44,
			self.n14 * other.n41 + self.n24 * other.n42 + self.n34 * other.n43 + self.n44 * other.n44
 			)

class Point3D:
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

class Point2D:
	def __init__(self, x=0,y=0):
		self.x = x
		self.y = y
	def __str__(self):
		return '[{0},{1}]'.format(self.x, self.y * -1)
	def string(self,prefix="t"):
		return '{0} {1:f} {2:f}\n'.format(prefix , self.x, self.y * -1 )
	def copy(self):
		return Point2D(x=self.x,y=self.y)

class Face:
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

class Group:
	def __init__(self, node):
		self.partRefs = node.getAttribute('partRefs').split(',')
		
class Bone:
	def __init__(self, node):
		self.refID = node.getAttribute('refID')
		(a, b, c, d, e, f, g, h, i, x, y, z) = map(float, node.getAttribute('transformation').split(','))
		self.matrix = Matrix3D(n11=a,n12=b,n13=c,n14=0,n21=d,n22=e,n23=f,n24=0,n31=g,n32=h,n33=i,n34=0,n41=x,n42=y,n43=z,n44=1)

class Part:
	def __init__(self, node):
		self.isGrouped = False
		self.GroupIDX = 0
		self.Bones = []
		self.refID = node.getAttribute('refID')
		self.designID = node.getAttribute('designID')
		self.materials = list(map(str, node.getAttribute('materials').split(',')))
		
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

class Brick:
	def __init__(self, node):
		self.refID = node.getAttribute('refID')
		self.designID = node.getAttribute('designID')
		self.Parts = []
		for childnode in node.childNodes:
			if childnode.nodeName == 'Part':
				self.Parts.append(Part(node=childnode))

class SceneCamera:
	def __init__(self, node):
		self.refID = node.getAttribute('refID')
		(a, b, c, d, e, f, g, h, i, x, y, z) = map(float, node.getAttribute('transformation').split(','))
		self.matrix = Matrix3D(n11=a,n12=b,n13=c,n14=0,n21=d,n22=e,n23=f,n24=0,n31=g,n32=h,n33=i,n34=0,n41=x,n42=y,n43=z,n44=1)
		self.fieldOfView = float(node.getAttribute('fieldOfView'))
		self.distance = float(node.getAttribute('distance'))

class Scene:
	def __init__(self, file):
		self.Bricks = []
		self.Scenecamera = []
		self.Groups = []

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

class GeometryReader:
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
			return int(struct.unpack_from('i', self.data, _offset)[0])
		else:
			return int.from_bytes(self.data[_offset:_offset + 4], byteorder='little')

	def readInt(self):
		if sys.version_info < (3, 0):
			ret = int(struct.unpack_from('i', self.data, self.offset)[0])
		else:
			ret = int.from_bytes(self.data[self.offset:self.offset + 4], byteorder='little')
		self.offset += 4
		return ret

	def readFloat(self):
		ret = float(struct.unpack_from('f', self.data, self.offset)[0])
		self.offset += 4
		return ret

class Geometry:
	def __init__(self, designID, database):
		self.designID = designID
		self.Parts = {}
		GeometryLocation = '{0}{1}{2}'.format(GEOMETRIEPATH, designID,'.g')
		GeometryCount = 0
		while str(GeometryLocation) in database.filelist:
			self.Parts[GeometryCount] = GeometryReader(data=database.filelist[GeometryLocation].read())
			GeometryCount += 1
			GeometryLocation = '{0}{1}{2}{3}'.format(GEOMETRIEPATH, designID,'.g',GeometryCount)

		primitive = Primitive(data = database.filelist[PRIMITIVEPATH + designID + '.xml'].read())
		self.Partname = primitive.Designname
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

class Bone2:
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

class Primitive:
	def __init__(self,data):
		self.Designname = ''
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
						self.Designname = childnode.getAttribute('designname')

class LOCReader:
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

class Materials:
	def __init__(self, data):
		self.Materials = {}
		xml = minidom.parseString(data)
		for node in xml.firstChild.childNodes: 
			if node.nodeName == 'Material':
				self.Materials[node.getAttribute('MatID')] = Material(node.getAttribute('MatID'),r=int(node.getAttribute('Red')), g=int(node.getAttribute('Green')), b=int(node.getAttribute('Blue')), a=int(node.getAttribute('Alpha')), mtype=str(node.getAttribute('MaterialType')))

	def setLOC(self, loc):
		for key in loc.values:
			if key in self.Materials:
				self.Materials[key].name = loc.values[key].replace(" ", "_")

	def getMaterialbyId(self, mid):
		return self.Materials[mid]

class Material:
	def __init__(self,id, r, g, b, a, mtype):
		self.id = id
		self.name = ''
		self.mattype = mtype
		self.r = float(r)
		self.g = float(g)
		self.b = float(b)
		self.a = float(a)
	def string(self):
		out = 'Kd {0} {1} {2}\nKa 1.600000 1.600000 1.600000\nKs 0.400000 0.400000 0.400000\nNs 3.482202\nTf 1 1 1\n'.format( self.r / 255, self.g / 255,self.b / 255) 
		if self.a < 255:
			out += 'Ni 1.575\n' + 'd {0}'.format(0.05) + '\n' + 'Tr {0}\n'.format(0.05)
		return out

class DBinfo:
	def __init__(self, data):
		xml = minidom.parseString(data)
		self.Version = xml.getElementsByTagName('Bricks')[0].attributes['version'].value
		print('DB Version: ' + str(self.Version))

class LIFFile:
	def __init__(self, name, offset, size, handle):
		self.handle = handle
		self.name = name
		self.offset = offset
		self.size = size

	def read(self):
		self.handle.seek(self.offset, 0)
		return self.handle.read(self.size)

class LIFReader:
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
			return int(struct.unpack('>i', self.filehandle.read(4))[0])
		else:
			return int.from_bytes(self.filehandle.read(4), byteorder='big')

	def readShort(self, offset=0):
		self.filehandle.seek(offset, 0)
		if sys.version_info < (3, 0):
			return int(struct.unpack('>h', self.filehandle.read(2))[0])
		else:
			return int.from_bytes(self.filehandle.read(2), byteorder='big')

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

		start_time = time.time()

		out = open(filename + ".obj", "w+")
		out.write("mtllib " + filename + ".mtl" + '\n\n')
		outtext = open(filename + ".mtl", "w+")
		
		total = len(self.scene.Bricks)
		current = 0

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

				out.write("o\n")

				for part in geo.Parts:
					geo.Parts[part].outpositions = [elem.copy() for elem in geo.Parts[part].positions]
					geo.Parts[part].outnormals = [elem.copy() for elem in geo.Parts[part].normals]

					for i, b in enumerate(pa.Bones):
						# positions
						for j, p in enumerate(geo.Parts[part].outpositions):
							if (geo.Parts[part].bonemap[j] == i):
								p.transform( invert * b.matrix)
						# normals
						for k, n in enumerate(geo.Parts[part].outnormals):
							if (geo.Parts[part].bonemap[k] == i):
								n.transformW( invert * b.matrix)

					for point in geo.Parts[part].outpositions:
						out.write(point.string("v")) 

					for normal in geo.Parts[part].outnormals:
						out.write(normal.string("vn"))

					for text in geo.Parts[part].textures:
						out.write(text.string("vt")) 

				decoCount = 0
				out.write("g " + "(" + geo.designID + ") " + geo.Partname + '\n')
				for part in geo.Parts:

					lddmat = self.allMaterials.getMaterialbyId(pa.materials[part])
					matname = lddmat.name

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
						outtext.write("newmtl " + matname + '\n')
						outtext.write(lddmat.string())
						if not deco == '0':
							outtext.write("map_Kd " + deco + ".png" + '\n')

					out.write("usemtl " + matname + '\n') 
					for face in geo.Parts[part].faces:
						if len(geo.Parts[part].textures) > 0:
							out.write(face.string("f",indexOffset,textOffset))  
						else:
							out.write(face.string("f",indexOffset)) 

					indexOffset += len(geo.Parts[part].outpositions)
					textOffset += len(geo.Parts[part].textures) 
				# -----------------------------------------------------------------
				out.write('\n')

		sys.stdout.write('%s\r' % ('                                                                                                 '))
		print("--- %s seconds ---" % (time.time() - start_time))


def FindDatabase():
	if os.name =='posix':
		return str(os.path.join(str(os.getenv('USERPROFILE') or os.getenv('HOME')),'Library','Application Support','LEGO Company','LEGO Digital Designer','db.lif'))
	else:
		return str(os.path.join(str(os.getenv('USERPROFILE') or os.getenv('HOME')),'AppData','Roaming','LEGO Company','LEGO Digital Designer','db.lif'))
	
def progress(count, total, status='', suffix = ''):
	bar_len = 40
	filled_len = int(round(bar_len * count / float(total)))
	percents = round(100.0 * count / float(total), 1)
	bar = '#' * filled_len + '-' * (bar_len - filled_len)
	sys.stdout.write('Progress: [%s] %s%s %s %s\r' % (bar, percents, '%', suffix, '                                                 '))
	sys.stdout.write('Progress: [%s] %s%s %s %s\r' % (bar, percents, '%', suffix, status))
	sys.stdout.flush()

def main():
	print("- - - pyldd2obj - - -")
	print("          _ ")
	print("         [_]")
	print("       /|   |\\")
	print("      ()'---' C")
	print("        | | |")
	print("        [=|=]")
	print("")
	print("- - - - - - - - - - - -")
	try:
	   lxf_filename = sys.argv[1]
	   obj_filename = sys.argv[2]
	except Exception as e:
	   print("Missing Paramenter:" + sys.argv[0] + " infile.lfx exportname (without extension)")
	   return

	converter = Converter()
	if os.path.exists(FindDatabase()):
		converter.LoadDatabase(databaselocation = FindDatabase())
		converter.LoadScene(filename=lxf_filename)
		converter.Export(filename=obj_filename)
	else:
		print("no LDD database found please install LEGO-Digital-Designer")

if __name__ == "__main__":
	main()
