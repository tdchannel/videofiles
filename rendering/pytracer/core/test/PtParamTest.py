import os
import unittest

from .core import PtParam 
from .core import PtGeom

class PtParamTest(unittest.TestCase):


    def test_basePtParam(self):
        # test for none init
        param = PtParam.PtParamBase()
        self.assertEqual(param.value,None)
        # test SetValue
        val = 10
        param.setValue(val)
        self.assertEqual(param.value,val)
        # test for value init
        param = PtParam.PtParamBase(value=val)
        self.assertEqual(param.value,val)
        
    def test_intPtParam(self):
        # test for none init
        param = PtParam.PtParamInt()
        self.assertEqual(param.value,None)
        # test SetValue
        val = 10
        param.setValue(val)
        self.assertEqual(param.value,val)
        # test for value init
        param = PtParam.PtParamInt(value=val)
        self.assertEqual(param.value,val)

    def test_floatPtParam(self):
        # test for none init
        param = PtParam.PtParamFloat()
        self.assertEqual(param.value,None)
        # test SetValue
        val = 10.0
        param.setValue(val)
        self.assertEqual(param.value,val)
        # test for value init
        param = PtParam.PtParamFloat(value=val)
        self.assertEqual(param.value,val)

    def test_pointPtParam(self):
        # test for none init
        param = PtParam.PtParamPoint()
        self.assertEqual(param.value,None)
        # test SetValue
        val = PtGeom.PtPoint()
        param.setValue(val)
        self.assertEqual(param.value,val)
        # test for value init
        param = PtParam.PtParamPoint(value=val)
        self.assertEqual(param.value,val)
        # test for list value init
        val = [1,2,3]
        param = PtParam.PtParamPoint(value=val)
        self.assertEqual(param.value.x,val[0])
        self.assertEqual(param.value.y,val[1])
        self.assertEqual(param.value.z,val[2])

    def test_vectorPtParam(self):
        # test for none init
        param = PtParam.PtParamVector()
        self.assertEqual(param.value,None)
        # test SetValue
        val = PtGeom.PtVector()
        param.setValue(val)
        self.assertEqual(param.value,val)
        # test for value init
        param = PtParam.PtParamVector(value=val)
        self.assertEqual(param.value,val)
        # test for list value init
        val = [1,2,3]
        param = PtParam.PtParamVector(value=val)
        self.assertEqual(param.value.x,val[0])
        self.assertEqual(param.value.y,val[1])
        self.assertEqual(param.value.z,val[2])



if __name__ == '__main__':
    print "Testing %s"%os.path.basename(__file__)[:-7]
    unittest.main()
