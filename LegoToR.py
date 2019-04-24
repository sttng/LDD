#!/usr/bin/env python

#
# Version 0.1 - Copyright (c) 2019 by 
# LegoToR parses LXF files and command line parameters to create a renderman compliant rib file.
#
# Updates:
#
# License: MIT License
#


import ParseCommandLine as cl
import sys,os.path,subprocess

cwd = os.getcwd()

# Main rendering routine
def main(filename, srate=10, pixelvar=0.1, width=1280, height=720, searcharchive=cwd, searchtexture=cwd, integrator='PxrPathTracer', integratorParams={}):
	print ('shading rate {} pivel variance {} using {} {}'.format(shadingrate,pixelvar,integrator,integratorParams))
	template_rib = '''##RenderMan RIB
version 3.04
Option "searchpath" "string archive" ["''' + searcharchive + '''"]
Option "searchpath" "string texture" [".:@:/Applications/Pixar/RenderManProServer-22.4/lib/RenderManAssetLibrary/EnvironmentMaps/Outdoor/GriffithObservatory.rma:''' + searchtexture + '''/"]
Option "Ri" "int Frame" [1]
	"float PixelVariance" [''' + pixelvar +''']
	"string PixelFilterName" ["gaussian"]
	"float[2] PixelFilterWidth" [2 2]
	"int[2] FormatResolution" [''' + width + ''' ''' + height + ''']
	"float FormatPixelAspectRatio" [1]
	"float[2] Clipping" [0.1 10000]
	"float[4] ScreenWindow" [-1 1 -0.5625 0.5625]
	"float[2] Shutter" [0 0]
Option "bucket" "string order" ["circle"]
Option "statistics" "int level" [1] "string xmlfilename" ["''' + cwd + '''/''' + filename + '''.xml"]

''' + integrator + '''
Hider "raytrace" "int minsamples" [32] "int maxsamples" [64] "float darkfalloff" [0.025] "int incremental" [1] "string pixelfiltermode" ["importance"]
ShadingRate ''' + srate + '''
Projection "PxrCamera" "float fov" [8.5] "float fStop" [3.5] "float focalLength" [0.8] "float focalDistance" [5] "point focus1" [0.0 0.0 -1] "point focus2" [1 0.0 -1] "point focus3" [1 1 -1]
'''

	
if __name__ == '__main__':
	cl.ParseCommandLine('myscene.rib')
	main(cl.filename, cl.args.srate, cl.args.pixelvar, cl.args.width, cl.args.height, cl.args.searcharchive, cl.args.searchtexture, cl.integrator, cl.integratorParams)
