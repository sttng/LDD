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
import sys, os.path


# Template generating routine
def main(infile, srate, pixelvar, width, height, fov, searcharchive, searchtexture, integrator, integratorParams, useplane):
	#print ('shading rate {} pivel variance {} using {} {}'.format(srate,pixelvar,integrator,integratorParams))
	cwd = os.getcwd()
	infile = os.path.splitext(os.path.basename(infile))[0]
	
	template_rib = '''##RenderMan RIB
version 3.04
Option "searchpath" "string archive" ["''' + str(searcharchive) + '''"] "string texture" [".:@:/Applications/Pixar/RenderManProServer-22.4/lib/RenderManAssetLibrary/EnvironmentMaps/Outdoor/GriffithObservatory.rma:''' + str(searchtexture) + '''/"]
Option "Ri" "int Frame" [1]
	"float PixelVariance" [''' + str(pixelvar) + ''']
	"string PixelFilterName" ["gaussian"]
	"float[2] PixelFilterWidth" [2 2]
	"int[2] FormatResolution" [''' + str(width) + ''' ''' + str(height) + ''']
	"float FormatPixelAspectRatio" [1]
	"float[2] Clipping" [0.1 10000]
	"float[4] ScreenWindow" [-1 1 -0.5625 0.5625]
	"float[2] Shutter" [0 0]
Option "bucket" "string order" ["circle"]
Option "statistics" "int level" [1] "string xmlfilename" ["''' + str(cwd) + '''/''' + str(infile) + '''.xml"]

''' + str(integrator) + '''
Hider "raytrace" "int minsamples" [32] "int maxsamples" [64] "float darkfalloff" [0.025] "int incremental" [1] "string pixelfiltermode" ["importance"]
ShadingRate ''' + str(srate) + '''
Projection "PxrCamera" "float fov" [''' + str(fov) + '''] "float fStop" [3.5] "float focalLength" [0.8] "float focalDistance" [5] "point focus1" [0.0 0.0 -1] "point focus2" [1 0.0 -1] "point focus3" [1 1 -1]''' + str(useplane)

	print template_rib
	
if __name__ == '__main__':
	cl.ParseCommandLine('')
	main(cl.args.infile, cl.args.srate, cl.args.pixelvar, cl.args.width, cl.args.height, cl.args.fov, cl.args.searcharchive, cl.args.searchtexture, cl.integrator, cl.integratorParams, cl.useplane)
	
