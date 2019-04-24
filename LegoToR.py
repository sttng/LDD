import ParseCommandLine as cl
import sys,os.path,subprocess

cwd = os.getcwd()

# Main rendering routine
def main(filename, srate=10, pixelvar=0.1, width=1024, height=720, searcharchive=cwd, searchtexture=cwd, integrator='PxrPathTracer', integratorParams={}):
	print ('shading rate {} pivel variance {} using {} {}'.format(shadingrate,pixelvar,integrator,integratorParams))

if __name__ == '__main__':
	cl.ProcessCommandLine('myscene.rib')
	main(cl.filename, cl.args.srate, cl.args.pixelvar, cl.args.width, cl.args.height, cl.args.searcharchive, cl.args.searchtexture, cl.integrator, cl.integratorParams)
