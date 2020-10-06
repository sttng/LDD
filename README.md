# Lego Digital Designer related scripts
The Python scripts have been tested to work on Python 2.7.10 on macOS 10.14 Mojave, Renderman 22.3, 22.4, 22.5, 22.6, 23.0, 23.1, 23.2, 23.3, 23.4.

## pylddlib
pylddlib.py is an 'improved' version of pyldd2obj.py. It adds support for LDD modifications (i.e. read the db folder instead of db.lif) and has a couple of other small fixes.

## pyldd2obj
pyldd2obj.py developed by jonnysp (https://github.com/jonnysp) will read in a Lego Digital Designer .lxf scene file and construct a corresponding Alias|Waveform .obj and .mtl scene from it.

## LifToObj (deprecated)
**deprecated - it is suggested to use pyldd2obj/pylddlib instead** LifToObj.py uses LIFExtractor.py from JrMasterModelBuilder (https://github.com/JrMasterModelBuilder/LIF-Extractor) to extract the Lego Digital Designer LIF library first and then converts the LDD .g geometry files to Alias|Waveform .obj files.

## LxfToRib (deprecated)
**deprecated - it is suggested to use LegoToR instead** LxfToRib.py will read in a Lego Digital Designer .lxf scene file and construct a Renderman .rib file of the scene by using BrickReader.py and ObjToRib2.py to convert the bricks of the scenes (from .g to .obj and finally to .rib) and use the relevant scene information to place the bricks accordingly (rotation, translation).

## ObjToRib2
ObjToRib2.py will read in a Alias|Waveform .obj file, construct geometry from it and write out a Renderman .rib file of it.
It is an improved version of ObjToRib with support for groups.

## prman commands
```terminal
export RMANTREE=/Applications/Pixar/RenderManProServer-23.4/
export PATH="$PATH:$RMANTREE/bin"

prman -d it -t:-2 ribfile.rib

oslc Primvar.osl
```

## USD commands
```terminal
export PYTHONPATH=$PYTHONPATH:USD_INSTALL_ROOT/lib/python
```

### Checkpointing

```terminal
prman -checkpoint 2m,20m foo.rib
```

This tells prman to save a checkpoint file at every two minutes and stop rendering at 20 minutes. If you want to resume a render:

```terminal
prman -recover 1 foo.rib
```

More info in the docs:

https://rmanwiki.pixar.com/display/REN22/Checkpointing+and+Recovery


## Useful links

* https://rmanwiki.pixar.com/display/REN22/PxrSurface
* http://cg.earlyworm.co.nz/renderman-commandline/
* https://renderman.pixar.com/forum/showthread.php?s=&threadid=35595&s=3f67579b2c1d88a74b98ea5f86a3c546
* https://www.rockraidersunited.com/topic/3764-lego-digital-designer-lif-extractor/?do=findComment&comment=133146
* http://stefanmuller.com/exploring-lego-material-part-1/
* http://stefanmuller.com/exploring-lego-material-part-2/
* http://stefanmuller.com/exploring-lego-material-part-3/
* https://github.com/chipgw/LibLDD
* https://sdm.scad.edu/faculty/mkesson/vsfx502/wip/best/fall11/kevin_george/rib_teapot/index.html
* http://julius-ihle.de/?p=547
* https://sdm.scad.edu/faculty/mkesson/vsfx755/wip/best/spring2011/zichuan_zhao/lemon/lemon.html
* https://nccastaff.bournemouth.ac.uk/jmacey/Renderman/
* https://www.janwalter.org/jekyll/blender/cloud/attic/2016/07/13/attic.html
* http://www.fundza.com/cutter/whatsnew/index.html
* https://rmanwiki.pixar.com/display/REN22/Denoising
* https://graphics.pixar.com/usd/docs/USD-Frequently-Asked-Questions.html#USDFrequentlyAskedQuestions-WhyIsn'tPythonFindingUSDModules?/
* https://dusankovic.com/store/jVDY/lookdev-kit

## Lego plastic materials

* Virtually all plastic used by LEGO is a proprietary version of Lanxess’ Novodur acrylonitrile butadiene styrene (ABS), Makrolon polycarbonate (PC) is used for transparent elements and Macrolex dyes for coloring. Delrin or nylon variants are used to make cloth and string elements. http://www.craftechind.com/which-plastic-material-is-used-in-lego-sets/
* Tyres and elastic materials are made from a slightly different polymer to ABS, styrene butadiene styrene (SBS). https://www.compoundchem.com/2018/04/09/lego/
* Green leaves, bushes, and trees in their products will be made from polyethene derived from sustainable sugar cane sources. https://www.compoundchem.com/2018/04/09/lego/

## LDD Links

* http://www.jespermosegaard.dk/portfolio/lego-digital-designer/
* https://tcrf.net/LEGO_Digital_Designer
* http://trierlab.com/
* https://drive.google.com/file/d/1qzIoAAUBAcaHVe8gVwXxLl1s0P76o0_D/view?usp=drivesdk

