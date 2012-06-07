import PtCommon
import PtNode

class PtCamera(PtNode.PtNode):
    def __init__(self,name=None):
        tmpName = name if name else PtCommon.getRandomName("BaseCam")
        PtNode.PtNode.__init__(self,name=tmpName)
        
        self.nodeType = PtCommon.TDC_PLUGIN_CAMERA
        ## Add Params
        self.addParamPoint("center",[0,0,0])
        self.addParamVector("lookAt",[0,0,1])
        self.addParamFloat("near",1e-07)
        self.addParamFloat("far",1e9)

    def createRay(self):
        pass

