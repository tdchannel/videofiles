import PtCommon
import PtPlugin
import PtTransform
import pytracer.core.PtWorld as PtWorld

class PtCamera(PtPlugin.PtPlugin):
    def __init__(self,name=None):
        PtPlugin.PtPlugin.__init__(self)
        #tmpName = name if name else PtCommon.getRandomName("BaseCam")
        self.name = self.__class__.__name__ 
        self.type = PtCommon.TDC_PLUGIN_CAMERA
        ## Add Params
        self.addParamPoint("center",[0,0,0])
        self.addParamMatrix("matrix",PtTransform.PtMatrix())
        self.addParamVector("lookAt",[0,0,1])
        self.addParamFloat("near",1e-07)
        self.addParamFloat("far",1e9)
        self.methods = {"createRay":self.createRay}

    def createRay(self):
        pass

