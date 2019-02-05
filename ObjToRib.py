#!/usr/bin/env python

#
# Version 0.1 - Copyright (c) 2019 by 
#
# Info:
# Obj To Rib Script
# This script will read in .obj files, construct
# geometry from them and write out a rib file
# for each of them.
#
# Updates:
#
# License: MIT License
#

from subprocess import call
from os import listdir
from os.path import isfile, join, splitext

## FILE INFO
#fileLoc = "C:\\Maya_Tests\\scenes\\test\\"
templatePath = "C:\\Desktop\\_CLASS\\2_Shading_I\\FINAL\\scripts\\"
#templatePath = "C:\\FINAL_Backup\\scripts\\"
objPath = templatePath + "objFiles\\"
ribFilePath = templatePath + "ribFiles\\"


## GET OBJ FILE LIST

fileNames = [ f for f in listdir(objPath) if isfile(join(objPath,f)) and ".obj" in f]


## READ TEMPLATE FILE
##  -- to allow for easy adjustment to the files later
t = open(templatePath + "template.rib")
temp = t.readlines()
template = []
for line in temp:
    if "\n" in line:
        line = line.split("\n")[0]
    template.append(line)
    
for fileName in fileNames:
    ## READ AND STORE OBJ FILE
    f1 = open(objPath + fileName)
    lines = f1.readlines()
    f1lines = []
    for line in lines:
        if "\n" in line:
            line = line.split("\n")[0]
        f1lines.append(line)
    f1.close()
    
    
    ## CREATE AND SETUP RIB FILE USING TEMPLATE
    name = splitext(fileName)[0]
    f2 = open(ribFilePath + name + ".rib", "w")
    lineNum = 0
    for line in template:
        lineNum += 1
        if ("RENAME" in line):
            n = splitext(fileName)[0]
            f2.write("\t\"" + n + ".jpg\"\n")
        else:
            f2.write(line + "\n")
            if "WorldBegin" in line:
                break
    
    
    ## CONVERT F1LINES TO USABLE FORMAT
    verts = []
    faces = []
    for line in f1lines:
        if "v " in line and "." in line:
            l = ["%.3f" % float(num) for num in line.split(" ") if 'v' not in num]
            verts.append(l)
        if "f " in line and "/" in line:
            l = []
            for nums in line.split(" "):
                if 'f' not in nums:
                    l.append(int(nums.split("/")[0]))
            faces.append(l)
    
    ## CREATE POLYGONS
    f2.write("\nAttributeBegin")
    f2.write("\nSurface \"matte\"")
    f2.write("\nColor [ 1 1 1 ]")
    for face in faces:
        f2.write("\n\tPolygon")
        newline = ''
        for i in xrange(0, len(face), 1):
            for j in xrange(0, len(verts[face[i]-1]), 1):
                newline += str(verts[face[i]-1][j]) + ' '
        f2.write("\n\t\t\"P\" [ " + newline + "]")
    f2.write("\nAttributeEnd")
    
    
    ## FINISH AND CLOSE FILE
    for i in range(lineNum, len(template)):
        f2.write(template[i] + "\n")
    f2.close()
