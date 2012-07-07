import os
import unittest

from .core.PtPlugin import PtPlugin 
from .core import PtParam 

class PtPluginTest(unittest.TestCase):

    def test_addPtParam1(self):
        val = 5.0
        param = PtParam.PtParamFloat(value=val)
        node = PtPlugin()
        node.addParam(param)
        self.assertEqual(node.numParams,1)

    def test_addPtParam2(self):
        node = PtPlugin()
        #try to add an int 
        node.addParamInt("intPtParam",value=5)
        self.assertEqual(node.numParams,1)
        #try to add a float 
        node.addParamFloat("floatPtParam",value=5.0)
        self.assertEqual(node.numParams,2)
        

if __name__ == '__main__':
    print "Testing %s"%os.path.basename(__file__)[:-7]
    unittest.main()
