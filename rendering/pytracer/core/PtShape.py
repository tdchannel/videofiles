import PtCommon
import PtPlugin
import PtTransform
import pytracer.core.PtWorld as PtWorld

class PtShape(PtPlugin.PtPlugin):
    def __init__(self,name=None):
        PtPlugin.PtPlugin.__init__(self)
        #tmpName = name if name else PtCommon.getRandomName("BaseCam")
        self.name = self.__class__.__name__ 
        self.type = PtCommon.TDC_PLUGIN_SHAPE
        ## Add Params
        self.addParamPoint("center",[0,0,0])
        mat = PtTransform.PtMatrix()
        self.addParamMatrix("matrix",mat)
        self.prepared = False
        self.methods = {"createRay":self.createRay,
                        "canIntersect":self.canIntersect,
                        "intersectP":self.intersectP}

    
    def createRay(self):
        pass

    def canIntersect(self):
        return True

    def prepare(self):
        pass

    def objectBound(self):
        pass

    def intersect(self, ray,thit):
        pass

    def intersectP(self,ray):
        pass
