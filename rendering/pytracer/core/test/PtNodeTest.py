import os
import unittest

from pytracer.core.PtNode import PtNode 
from pytracer.core import PtParam 

class PtNodeTest(unittest.TestCase):

    def test_addPtParam1(self):
        pass
        #val = 5.0
        #param = PtParam.PtParamFloat(value=val)
        #node = PtNode("ortho_camera")
        #node.addParam(param)
        #self.assertEqual(node.numParams,1)

    def test_addPtParam2(self):
        pass
        #node = PtNode("ortho_camera")
        ##try to add an int 
        #node.addParamInt("intPtParam",value=5)
        #self.assertEqual(node.numParams,1)
        ##try to add a float 
        #node.addParamFloat("floatPtParam",value=5.0)
        #self.assertEqual(node.numParams,2)
        
    def test_paramValue(self):
        pass
        #paramName = "testPtParam"
        #node = PtNode("ortho_camera",name="testNode")
        #node.addParamInt(paramName)
        #val = 2345
        ## test set PtParam
        #node.setParamValue(paramName,val)
        ## test get PtParam
        #paramVal = node.paramValue(paramName)
        #self.assertEqual(paramVal,val)

if __name__ == '__main__':
    print "Testing %s"%os.path.basename(__file__)[:-7]
    unittest.main()
