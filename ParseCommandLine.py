#!/usr/bin/env python

#
# Version 0.1 - Copyright (c) 2019 by 
#
# Updates:
#
# License: MIT License
#

import argparse
import os.path
import posixpath

filename = 'scene.rib'
#integratorParams = {"int maxPathLength" [10], "int maxContinuationLength" [-1], "int maxNonStochasticOpacityEvents" [0], "string sampleMode" ["bxdf"], "int numLightSamples" [1], "int numBxdfSamples" [1], "int numIndirectSamples" [1], "int numDiffuseSamples" [1], "int numSpecularSamples" [1], "int numSubsurfaceSamples" [1], "int numRefractionSamples" [1], "int allowCaustics" [0], "int accumOpacity" [0], "int rouletteDepth" [4], "float rouletteThreshold" [0.200000003], "int clampDepth" [2], "float clampLuminance" [10]}
integratorParams = {}
integrator = '''Integrator "PxrPathTracer" "PxrPathTracer1"
			"int maxPathLength" [10] 
			"int maxContinuationLength" [-1] 
			"int maxNonStochasticOpacityEvents" [0] 
			"string sampleMode" ["bxdf"] 
			"int numLightSamples" [1] 
			"int numBxdfSamples" [1] 
			"int numIndirectSamples" [1] 
			"int numDiffuseSamples" [1] 
			"int numSpecularSamples" [1] 
			"int numSubsurfaceSamples" [1] 
			"int numRefractionSamples" [1] 
			"int allowCaustics" [0] 
			"int accumOpacity" [0] 
			"int rouletteDepth" [4] 
			"float rouletteThreshold" [0.2] 
			"int clampDepth" [2] 
			"float clampLuminance" [10]'''
args = []
if os.name =='posix':
	cwd = os.getcwd()
else:
	cwd = os.path.normpath(os.getcwd())
	cwd = cwd.split(os.sep)
	cwd = posixpath.join(*cwd)
useplane = True
usenormal = True
uselogoonstuds = True
usecsvcolors = True

def ParseCommandLine(_filename) :
	global filename
	global integratorParams
	global integrator
	global args
	global cwd
	global useplane
	global usenormal
	global uselogoonstuds
	global usecsvcolors
	
	parser = argparse.ArgumentParser(description = 'Modify LegoToR render parameters')
	
	# Required positional argument
	parser.add_argument('infile', type = open,
		help = 'required input LXF file')
	
	parser.add_argument('-s', '--srate', nargs = '?', 
		const = 10.0, default = 10.0, type = float,
		help = 'modify shading rate. Default 10')
	
	parser.add_argument('-p', '--pixelvar', nargs = '?', 
		const = 0.1, default = 0.1, type = float,
		help = 'modify the pixel variance. Default 0.1')
	
	parser.add_argument('-fo', '--fov' ,nargs='?', 
		const = 25.0, default = 25.0, type = float,
		help='projection fov. Default 25.0')
		
	parser.add_argument('-fs', '--fstop' ,nargs='?', 
		const = 9.99999968e+37, default = 9.99999968e+37, type = float,
		help='fStop. Default 9.99999968e+37 (unlimited)')
	
	parser.add_argument('-wd', '--width', nargs = '?', 
		const = 1280, default = 1280, type = int,
		help = 'width of image. Default 1280')
	
	parser.add_argument('-ht', '--height', nargs = '?', 
		const = 720, default = 720, type = int,
		help = 'height of image. Default 720')
		
	parser.add_argument('-sa', '--searcharchive', nargs = '?',
		default = cwd,
		help = 'searchpath archive. Default current working dir')

	parser.add_argument('-st', '--searchtexture', nargs = '?', 
		default = cwd,
		help = 'searchpath texture. Default current working dir')
	
	parser.add_argument('-cam', '--camera', nargs = '?', 
		const = -1, default = -1, type = int,
		help = 'set active camera. Default is -1 for Cam--1 \'Minus 1\'')	
		
	parser.add_argument('-d', '--default', action = 'count', help = 'use PxrPathTracer')
	parser.add_argument('-v', '--vcm', action = 'count', help = 'use PxrVCM')
	parser.add_argument('-u', '--unified', action = 'count', help = 'use PxrUnified. Enable also in rendermn.ini to work!')
	parser.add_argument('-o', '--occlusion', action = 'count', help = 'use Occlusion')
	
	parser.add_argument('-t', '--direct', action = 'count', help = 'use PxrDirect')
	parser.add_argument('-w', '--wire', action = 'count', help = 'use PxrVisualizer with wireframe shaded')
	parser.add_argument('-n', '--normals', action = 'count', help = 'use PxrVisualizer with wireframe and Normals')
	parser.add_argument('-z', '--wst', action = 'count', help = 'use PxrVisualizer with wireframe and ST')
	parser.add_argument('-b', '--bxdf', action = 'count', help = 'use PxrVisualizer with wireframe and bxdf')
	parser.add_argument('-fl', '--flat', action = 'count', help = 'use PxrVisualizer with wireframe flat')
	
	parser.add_argument('-np', '--noplane', action = 'count', help = 'disable ground plane. Useful for space ships!')
	parser.add_argument('-nn', '--nonormals', action = 'count', help = 'disable writing of normals, as some normals in LDD may have problems')
	parser.add_argument('-nl', '--nologo', action = 'count', help = 'disable logo on studs')
	parser.add_argument('-nc', '--nocsv', action = 'count', help = 'disable reading of color values from csv file. Use LDD built-in colors instead')

	
	args = parser.parse_args()
		
	if args.default:
		integrator = '''Integrator "PxrPathTracer" "PxrPathTracer1"
			"int maxPathLength" [10] 
			"int maxContinuationLength" [-1] 
			"int maxNonStochasticOpacityEvents" [0] 
			"string sampleMode" ["bxdf"] 
			"int numLightSamples" [1] 
			"int numBxdfSamples" [1] 
			"int numIndirectSamples" [1] 
			"int numDiffuseSamples" [1] 
			"int numSpecularSamples" [1] 
			"int numSubsurfaceSamples" [1] 
			"int numRefractionSamples" [1] 
			"int allowCaustics" [0] 
			"int accumOpacity" [0] 
			"int rouletteDepth" [4] 
			"float rouletteThreshold" [0.2] 
			"int clampDepth" [2] 
			"float clampLuminance" [10]'''
	if args.vcm:
		integrator = 'Integrator "PxrVCM" "PxrVCM1"'
	if args.unified:
		integrator = 'Integrator "PxrUnified" "PxrUnified1"' # Must be enabled in rendermn.ini to work
	if args.occlusion:
		integrator = '''Integrator "PxrOcclusion" "PxrOcclusion1"
			"int numSamples" [4]
			"int distribution" [1]
			"float cosineSpread" [2.0]
			"float falloff" [0.01]
			"float maxDistance" [100.0]
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
			"float wireframeOpacity" [0.8]
			"float wireframeWidth" [1.2]'''
	if args.normals:
		integrator = '''Integrator "PxrVisualizer" "PxrVisualizer1"
			"string style" ["normals"]
			"int wireframe" [1]
			"int normalCheck" [0]
			"string matCap" [""]
			"color wireframeColor" [0.0 0.0 0.0]
			"float wireframeOpacity" [0.5]
			"float wireframeWidth" [1.0]'''
	if args.wst:
		integrator = '''Integrator "PxrVisualizer" "PxrVisualizer1"
			"string style" ["st"]
			"int wireframe" [1]
			"int normalCheck" [0]
			"string matCap" [""]
			"color wireframeColor" [0.0 0.0 0.0]
			"float wireframeOpacity" [0.5]
			"float wireframeWidth" [1.0]'''
	if args.bxdf:
		integrator = '''Integrator "PxrVisualizer" "PxrVisualizer1"
			"string style" ["bxdf"]
			"int wireframe" [1]
			"int normalCheck" [0]
			"string matCap" [""]
			"color wireframeColor" [0.0 0.0 0.0]
			"float wireframeOpacity" [0.5]
			"float wireframeWidth" [1.0]'''
	if args.flat:
		integrator = '''Integrator "PxrVisualizer" "PxrVisualizer1"
			"string style" ["flat"]
			"int wireframe" [1]
			"int normalCheck" [0]
			"string matCap" [""]
			"color wireframeColor" [0.0 0.0 0.0]
			"float wireframeOpacity" [0.5]
			"float wireframeWidth" [1.0]'''
	if args.noplane:
		useplane = False
	if args.nonormals:
		usenormal = False
	if args.nologo:
		uselogoonstuds = False
	if args.nocsv:
		usecsvcolors = False
