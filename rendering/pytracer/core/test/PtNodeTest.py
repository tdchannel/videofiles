import os
import unittest

from .core.PtNode import PtNode 
from .core import PtParam 

class PtNodeTest(unittest.TestCase):

    def test_addPtParam1(self):
        val = 5.0
        param = PtParam.PtParamFloat(value=val)
        node = PtNode()
        node.addParam(param)
        self.assertEqual(node.numParams,1)

    def test_addPtParam2(self):
        node = PtNode()
        #try to add an int 
        node.addParamInt("intPtParam",value=5)
        self.assertEqual(node.numParams,1)
        #try to add a float 
        node.addParamFloat("floatPtParam",value=5.0)
        self.assertEqual(node.numParams,2)
        
    def test_paramValue(self):
        paramName = "testPtParam"
        node = PtNode(name="testNode")
        node.addParamInt(paramName)
        val = 2345
        # test set PtParam
        node.setParamValue(paramName,val)
        # test get PtParam
        paramVal = node.paramValue(paramName)
        self.assertEqual(paramVal,val)

if __name__ == '__main__':
    print "Testing %s"%os.path.basename(__file__)[:-7]
    unittest.main()
