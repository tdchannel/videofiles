import inspect
import PtCommon
import PtPlugin



class PtDriver(PtPlugin.PtPlugin):
    def __init__(self,name=None):
        PtPlugin.PtPlugin.__init__(self)
        self.name = self.__class__.__name__ 
        self.type = PtCommon.TDC_PLUGIN_DRIVER
        self.options = None
        ## Add Params
        #self.addParamPoint("center",[0,0,0])
        #self.addParamVector("lookAt",[0,0,1])
        #self.addParamFloat("near",1e-07)
        #self.addParamFloat("far",1e9)
        self.methods={
                      "open":self.open,
                      "prepareBucket":self.prepareBucket,
                      "writeBucket":self.writeBucket,
                      "close":self.close
                      }

        
    def open(self,fileName):
        raise PtPlugin.PtPluginError("open not implemented in %s"%self.__class__.__name__)
    def prepareBucket(self):
        raise PtPlugin.PtPluginError("prepareBucekt not implemented in %s"%self.__class__.__name__)
    def writeBucket(self):
        raise PtPlugin.PtPluginError("writeBucket not implemented in %s"%self.__class__.__name__)
    def close(self):
        raise PtPlugin.PtPluginError("close not implemented in %s"%self.__class__.__name__)
