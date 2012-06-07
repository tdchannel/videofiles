import sys

import PtCommon
import PtParam 

class PtNode():
    def __init__(self,name=None):
        self.name       = name if name else PtCommon.getRandomName("Node")
        self.nodeType   = None
        self.params     = {} 

    #
    # Private
    #

    #
    # Public
    #

    ######### Properties ########
    @property
    def numParams(self):
        return len(self.params.keys())

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

    def paramValue(self,paramName):
        param = self.params[paramName]
        return param.value

    def setParamValue(self,paramName,paramValue):
        param = self.params[paramName]
        param.setValue(paramValue)

       
    def info(self,fout=sys.stdout,defaults=True):
        colw = 15

        fout.write("%s%s\n"%("Name:".ljust(colw),self.name)) 
        fout.write("%s%s\n"%("Type:".ljust(colw),self.__class__.__name__)) 
        fout.write("Params:\n") 

        colw = 24
        separator = "-"*60
        fout.write(separator+"\n")
        if defaults:
            fout.write("%s%s%s\n"%("name".ljust(colw),"type".ljust(colw),"default".ljust(colw)))
        else:
            fout.write("%s%s%s\n"%("name".ljust(colw),"type".ljust(colw),"value".ljust(colw)))
        fout.write(separator+"\n")

        for p in self.params:
            par = self.params[p]
            if defaults:
                fout.write("%s%s%s\n"%(par.name.ljust(colw),par.typeStr.ljust(colw),par.default))
            else:
                fout.write("%s%s%s\n"%(par.name.ljust(colw),par.typeStr.ljust(colw),par.value))

    def diagnose(self,fout=sys.stdout):
        self.info(fout=fout,defaults=False)
