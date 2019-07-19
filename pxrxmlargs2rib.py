#!/usr/bin/env python
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
		self.Name = xml.firstChild.getAttribute("page")
				
		for node in xml.firstChild.childNodes: 
			if node.nodeName == 'param':
				for childnode in node.childNodes:
					print childnode.getAttribute("type")
					print childnode.getAttribute("name")
					print childnode.getAttribute("default")
			elif node.nodeName == 'output':
				for childnode in node.childNodes:
					if childnode.nodeName == 'tag':
						print childnode.getAttribute("color")
					print childnode.getAttribute("name")

		print('args "'+ self.Name)


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