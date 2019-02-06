# LDD related Python scripts
## LifToObj 
LifToObj.py uses LIFExtractor.py from JrMasterModelBuilder to extract the Lego Digital Designer LIF library first and then converts the LDD .g geometry files to Alias|Wavefrom .obj files.

## ObjToRib
ObjToRib.py will read in Alias|Wavefrom .obj files, construct geometry from them and write out a Renderman .rib file for each of them.

## prman command
prman -d it -t:-2 ribfile.rib

oslc Primvar.osl

