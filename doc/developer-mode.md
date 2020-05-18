You have to add DeveloperMode=1 after language=en in Preferences.ini

```
language=en
DeveloperMode=1
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






