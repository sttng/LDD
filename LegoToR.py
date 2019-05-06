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
import sys, os.path, datetime
from _version import __version__
import LxfToRib


# rib "header" generating routine
def generate_rib_header(infile, srate, pixelvar, width, height, fov, searcharchive, searchtexture, integrator, integratorParams, useplane):
	#print ('shading rate {} pivel variance {} using {} {}'.format(srate,pixelvar,integrator,integratorParams))
	cwd = os.getcwd()
	infile = os.path.realpath(infile.name)
	infile = os.path.splitext(os.path.basename(infile))[0]
	
	rib_header = '''##RenderMan RIB
# Generated with LegoToR ''' + __version__ + ''' on ''' + str(datetime.datetime.now()) + '''
version 3.04
Option "searchpath" "string archive" ["''' + str(searcharchive) + os.sep + '''"] "string texture" [".:@:/Applications/Pixar/RenderManProServer-22.4/lib/RenderManAssetLibrary/EnvironmentMaps/Outdoor/GriffithObservatory.rma:''' + str(searchtexture) + os.sep + '''"]
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
Option "statistics" "int level" [1] "string xmlfilename" ["''' + str(cwd) + os.sep + str(infile) + '''.xml"]

''' + str(integrator) + '''
Hider "raytrace" "int minsamples" [32] "int maxsamples" [64] "float darkfalloff" [0.025] "int incremental" [1] "string pixelfiltermode" ["importance"]
ShadingRate ''' + str(srate) + '''

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

Projection "PxrCamera" "float fov" [''' + str(fov) + '''] "float fStop" [3.5] "float focalLength" [0.8] "float focalDistance" [5] "point focus1" [0.0 0.0 -1] "point focus2" [1 0.0 -1] "point focus3" [1 1 -1]'''

	#print rib_header
	with open('rib_header.rib', 'w') as file_writer:
		file_writer.write(rib_header)
	file_writer.close()
	return True


def main():
	cl.ParseCommandLine('')
	lxf_filename = os.path.realpath(cl.args.infile.name)
	generate_rib_header(cl.args.infile, cl.args.srate, cl.args.pixelvar, cl.args.width, cl.args.height, cl.args.fov, cl.args.searcharchive, cl.args.searchtexture, cl.integrator, cl.integratorParams, cl.useplane)
	
	# Clean up before writing
	if os.path.exists("Material_Archive.zip"):
		os.remove("Material_Archive.zip")
	
	LxfToRib.generate_bricks(lxf_filename)
	LxfToRib.export_to_rib(lxf_filename, cl.useplane)
	LxfToRib.generate_master_scene(lxf_filename)
	
	lxf_filename = os.path.splitext(os.path.basename(lxf_filename))[0]

	print '''
Now start Renderman with (for preview):
./prman -d it -t:-2 ''' + str(cl.args.searcharchive) + os.sep + lxf_filename + '''_Scene.rib'''
	print '''Or start Renderman with (for final mode without preview):
./prman -t:-2 ''' + str(cl.args.searcharchive) + os.sep + lxf_filename + '''_Scene.rib'''
	print '''
Finally denoise the final output with:
./denoise ''' + str(cl.args.searcharchive) + os.sep + lxf_filename + '''.beauty.001.exr'''


if __name__ == '__main__':
	main()
