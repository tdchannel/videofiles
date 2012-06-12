#!/usr/bin/env python

from pytracer import *

PtBegin()

cam = PtNode("ortho_camera")
options = PtWorld.getOptions()
#options.xres.setValue(10)
#options.yres.setValue(10)
#options.bucketSize.setValue(5)
PtWorld.driver = PtNode("display_driver")
PtRender()
