from pickle import FALSE, TRUE
import laspy
import numpy as np
from class1 import Octree
class Data(object):
        def __init__(self, name, position):
            self.name = name
            self.position = position
        def __str__(self):
            return u"name: {0} position: {1}".format(self.name, self.position)
las = laspy.read("2743_1234.las")
WORLD_SIZE =  las.header.maxs[0]
ORIGIN = (0, 0, 0)
depth = (
        (8),
        ( 8)
    )
a = Octree(
            WORLD_SIZE,
            ORIGIN,
            max_type=depth[0],
            max_value=depth[1]
        )
x =las.header.point_count
y=0;
z=TRUE
lasData = []
while z:
    n=[las.x[y],las.y[y],las.z[y]]
    the_name = "Node__" + str(x)
    the_pos = (
            n[0] ,
            n[1] ,
            n[2] 
        )
    lasData.append(Data(the_name, the_pos))
    y=y+1
    if y>=x:
        break  
for testObject in lasData:
   a.insertNode(testObject.position, testObject)
  