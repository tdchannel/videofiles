from pytracer.core import PtCommon
from pytracer.core import PtCamera
from pytracer.core import PtTransform
from pytracer.core import PtGeom

import pytracer.core.PtWorld as PtWorld

class ortho_camera(PtCamera.PtCamera):
    def __init__(self,name=None):
        PtCamera.PtCamera.__init__(self,name=name)

    def createRay(self,x,y):
        near = self.params['near'].value
        far = self.params['far'].value
        o = self.params['center'].value
        d = self.params['lookAt'].value
        m = self.params['matrix'].value
        xres = PtWorld.options.xres.value
        yres = PtWorld.options.yres.value

        ## create a transform
        #xf = PtTransform.PtTransform(m)
        ## flip the values  (why? IHNFI)
        o.y *=-1; o.z *=-1
        xpoint = PtTransform.PiTranslate(o)
        #xpoint = PtTransform.PtMatrix()
       
        ## multipliy the xform by the position
        m *= xpoint

        px = x - xres / 2. + 0.5
        py = y - yres / 2. + 0.5

        tmp = PtGeom.PtRay(origin=PtGeom.PtPoint(px,py,o.z),
                           direction=PtGeom.PtVector(d.x,d.y,d.z))
        tmp.mint = near
        tmp.maxt = far
        tmp.transform(m)
        return tmp
