import os
import unittest

from pytracer.core import PtTransform 
from pytracer.core import PtGeom


class PtTransformTest(unittest.TestCase):

    def test_PtMatrix(self):
        # test for no param init
        m = [1.,0.,0.,0.,
             0.,1.,0.,0.,
             0.,0.,1.,0.,
             0.,0.,0.,1.]
        mat = PtTransform.PtMatrix()
        self.assertEqual(m,mat.m)

        # test for list init
        m2 = [1.1,0.,0.,0.,
             0.,1.2,0.,0.,
             0.,0.,1.3,0.,
             0.,0.,0.,1.]
        # test for no param init
        mat = PtTransform.PtMatrix(m2)
        self.assertEqual(m2,mat.m)
        # test determinant
        self.assertEqual(mat.determinant,1.7160000000000002)
        # test identity
        mat.identity
        self.assertEqual(m,mat.m)

        #test Transpose
        m3 = [1.,0.,0.,2.,
              0.,1.,0.,3.,
              0.,0.,1.,4.,
              0.,0.,0.,1.]
        m3i = [1.,0.,0.,-2.,
              0.,1.,0.,-3.,
              0.,0.,1.,-4.,
              0.,0.,0.,1.]
        m3t = [1.,0.,0.,0.,
               0.,1.,0.,0.,
               0.,0.,1.,0.,
               2.,3.,4.,1.]
        mat = PtTransform.PtMatrix(m3)
        mat.transpose
        self.assertEqual(mat.m,m3t)
        mat.transpose
        # test invert
        mat.invert
        self.assertEqual(mat.m,m3i)

    #def test_PtTransform(self):
    #    m = [1.,0.,0.,0.,
    #         0.,1.,0.,0.,
    #         0.,0.,1.,0.,
    #         0.,0.,0.,1.]
    #    trans = [1.,0.,0.,2.,
    #              0.,1.,0.,3.,
    #              0.,0.,1.,4.,
    #              0.,0.,0.,1.]
    #    #test empty init
    #    t = PtTransform.PtTransform()
    #    self.assertEqual(t.m.m,m)
    #    #test arg init
    #    t = PtTransform.PtTransform(PtTransform.PtMatrix(trans))
    #    self.assertEqual(t.m.m,trans)
    
    def test_PiTranslate(self):
        m = [1.,0.,0.,0.,
             0.,1.,0.,0.,
             0.,0.,1.,0.,
             0.,0.,0.,1.]
        trans = [1.,0.,0.,2.,
                  0.,1.,0.,3.,
                  0.,0.,1.,4.,
                  0.,0.,0.,1.]
        #test empty
        t = PtTransform.PiTranslate()
        self.assertEqual(t.m,m)
        #test list init
        t = PtTransform.PiTranslate([2.,3.,4.])
        self.assertEqual(t.m,trans)
        #test Vector init
        t = PtTransform.PiTranslate(PtGeom.PtVector(2.,3.,4.))
        self.assertEqual(t.m,trans)
        
        
    def test_PiScale(self):
        m = [1.,0.,0.,0.,
             0.,1.,0.,0.,
             0.,0.,1.,0.,
             0.,0.,0.,1.]
        trans = [2.,0.,0.,0.,
                 0.,3.,0.,0.,
                 0.,0.,4.,0.,
                 0.,0.,0.,1.]

        #test empty
        t = PtTransform.PiScale()
        self.assertEqual(t.m,m)
        #test list init
        t = PtTransform.PiScale([2.,3.,4.])
        self.assertEqual(t.m,trans)
        #test Vector init
        t = PtTransform.PiScale(PtGeom.PtVector(2.,3.,4.))
        self.assertEqual(t.m,trans)

    def test_PiRotateX(self):
        m = [1.0, 0.0, 0.0, 0.0, 
             0.0, 0.70710678118654757, -0.70710678118654746, 0.0, 
             0.0, 0.70710678118654746, 0.70710678118654757, 0.0, 
             0.0, 0.0, 0.0, 1.0]

        r = PtTransform.PiRotateX(45)
        self.assertEqual(r.m,m)

    def test_PiRotateY(self):
        m =[0.70710678118654757, 0.0, 0.70710678118654746, 0.0, 
            0.0, 1.0, 0, 0.0, 
            -0.70710678118654746, 0.0, 0.70710678118654757, 0.0, 
            0.0, 0.0, 0.0, 1.0] 
        

        r = PtTransform.PiRotateY(45)
        self.assertEqual(r.m,m)

    def test_PiRotateZ(self):
        m = [0.70710678118654757, -0.70710678118654746, 0.0, 0.0, 
             0.70710678118654746, 0.70710678118654757, 0.0, 0.0,
             0.0, 0.0, 1.0, 0.0,
             0.0, 0.0, 0.0, 1.0]
        
        r = PtTransform.PiRotateZ(45)
        self.assertEqual(r.m,m)


if __name__ == '__main__':
    print "Testing %s"%os.path.basename(__file__)[:-7]
    unittest.main()
