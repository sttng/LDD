# LDD related scripts
## LifToObj 
LifToObj.py uses LIFExtractor.py from JrMasterModelBuilder to extract the Lego Digital Designer LIF library first and then converts the LDD .g geometry files to Alias|Wavefrom .obj files.

## ObjToRib
ObjToRib.py will read in a Alias|Wavefrom .obj file, construct geometry from it and write out a Renderman .rib file of it.

## LxfRoRib
LxfRoRib.py will read in a Lego Digital Designer .lxf scene file and construct a Renderman .rib file of the scene by using ObjToRib to concert the bricks of the scenes and use the relevant scene information to place the bricks accordingly (rotation, translation).

## prman commands
```terminal
prman -d it -t:-2 ribfile.rib

oslc Primvar.osl
```

## Useful links

* https://sdm.scad.edu/faculty/mkesson/vsfx502/wip/best/spring11/miho_tomimasu/rib_archives/index.html
* RIB Entity files section: https://renderman.pixar.com/resources/RenderMan_20/ribBinding.html
* https://rmanwiki.pixar.com/display/REN/PxrSurface.mobile.phone
* http://cg.earlyworm.co.nz/renderman-commandline/
* https://renderman.pixar.com/forum/showthread.php?s=&threadid=35595&s=3f67579b2c1d88a74b98ea5f86a3c546
* https://www.rockraidersunited.com/topic/3764-lego-digital-designer-lif-extractor/?do=findComment&comment=133146
* http://stefanmuller.com/exploring-lego-material-part-1/
* http://stefanmuller.com/exploring-lego-material-part-2/
* https://github.com/chipgw/LibLDD
* https://sdm.scad.edu/faculty/mkesson/vsfx502/wip/best/fall11/kevin_george/rib_teapot/index.html
* http://julius-ihle.de/?p=547
