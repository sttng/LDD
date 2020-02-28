# Custom2DField data specification
## XML element description
The **height** and **width** attributes are always double the number of studs.
The contained text is a 2D array that is always **height**+1 and **width**+1.

This is done to keep information between and around the studs.
So for a 2x2 brick, the height and width attributes would be equal to 4.
This gives a 5x5 2D array that would look like this: 

| X | X | X | X | X |
:---:|:---:|:---:|:---:|:---:
**X** | **O** |   | **O** | **X**
**X** |   |   |   | **X**
**X** | **O** |   | **O** | **X**
**X** | **X** | **X** | **X** | **X**

The **type** attribute can be 22 or 23. 22 is used for female connections and 23 for male connections.

## Possible values
Conn. type  | Gender | Description
------------|:------:|:----------------------------------
**TYPE 0**  |  Male  | Stud connection
  0:4       |        |
  0:4:1     |        |
  0:4:2     |        |
  0:4:17    |        | Used only for parts 4237 'CHEST OF DRAWERS', 30150 'BOX 3X4' and 61780 'BOX  2x2x2'
  0:4:32    |        |
  0:4:33    |        |
  0:4:34    |        |
  0:4:40    |        | Used only for parts 10058 'ANIMAL NO.8 ARM', 3820 'MINI HAND' and 64783 'ROCK MONSTER, MINI, ARM'
——————— | —————— |———————————————————————————————————
**TYPE 1**  |  Male  | 
  1:4       |        |
  1:4:1     |        |
  1:4:2     |        |
  1:4:4     |        |
  1:4:5     |        |
  1:4:6     |        |
  1:4:16    |        |
  1:4:32    |        |
  1:4:33    |        |
  1:4:34    |        |
  1:4:36    |        |
  1:4:37    |        |
  1:4:38    |        |
  1:4:41    |        |
——————— | —————— |———————————————————————————————————
**TYPE 2**  |  Male  | Stud connection (idk the difference with type 0)
  2:4:1     |        |
  2:4:32    |        |
  2:4:33    |        |
  2:4:34    |        |
——————— | —————— |———————————————————————————————————
**TYPE 3**  |  Male  | Stud with hole that connects with lego bar
  3:4:1     |        |
  3:4:4     |        |
  3:4:5     |        |
  3:4:32    |        |
  3:4:33    |        |
  3:4:34    |        |
  3:4:36    |        |
  3:4:37    |        |
  3:4:38    |        |
——————— | —————— |———————————————————————————————————
**TYPE 4**  |  Male  | Door stud
 4:4:32     |        | Used only for part 76041 'DOOR FOR FRAME 1X4X6'
 4:4:33     |        | Used only for part 47899 'LEFT SHOP DOOR 4X5'
——————— | —————— |———————————————————————————————————
**TYPE 5**  | Female | Circular connector that surrounds a stud
  5:4:32    |        | 
  5:4:33    |        | Used primarily for minifig related bricks
  5:4:34    |        |
  5:4:96    |        | 
  5:4:98    |        | Used only for part 32828 'PLATE 1X1 ROUND W/ HORIZONTAL 3.2 SHAFT'
——————— | —————— |———————————————————————————————————
**TYPE 7**  | Female | Bottom tube (cylinder between 4 studs)
  7:4       |        |
  7:4:1     |        |
  7:4:2     |        | 
  7:4:64    |        |
——————— | —————— |———————————————————————————————————
**TYPE 8**  | Female |
  8:4       |        |
  8:4:1     |        |
  8:4:2     |        |
——————— | —————— |———————————————————————————————————
**TYPE 9**  | Female |
  9:4       |        |
  9:4:1     |        | Bottom peg/cylinder (the size of a lego bar)
  9:4:2     |        |
  9:4:32    |        |
  9:4:33    |        |
  9:4:34    |        |
——————— | —————— |———————————————————————————————————
**TYPE 10** | Female |
 10:4:1     |        |
——————— | —————— |———————————————————————————————————
**TYPE 11** | Female |
 11:4:1     |        |
 11:4:32    |        |
——————— | —————— |———————————————————————————————————
**TYPE 12** | Female |
 12:4:1     |        |
——————— | —————— |———————————————————————————————————
**TYPE 13** | Female |
 13:4:32    |        |
 13:4:33    |        |
——————— | —————— |———————————————————————————————————
**TYPE 14** | Female |
 14:4:32    |        |
 14:4:33    |        |
——————— | —————— |———————————————————————————————————
**TYPE 15** | Female | Stud connection
 15:4       |        | 
 15:4:1     |        | 
 15:4:2     |        | 
 15:4:32    |        | 
 15:4:33    |        | 
 15:4:34    |        | 
 15:4:64    |        | 
 15:4:96    |        | Used for holes where a stud fit but is not primarily made for that (e.g. a tool wrench or a towball hook's)
——————— | —————— |———————————————————————————————————
**TYPE 16** | Female |
 16:4:64    |        | 
 16:4:96    |        | Used only for part 88517 'MOTORCYCLE RIM Ø 75'
——————— | —————— |———————————————————————————————————
**TYPE 17** | Female |
 17:4:1     |        | Used for 1x1 square bricks and plate (parts 3005, 20310 and 3024)
——————— | —————— |———————————————————————————————————
**TYPE 18** |  Male  | Space between 4 studs
 18:1       |        | Used only for part 2429 'HINGE PLATE 1X2 II'
 18:1:1     |        | On the corner of a brick (1 stud on the brick, the others would be on a brick beside)
 18:1:2     |        | Used only for part 2430 'HINGE PLATE 1X2 I'
 18:2:1     |        | On the edge of a brick (2 studs on the brick, the others would be on a brick beside)
 18:3:1     |        |
 18:4       |        | In the center of a brick (all 4 studs on the brick)
 18:4:1     |        | 
 18:4:2     |        | Used only for part 47507 'BRICK 6X6X2 W. Ø4,85'
 18:4:4     |        | Used only for part 11295 'BOTTOM 6X8 W. DOUBLE BOW INVERTED'
——————— | —————— |———————————————————————————————————
**TYPE 19** |  Male  |
 19:4:33    |        |
——————— | —————— |———————————————————————————————————
**TYPE 21** | Female |
 21:4:32    |        | Used only for parts 6026 'CROCODILE and 75174 'DRAGON'
——————— | —————— |———————————————————————————————————
**TYPE 22** | Female | Brick walls
 22:1:1     |        | Corners
 22:2:1     |        | Edges/Perimeter
 22:3:1     |        | Intersection
——————— | —————— |———————————————————————————————————
**TYPE 23** |        | Space between two side-by-side studs
 23:4       | Female | Used only for part 87580 'PLATE 2X2 W 1 KNOB'
 23:4:1     | Female | Used only "inside" the brick, otherwise type 22:2:1 (wall) is used
 23:4:1     |  Male  | 
 ——————— | —————— |———————————————————————————————————
**TYPE 24** | Female |
 24:4:1     |        | Used only for parts 3660 'ROOF TILE 2X2/45 INV.' and 3747 'ROOF TILE 2X3/25° INV.'
——————— | —————— |———————————————————————————————————
**TYPE 25** |  Male  |
 25:4:1     |        | Used for power function connectors (parts 58124, 59510 and 64228)
——————— | —————— |———————————————————————————————————
**TYPE 26** |  Male  |
 26:4:1     |        | Used for power function connectors (parts 58124, 59510 and 64228)
——————— | —————— |———————————————————————————————————
**TYPE 27** | Female |
 27:4:1     |        | Used only for part 58124 'FUNC. PLUG TOP'
——————— | —————— |———————————————————————————————————
**TYPE 28** | Female |
 28:4:1     |        | Used only for part 58124 'FUNC. PLUG TOP'
——————— | —————— |———————————————————————————————————
**TYPE 29** |        | No connections
 29:0       |  Both  |
 29:0:1     |  Both  |
 29:0:4     |  Male  | Used only for part 11295 'BOTTOM 6X8 W. DOUBLE BOW INVERTED'
