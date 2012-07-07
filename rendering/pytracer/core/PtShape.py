import PtCommon
import PtPlugin

class PtShape(PtPlugin.PtPlugin):
    def __init__(self,name=None):
        PtPlugin.PtPlugin.__init__(self)
        #tmpName = name if name else PtCommon.getRandomName("BaseCam")
        self.name = self.__class__.__name__ 
        self.type = PtCommon.TDC_PLUGIN_SHAPE
        ## Add Params
        self.addParamPoint("center",[0,0,0])
        self.addParamMatrix("matrix",mat)

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

