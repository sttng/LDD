# 1 Introduction
This document gives a conceptual overview of the LEGO eXchange Format Markup Language (LXFML). The details of the format are described in the schema file “lxfmlschema.xsd”.

# 2 Concepts

## 2.1 Models
The term model refers to a LEGO model build from LEGO bricks. The geometry of the bricks and the complete model they compose are not part of the model description. Models are stored in LXFML.

## 2.2 Parts
The term part refers to a LEGO construction-element abstraction. A part could describe any physical or virtual object ever created by the LEGO Company, but for several reasons we restrict the term part to the physical or logical form of those objects, which are part of the current, former, or future selection in, what we today call, the Duplo, Dacta, System, and Technic ranges. The shape of any part has a unique identifier as does the material of the part.

## 2.3 SubMaterial
SubMaterials are used when a single Part is comprised of more than one material e.g. a door frame with a transparent window. A SubMaterial defines which surface on the Part needs which material. If no SubMaterial is defined for a given surface, the main material is used.

## 2.4 Decoration
A Decoration is a picture that is drawn on a single Part. A Decoration defines which surface on the Part has which picture.

## 2.5 Assemblies
An Assembly is used when a brick is made up of more than one Part e.g. mini figs. In LXFML all Parts belonging to an Assembly have an assemblyID that defines which type of assembly they are part of and an assemblyRefID which is a uniqueness identifier for this instance of the Assembly.

## 2.6 Meta
The LXFML format supports a variety of non-model description information. Users may save their own information in a Meta element. A Meta element consists of two distinct types of information, of which none, one, or both types may make up the element:

1. A plain text string
2. A list of key-value pairs

LEGO has predefined some Meta elements in the schema file, which can be used by users or applications as long as they adhere to the syntax defined in the schema. Users are encouraged to prefix their Meta element names to avoid future clashes with LEGO defined names.

## 2.7 RefID
Several objects in an LXFML file may be used by other objects, in order to describe such a link, or reference, all objects that can be referenced have a unique refID value that can be used to point to the object. All refID’s for a given type must be unique across the entire file regardless of scope.

## 2.8 Placement
A Placement is used to place objects in the world. It is described by an axis angle rotation and a translation. Objects can be placed relative to other objects, in such a case the world placement is calculated by concatenating the placements.

## 2.9 Camera
A Camera is used to describe points of view; as such a Camera has a position in the world and a view direction. A Camera also has information about field of view.

## 2.10 Model
In LXFML a Model is intended to be a connected structure that is equivalent to a model that you can hold in your hand. It is however not a requirement that a Model is interconnected, or for that matter that a single interconnected structure is contained in a single Model element. It is only meant as a good hint; in the future we may be less lax in this.

## 2.11 Group
A Group contain a list of Parts; it defines a local coordinate system for these Parts. A Model element is made up of one or more Group elements. All Groups are placed in the world coordinate system.

## 2.12 Joints
A connection between two Group elements inside the same Model element is described by a Joint element. This jointed structure is not limited to describe a hierarchy but may also form a looping graph.
Joints are described by a position and two perpendicular axes. Currently two types of joints are defined: the ball joint and the hinge joint, the following is the description of what the axes mean for these joints.

•	Ball joint
o	The ‘a’ axis is the primary axis, protruding out and away from the foundation of the joint 
o	The ‘z’ axis is the secondary axis
o	The third axis can be calculated by crossing the ‘a’ and ‘z’ axes
o	The axes are only interesting when rotational constraints are used
•	Hinge joint
o	The ‘a’ axis describe the rotation axis
o	The ‘z’ axis describes a zero axis from where rotational constraints can be calculated

It is possible to convert this jointed structure into a hierarchical structure by doing the following described by pseudo code, be aware that loops in the structure are broken:

```
List handledGroups
Function BuildHierarchyHelper(current Group)
	If(current Group not handled)
		Mark current Group as handled
For(all joints to/from current Group)
			Make dest Group child of current
			BuildHierarchyHelper(dest Group)
			
Function BuildHierarchy()
Clear handledGroups
For(all groups)
		BuildHierarchyHelper(current)
```

## 2.13 Building instructions
LXFML allow for the description of building instructions. Building instructions are made up of a sequence of steps.

### 2.13.1 Step
A step in a building instruction introduces a Part into the BI world. In the future when explosions are introduced Steps may refer to the same Part several times, once every time a Part is exploded.

Steps may contain other steps. The motivation behind is to emulate the vignettes known from paper building instructions. An example of steps in steps is shown in the following BI:

```
Step A
	Part p1
Step B
	Step C
		Part p2
		Part p3
	Part p4
Step D
	Part p5
```

When viewing this BI as a time line the following Parts are to be shown:

```
  Time 1        Time 2        Time 3        Time 4
  p1            p2,p3         p1,p2,p3,p4   p1,p2,p3,p4,p5
```

### 2.13.2 Explosion
In order to allow models to be built some Parts may need to be moved from their final Placement during the building process. The term Explosion thus refers to a change of Placement for a Part in Step.

# 3 LXFML Element Diagram
Below is a diagram showing the different elements in LXFML and their relationships. The arrows indicate which elements can have which elements as children / parents. The arrow describes a parent to child relationship.
