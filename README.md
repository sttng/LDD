# LDD related scripts
## LifToObj 
LifToObj.py uses LIFExtractor.py from JrMasterModelBuilder to extract the Lego Digital Designer LIF library first and then converts the LDD .g geometry files to Alias|Wavefrom .obj files.

## ObjToRib
ObjToRib.py will read in a Alias|Wavefrom .obj file, construct geometry from it and write out a Renderman .rib file of it.

## LxfRoRib
LxfRoRib.py will read in a Lego Digital Designer .lxf scene file and construct a Renderman .rib file of the scene by using BrickReader.py and ObjToRib.py to convert the bricks of the scenes (from .g to .obj and finally to .rib) and use the relevant scene information to place the bricks accordingly (rotation, translation).

## prman commands
```terminal
prman -d it -t:-2 ribfile.rib

oslc Primvar.osl
```

## Useful links

* https://rmanwiki.pixar.com/display/REN/PxrSurface.mobile.phone
* http://cg.earlyworm.co.nz/renderman-commandline/
* https://renderman.pixar.com/forum/showthread.php?s=&threadid=35595&s=3f67579b2c1d88a74b98ea5f86a3c546
* https://www.rockraidersunited.com/topic/3764-lego-digital-designer-lif-extractor/?do=findComment&comment=133146
* http://stefanmuller.com/exploring-lego-material-part-1/
* http://stefanmuller.com/exploring-lego-material-part-2/
* https://github.com/chipgw/LibLDD
* https://sdm.scad.edu/faculty/mkesson/vsfx502/wip/best/fall11/kevin_george/rib_teapot/index.html
* http://julius-ihle.de/?p=547
* https://sdm.scad.edu/faculty/mkesson/vsfx755/wip/best/spring2011/zichuan_zhao/lemon/lemon.html
* https://nccastaff.bournemouth.ac.uk/jmacey/Renderman/

## Lego plastic materials

* Virtually all plastic used by LEGO is a proprietary version of Lanxess’ Novodur ABS, Makrolon polycarbonate (for transparent elements) and Macrolex dyes for coloring.   Delrin or nylon variants are used to make cloth and string elements. http://www.craftechind.com/which-plastic-material-is-used-in-lego-sets/
* Tyres are made from a slightly different polymer to ABS, styrene butadiene styrene (SBS). https://www.compoundchem.com/2018/04/09/lego/
