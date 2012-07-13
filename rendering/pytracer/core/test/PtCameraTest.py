import os
import unittest

from pytracer.core import PtCamera
from pytracer.core import PtNode
from pytracer.core import PtGeom
from pytracer.core import PtRender

class PtCameraTest(unittest.TestCase):

    def test_instantiate(self):
        PtRender.PtBegin()
        tmp = PtNode.PtNode("ortho_camera")
        # test setting the center
        center = [1.2,10.0,0.22]
        tmp.setParamValue("center",center)
        self.assertEqual(tmp.paramValue("center").x,center[0])
        self.assertEqual(tmp.paramValue("center").y,center[1])
        self.assertEqual(tmp.paramValue("center").z,center[2])



if __name__ == '__main__':
    print "Testing %s"%os.path.basename(__file__)[:-7]
    unittest.main()

