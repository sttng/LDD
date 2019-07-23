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
		
		shaderType = xml.getElementsByTagName("shaderType")[0]
		shaderTypeTag = shaderType.getElementsByTagName("tag")[0]
		shaderValue = shaderTypeTag.getAttribute("value").capitalize()
		print('{0} "{1}" "{1}1"').format(shaderValue, self.Name)
		
		params = xml.getElementsByTagName("param")
		for param in params:
			paramType = param.getAttribute("type")
			paramName = param.getAttribute("name")
			paramDefault = "''"
			if param.hasAttribute("default"):
				paramDefault = param.getAttribute("default")
			#paramHelp = param.getElementsByTagName("help")[0].firstChild.nodeValue
			#print('\t#{0}').format(paramHelp)
			print('\t"{0} {1}" [{2}]').format(paramType, paramName, paramDefault)
		
		outputs = xml.getElementsByTagName("output")
		
		if outputs:
			print '\nOutputs:\n'
		for output in outputs:
			outputName = output.getAttribute("name")
			outputTags= output.getElementsByTagName("tag")
			outputTagValue = ''
			for outputTag in outputTags:
				outputTagValue = outputTagValue + outputTag.getAttribute("value") + ' '
			print('\t{0} {1}').format(outputTagValue, outputName)

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
