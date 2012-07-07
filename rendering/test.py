#!/usr/bin/env python

from pytracer import *

PtBegin()

cam = PtNode("ortho_camera")
options = PtWorld.getOptions()
#options.xres.setValue(1280)
#options.yres.setValue(720)
#options.bucketSize.setValue(64)
PtWorld.driver = PtNode("display_driver")
PtRender()
