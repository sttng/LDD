# Lego Digital Designer related scripts
The Python scripts have been tested to work on Python on macOS 10.14 Mojave, Renderman 22.3 and 22.4.

## LifToObj 
LifToObj.py uses LIFExtractor.py from JrMasterModelBuilder (https://github.com/JrMasterModelBuilder/LIF-Extractor) to extract the Lego Digital Designer LIF library first and then converts the LDD .g geometry files to Alias|Waveform .obj files.

## ObjToRib2
ObjToRib2.py will read in a Alias|Waveform .obj file, construct geometry from it and write out a Renderman .rib file of it.
It is an improved version of ObjToRib with support for groups.

## LxfRoRib
LxfRoRib.py will read in a Lego Digital Designer .lxf scene file and construct a Renderman .rib file of the scene by using BrickReader.py and ObjToRib2.py to convert the bricks of the scenes (from .g to .obj and finally to .rib) and use the relevant scene information to place the bricks accordingly (rotation, translation).

## prman commands
```terminal
export RMANTREE=/Applications/Pixar/RenderManProServer-22.4/

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

* Virtually all plastic used by LEGO is a proprietary version of Lanxess’ Novodur acrylonitrile butadiene styrene (ABS), Makrolon polycarbonate (for transparent elements) and Macrolex dyes for coloring.   Delrin or nylon variants are used to make cloth and string elements. http://www.craftechind.com/which-plastic-material-is-used-in-lego-sets/
* Tyres and elastic materials are made from a slightly different polymer to ABS, styrene butadiene styrene (SBS). https://www.compoundchem.com/2018/04/09/lego/
* Green leaves, bushes, and trees in their products will be made from polyethene derived from sustainable sugar cane sources. https://www.compoundchem.com/2018/04/09/lego/
* Transparent bricks are made from polycarbonate plastic (PC) rather than ABS. https://bricks.stackexchange.com/questions/155/are-transparent-neon-lego-bricks-made-from-a-different-plastic-than-usual
