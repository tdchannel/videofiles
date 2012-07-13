#!/usr/bin/env python

from pytracer import *

PtBegin(2)

options = PtWorld.getOptions()

options.verbose.setValue(2)
options.xres.setValue(640)
options.yres.setValue(480)
#options.bucketSize.setValue(10)

cam = PtNode("ortho_camera")

sph = PtNode("sphere")
sph.radius.setValue(100)
sph.center.setValue([10,10,10])

PtWorld.driver = PtNode("display_driver")
PtRender()

PtEnd()
