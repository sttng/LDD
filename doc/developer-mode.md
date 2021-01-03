You have to add DeveloperMode=1 after language=en in Preferences.ini located in /Users/USER NAME/Library/Application\ Support/LEGO\ Company/LEGO\ Digital\ Designer/ (macOS).

```
language=en
DeveloperMode=1
```
Other flags:

```
ShowExtendedBrickToolTip=1
```

## Shortcuts

### Caps lock off 
* 1 yellow shapes
* 2 violet shapes 
* 3 cyan shapes 
* Q remove all but holes 
* R Random color coding pieces 
* T post processing options
  * SSAO : Screen Space Ambient Occlusion.
  * SSDO : Screen Space Directional Occlusion.
  * None
  * Scene normals
* O makes everything glow white 
* P Black outlines G Hide all 
* H color coding connected pieces 
* I returns view to origin 
* K hides studs 
* C Shows green crosses on parts 
* V Shows collision elements 
* M hides everthing but decals 

### Shift or Caps lock 
* 1 yellow shapes 
* 2 violet shapes
* 3 cyan shapes 
* Q remove all but holes 
* W wireframe
* R centers views 
* A opens preferences and communication 
* S shows statistics 
* G hides grid 
* ALT GR + I shows all the bricks in 

## Ctrl

* Ctrl+T or menu "Developer / Create model of all bricks":  Opens an exploded model with all the parts of the library.
* Ctrl + Alt + T or AltGr + T or the "Developer / Create model of filtered bricks" menu: Opens an exploded model with all the filtered parts (see chapter Selection filters).

## Developer Menu
* Create model of all bricks: Create a model of all parts of the library.
* Create model of filtered bricks: Creates a model of all current filtered parts.
* Save current Palettes: Saves the current palettes.
* Toggle Physics Test: Turn off brick collision test mode.
* Select alternative LDD web server: Select another LDD server:
 * DKAPER: (no longer available - unknown)
 * 3rd party: -> initialiseDesignerURL=http://ldd.3rd.corp.lego.com/service/integration.asmx/initialiseDesigner
 * LEGO.com: -> initialiseDesignerURL=http://ldd.lego.com/service/integration.asmx/initialiseDesigner
 * Web Dev: -> initialiseDesignerURL=http://ldd.dev.corp.lego.com/service/integration.asmx/initialiseDesigner
 * Web QA: -> initialiseDesignerURL=http://ldd.webqa.lego.com/service/integration.asmx/initialiseDesigner
* Lua console: Opens a Lua console window.

## LUA console features
Details here: https://www.rockraidersunited.com/topic/7912-ldd-lua-console/

Dump the keys of a table: 
```
dumptable = function(foo) local stuff="" for key in pairs(foo) do stuff=stuff .. key .. "\n" end error(stuff) end
```
Dump the keys of global variable 'LDD':
```
dumptable(LDD)
```


## Others

Regarding the preference.ini file, there is one in the Program Files folder and one in the AppData folder. Some flags works in both but some are specific to one or the other.

An usefull one was "DoServerCall" (setted in the Program Files ini). 
By setting it to "0" (false), it prevents LDD from making calls to the Lego servers.
It "was" because it seems like the servers are no longer online.
You could used this flag because whenever one extracted a palette (e.g. LDD base palette) it would delete that folder and redownload the LIF when you started LDD. But recently it no longer will redownload the LIFs.

There is a "Verbose" flag, when set to "1" (true) it creates a log file (%AppData%\LEGO Company\DCLTrace.txt)
It does not provide a lot of usefull information, but can pinpoint why some bricks won't load.
This flag can be in both files it seems (but have to check), because in some documentation it says in Program File but currently it seems it's in the AppData one.

Regarding brick loading, by looking at the logs, there is a bunch of bricks that are not found in the default LDD palette.
Turns out most of them actually exist, but in the palette the part alias is used. Replacing it with the correct part ID solve the issue.
So it looks like the Alias property of the primitive XML is an unfinished feature, wich seems to be planned to use later.

There is a flag nammed "LoadAssemblies" that can be set to "0" (false) and the assemblies will not be loaded and the contained parts will appear in the palette. This flag must be set in the Program File ini.

This flag revealed that any part that is contained in an assembly won't be loaded in the palette, even if you add it in the LDD palette file.
But ther is a hack... You can create a new assembly with only one part. So for exemple you may create an assemblies for the shock absorber parts so you can adjust them properly.

Finally there are two flags which are unknown: "QAMode" (AppData) and "LoadMostRecentModel" (Program Files).
