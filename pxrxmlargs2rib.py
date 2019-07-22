#!/usr/bin/env python
#
# Convert renderman xml .args files to basic rib output files
#
# License: MIT License
#

import os
import sys
from xml.dom import minidom


class Converter:
	def LoadArgsFile(self,filename):
		self.scene = ArgsFile(file=filename)


class ArgsFile:
	def __init__(self, file):

		if file.endswith('.args'):
			with open(file, "rb") as file:
				data = file.read()
		else:
			return

		xml = minidom.parseString(data)
		self.Name = os.path.splitext(os.path.basename(file.name))[0]
		i = 0
		
		#shaderType = xml.getElementsByTagName("shaderType")[0]
		#shaderTypeTag = shaderType.getElementsByTagName("tag")[0]
		#shaderValue = shaderTypeTag.getAttribute("value").capitalize()
		#print('{0} "{1}" "{1}1"').format(shaderValue, self.Name)
		#
		#params = xml.getElementsByTagName("param")
		#for param in params:
		#	paramType = param.getAttribute("type")
		#	paramName = param.getAttribute("name")
		#	paramDefault = param.getAttribute("default")
		#	print('\t"{0} {1}" [{2}]').format(paramType, paramName, paramDefault)
		#
		#outputs = xml.getElementsByTagName("output")
		#print '\nOutputs:\n'
		#for output in outputs:
		#	outputName = output.getAttribute("name")
		#	outputTags= output.getElementsByTagName("tag")
		#	for outputTag in outputTags:
		#		outputTagValue = outputTag.getAttribute("value")
		for node in xml.firstChild.childNodes:
			if node.nodeName == 'shaderType':
				for childnode in node.childNodes:
					if childnode.nodeName == 'tag':
						print('{0} "{1}" "{1}1"').format(childnode.getAttribute("value").capitalize(), self.Name)
			elif node.nodeName == 'page':
				for childnode in node.childNodes:
					if childnode.nodeName == 'param':
						print('\t"{0} {1}" [{2}]').format(childnode.getAttribute("type"), childnode.getAttribute("name"), childnode.getAttribute("default"))
			elif node.nodeName == 'param':
				print('\t"{0} {1}" [{2}]').format(node.getAttribute("type"), node.getAttribute("name"), node.getAttribute("default"))
			elif node.nodeName == 'output':
				if i == 0:
					print '\nOutputs:\n'
				i += 1
				outval = ''
				for childnode in node.childNodes:
					if childnode.nodeName == 'tags':
						for subnode in childnode.childNodes:
							if subnode.nodeName == 'tag':
								outval = outval + subnode.getAttribute("value") + ' '
				print('\t{0} {1}').format(outval, node.getAttribute("name"))


def main():
	try:
		args_filename = sys.argv[1]
	except Exception as e:
		print("Missing Paramenter:" + sys.argv[0] + " PxrInfile.args")
		return

	converter = Converter()
	converter.LoadArgsFile(filename=args_filename)


if __name__ == "__main__":
	main()
