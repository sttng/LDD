```xml
Element = LEGOPrimitive
  Possible Attributes = versionMajor, versionMinor
  Element = Annotations
    Element = Annotation
      Possible Attributes = aliases, designname, maingroupid, maingroupname, platformid, platformname, version, length, holes
  Element = Collision
    Element = Box
      Possible Attributes = sX, sY, sZ, angle, ax, ay, az, tx, ty, tz
    Element = Sphere
      Possible Attributes = radius, angle, ax, ay, az, tx, ty, tz
  Element = Connectivity
    Element = Custom2DField
      Possible Attributes = type, width, height, angle, ax, ay, az, tx, ty, tz
    Element = Hinge
      Possible Attributes = type, oriented, angle, ax, ay, az, tx, ty, tz, LimMin, LimMax, FlipLimMin, FlipLimMax, tag
    Element = Axel
      Possible Attributes = type, length, requireGrabbing, startCapped, endCapped, angle, ax, ay, az, tx, ty, tz, grabbing
    Element = Fixed
      Possible Attributes = type, axes, angle, ax, ay, az, tx, ty, tz, tag
    Element = Gear
      Possible Attributes = type, toothCount, radius, angle, ax, ay, az, tx, ty, tz
    Element = Slider
      Possible Attributes = type, length, startCapped, endCapped, angle, ax, ay, az, tx, ty, tz, cylindrical, spring, tag
    Element = Ball
      Possible Attributes = type, angle, ax, ay, az, tx, ty, tz
    Element = Rail
      Possible Attributes = type, angle, ax, ay, az, tx, ty, tz, length
  Element = PhysicsAttributes
    Possible Attributes = inertiaTensor, centerOfMass, mass, frictionType
  Element = Bounding
    Element = AABB
      Possible Attributes = minX, minY, minZ, maxX, maxY, maxZ
  Element = GeometryBounding
    Element = AABB
      Possible Attributes = minX, minY, minZ, maxX, maxY, maxZ
  Element = Decoration
    Possible Attributes = faces, subMaterialRedirectLookupTable
  Element = Flex
    Element = Bone
      Possible Attributes = boneId, angle, ax, ay, az, tx, ty, tz, flexCheckConnection
      Element = Collision
        Element = Box
          Possible Attributes = sX, sY, sZ, angle, ax, ay, az, tx, ty, tz
      Element = Connectivity
        Element = Axel
          Possible Attributes = type, length, requireGrabbing, startCapped, endCapped, angle, ax, ay, az, tx, ty, tz, grabbing
        Element = Custom2DField
          Possible Attributes = type, width, height, angle, ax, ay, az, tx, ty, tz
        Element = Ball
          Possible Attributes = type, angle, ax, ay, az, tx, ty, tz, flexAttributes
        Element = Fixed
          Possible Attributes = type, angle, ax, ay, az, tx, ty, tz
      Element = PhysicsAttributes
        Possible Attributes = inertiaTensor, centerOfMass, mass, frictionType
      Element = Bounding
        Element = AABB
          Possible Attributes = minX, minY, minZ, maxX, maxY, maxZ
  Element = DefaultOrientation
    Possible Attributes = angle, ax, ay, az, tx, ty, tz
  Element = DefaultCamera
    Possible Attributes = lat, lon
  Element = Paths
    Element = Path
      Possible Attributes = type, points
```

## Decoration
It seems this is only used to synchronize the color of multi surfaces part.
Let's say we have XXXX.g, XXXX.g1 and XXXX.g2. If the subMaterialRedirectLookupTable is "0,1,0", then when applying the paint bucket on the main surface (mesh from the XXXX.g file) the third surface (XXXX.g2) will have the same color applied.
I think it's main purpose is to prevent changing a surface color when you only want to allow decals.
That is why you often see "0,0".
