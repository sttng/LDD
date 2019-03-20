import argparse

filename = 'default.rib'
integratorParams = {"int numLightSamples" : [1], "int numBxdfSamples" : [1], "int maxPathLength" : [4]}
integrator = 'Integrator "PxrPathTracer" "PxrPathTracer1"'
args = []

def ProcessCommandLine(_filename) :
	global filename
	global integratorParams
	global integrator
	global args
	parser = argparse.ArgumentParser(description = 'Modify render parameters')
	
	parser.add_argument('--shadingrate', '-s', nargs = '?', 
		const = 10.0, default = 10.0, type = float,
		help = 'modify the shading rate default to 10')
	
	parser.add_argument('--pixelvar', '-p', nargs = '?', 
		const = 0.1, default = 0.1, type = float,
		help = 'modify the pixel variance default  0.1')
	
	parser.add_argument('--fov', '-f', nargs = '?', 
		const = 48.0, default = 48.0, type = float,
		help = 'projection fov default 48.0')
	
	parser.add_argument('--width', '-wd', nargs = '?', 
		const = 1024, default = 1024, type = int,
		help = 'width of image default 1024')
	
	parser.add_argument('--height', '-ht', nargs = '?', 
		const = 720, default = 720, type = int,
		help = 'height of image default 720')
		
	parser.add_argument('--default', '-d', action = 'count', help = 'use PxrPathTracer')
	parser.add_argument('--vcm', '-v', action = 'count', help = 'use PxrVCM')
	parser.add_argument('--unified', '-i', action = 'count', help = 'use PxrUnified. But these also needs to be enabled in rendermn.ini')
	parser.add_argument('--occlusion', '-o', action = 'count', help = 'use Occlusion')
	
	parser.add_argument('--direct', '-t', action = 'count', help = 'use PxrDirect')
	parser.add_argument('--wire', '-w', action = 'count', help = 'use PxrVisualizer with wireframe shaded')
	parser.add_argument('--normals', '-n', action = 'count', help = 'use PxrVisualizer with wireframe and Normals')
	parser.add_argument('--st', '-u', action = 'count', help = 'use PxrVisualizer with wireframe and ST')
	
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
		integrator = ('Integrator "PxrOcclusion" "PxrOcclusion1"
			"int numSamples" [4]\n
			"int distribution" [1]\n
			"float cosineSpread" [2.0]\n
			"float falloff" [0.01]\n
			"float maxDistance" [100.0]\n
			"int useAlbedo" [0]')
	if args.direct:
		integrator = 'Integrator "PxrDirectLighting" "PxrDirectLighting1"'
	if args.wire:
		integrator = ('Integrator "PxrVisualizer" "PxrVisualizer1"
			"string style" ["shaded"]
			"int wireframe" [1]
			"int normalCheck" [0]
			"string matCap" [""]
			"color wireframeColor" [0.0 0.0 0.0]
			"float wireframeOpacity" [0.5]
			"float wireframeWidth" [1.0]')
	if args.normals:
		integrator = ('Integrator "PxrVisualizer" "PxrVisualizer1"
			"string style" ["normals"]
			"int wireframe" [1]
			"int normalCheck" [0]
			"string matCap" [""]
			"color wireframeColor" [0.0 0.0 0.0]
			"float wireframeOpacity" [0.5]
			"float wireframeWidth" [1.0]')
	if args.st:
		integrator = ('Integrator "PxrVisualizer" "PxrVisualizer1"
			"string style" ["st"]
			"int wireframe" [1]
			"int normalCheck" [0]
			"string matCap" [""]
			"color wireframeColor" [0.0 0.0 0.0]
			"float wireframeOpacity" [0.5]
			"float wireframeWidth" [1.0]')
