#!/usr/bin/env python

from pytracer import *

PtBegin(2)

options = PtWorld.getOptions()

options.verbose.setValue(2)
options.xres.setValue(250)
options.yres.setValue(250)
#options.bucketSize.setValue(10)

cam = PtNode("ortho_camera")

sph = PtNode("sphere")
sph.radius.setValue(50)
rot = PiRotateX(90.)
#sph.center.setValue([10,10,1])
#sph.matrix.setValue(rot)
#sph.zmin.setValue(-0.5)
#sph.zmax.setValue(0.5)

PtWorld.driver = PtNode("display_driver")
PtRender()

PtEnd()
