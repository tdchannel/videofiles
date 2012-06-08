import PtCommon
import PtParam 


class PtPluginError(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class PtPlugin():
    def __init__(self):
        self.name = None
        self.type = None
        self.returnType = None
        self.params = {}
        self.methods= {}

    ########## Methods ##########
    def addParam(self,param,value=None,parmType=None):
        if isinstance(param,PtParam.PtParamBase):
            self.params[param.name]=param
        else:
            if parmType == PtCommon.TDC_TYPE_INT:
                tmpParam = PtParam.PtParamInt(name=param,value=value)
            elif parmType == PtCommon.TDC_TYPE_FLOAT:
                tmpParam = PtParam.PtParamFloat(name=param,value=value)
            elif parmType == PtCommon.TDC_TYPE_POINT:
                tmpParam = PtParam.PtParamPoint(name=param,value=value)
            elif parmType == PtCommon.TDC_TYPE_VECTOR:
                tmpParam = PtParam.PtParamVector(name=param,value=value)
            elif parmType == PtCommon.TDC_TYPE_STRING:
                tmpParam = PtParam.PtParamString(name=param,value=value)
            else:
                tmpParam = PtParam.PtParamBase(name=param,value=value)
            self.params[param]=tmpParam

    def addParamInt(self,param,value=None):
        self.addParam(param,value=value,parmType=PtCommon.TDC_TYPE_INT)

    def addParamFloat(self,param,value=None):
        self.addParam(param,value=value,parmType=PtCommon.TDC_TYPE_FLOAT)

    def addParamPoint(self,param,value=None):
        self.addParam(param,value=value,parmType=PtCommon.TDC_TYPE_POINT)

    def addParamVector(self,param,value=None):
        self.addParam(param,value=value,parmType=PtCommon.TDC_TYPE_VECTOR)
    
    def addParamString(self,param,value=None):
        self.addParam(param,value=value,parmType=PtCommon.TDC_TYPE_STRING)
