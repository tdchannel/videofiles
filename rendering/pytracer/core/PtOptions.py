import PtCommon
import PtPlugin

class PtOptions(PtPlugin.PtPlugin):
    def __init__(self,name=None):
        PtPlugin.PtPlugin.__init__(self)
        #tmpName = name if name else PtCommon.getRandomName("BaseCam")
        self.name = self.__class__.__name__ 
        self.type = PtCommon.TDC_PLUGIN_CAMERA
        ## Add Params
        self.addParamInt("xres",640)
        self.addParamInt("yres",480)
        self.addParamInt("bucketSize",32)
        self.addParamInt("verbose",0)
        self.addParamString("outputFile","image")

