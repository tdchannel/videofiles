#!/usr/bin/env python

from pytracer import *

PtBegin()

options = PtWorld.getOptions()
#print PtWorld
#print "XX"
cam = PtNode("ortho_camera")

sph = PtNode("sphere")
#sph.center.setValue([10,1,2])
sph.intersectP(PtRay())
options.xres.setValue(200)
options.yres.setValue(200)
#options.bucketSize.setValue(10)
PtWorld.driver = PtNode("display_driver")
PtRender()

PtEnd()
