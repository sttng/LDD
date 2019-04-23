#!/usr/bin/env python

#
# Version 0.1 - Copyright (c) 2019 by 
# Scans lxf file, writes ribs of bricks, places them in scene.rib
#
# Updates:
#
# License: MIT License
#

import argparse

filename = 'scene.rib'
integratorParams = {"int numLightSamples" : [1], "int numBxdfSamples" : [1], "int maxPathLength" : [4]}
integrator = 'Integrator "PxrPathTracer" "PxrPathTracer1"'
args = []

def ParseCommandLine(_filename) :
	global filename
	global integratorParams
	global integrator
	global args
	parser = argparse.ArgumentParser(description = 'Modify LegoToR render parameters')
	
	parser.add_argument('-s', '--srate', nargs = '?', 
		const = 10.0, default = 10.0, type = float,
		help = 'modify shading rate. Default 10')
	
	parser.add_argument('-p', '--pixelvar', nargs = '?', 
		const = 0.1, default = 0.1, type = float,
		help = 'modify the pixel variance. Default 0.1')
	
	parser.add_argument('-wd', '--width', nargs = '?', 
		const = 1024, default = 1024, type = int,
		help = 'width of image. Default 1024')
	
	parser.add_argument('-ht', '--height', nargs = '?', 
		const = 720, default = 720, type = int,
		help = 'height of image. Default 720')
		
	parser.add_argument('-d', '--default', action = 'count', help = 'use PxrPathTracer')
	parser.add_argument('-v', '--vcm', action = 'count', help = 'use PxrVCM')
	parser.add_argument('-i', '--unified', action = 'count', help = 'use PxrUnified. Also needs to be enabled in rendermn.ini to work')
	parser.add_argument('-o', '--occlusion', action = 'count', help = 'use Occlusion')
	
	parser.add_argument('-t', '--direct', action = 'count', help = 'use PxrDirect')
	parser.add_argument('-w', '--wire', action = 'count', help = 'use PxrVisualizer with wireframe shaded')
	parser.add_argument('-n', '--normals', action = 'count', help = 'use PxrVisualizer with wireframe and Normals')
	parser.add_argument('-u', '--st', action = 'count', help = 'use PxrVisualizer with wireframe and ST')
	
	args = parser.parse_args()
	if args.rib:
		filename = _filename 
		
	else:
		filename = '__render'
		
	if args.default:
		integrator = 'Integrator "PxrPathTracer" "PxrPathTracer1"'
	if args.vcm:
		integrator = 'Integrator "PxrVCM" "PxrVCM1"'
	if args.unified:
		integrator = 'Integrator "PxrUnified" "PxrUnified1"' # Must be enabled in rendermn.ini also
	if args.occlusion:
		integrator = '''Integrator "PxrOcclusion" "PxrOcclusion1"
			"int numSamples" [4]\n
			"int distribution" [1]\n
			"float cosineSpread" [2.0]\n
			"float falloff" [0.01]\n
			"float maxDistance" [100.0]\n
			"int useAlbedo" [0]'''
	if args.direct:
		integrator = 'Integrator "PxrDirectLighting" "PxrDirectLighting1"'
	if args.wire:
		integrator = '''Integrator "PxrVisualizer" "PxrVisualizer1"
			"string style" ["shaded"]
			"int wireframe" [1]
			"int normalCheck" [0]
			"string matCap" [""]
			"color wireframeColor" [0.0 0.0 0.0]
			"float wireframeOpacity" [0.5]
			"float wireframeWidth" [1.0]'''
	if args.normals:
		integrator = '''Integrator "PxrVisualizer" "PxrVisualizer1"
			"string style" ["normals"]
			"int wireframe" [1]
			"int normalCheck" [0]
			"string matCap" [""]
			"color wireframeColor" [0.0 0.0 0.0]
			"float wireframeOpacity" [0.5]
			"float wireframeWidth" [1.0]'''
	if args.st:
		integrator = '''Integrator "PxrVisualizer" "PxrVisualizer1"
			"string style" ["st"]
			"int wireframe" [1]
			"int normalCheck" [0]
			"string matCap" [""]
			"color wireframeColor" [0.0 0.0 0.0]
			"float wireframeOpacity" [0.5]
			"float wireframeWidth" [1.0]'''
