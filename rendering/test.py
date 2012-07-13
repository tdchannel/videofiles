#!/usr/bin/env python

from pytracer import *

PtBegin(2)

options = PtWorld.getOptions()

options.verbose.setValue(2)
options.xres.setValue(200)
options.yres.setValue(200)
#options.bucketSize.setValue(10)

cam = PtNode("ortho_camera")

sph = PtNode("sphere")
sph.radius.setValue(50)
#sph.center.setValue([20,20,10])

PtWorld.driver = PtNode("display_driver")
PtRender()

PtEnd()
