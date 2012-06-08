import PtCommon
import PtGeom

class PtParamError(Exception):
    def __init__(self,value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)

class PtParamBase():
    def __init__(self,name=None,value=None,parmType=None):
        self.type   = parmType if parmType else None
        self.name   = name if name else PtCommon.getRandomName("Param") 
        self.__value  = value if value else None
        self.default  = value 

    @property
    def value(self):
        return self.__value

    @property
    def typeStr(self):
        return PtCommon.dataTypeToStr(self.type)

    def setValue(self,value):
        try:
            self.__value = value
        except:
            raise PtParamError("Error setting %s"%self.name)

class PtParamInt(PtParamBase):
    def __init__(self,name=None,value=None):
        PtParamBase.__init__(self,name=name,
                           parmType=PtCommon.TDC_TYPE_INT)
        if value:
            self.setValue(value)
            self.default = value
    
    def setValue(self,value):
        if type(value) == int:
            PtParamBase.setValue(self,value)
        else:
            raise PtParamError("Tried to assign %s to %s %s"%(value.__class__.__name__,
                                                              self.__class__.__name__,
                                                             self.name))


class PtParamFloat(PtParamBase):
    def __init__(self,name=None,value=None):
        PtParamBase.__init__(self,name=name,
                           parmType=PtCommon.TDC_TYPE_FLOAT)
        if value:
            self.setValue(value)
            self.default = value
    
    def setValue(self,value):
        if type(value) in [float,int]:
            PtParamBase.setValue(self,float(value))
        else:
            raise PtParamError("Tried to assign %s to %s %s"%(value.__class__.__name__,
                                                              self.__class__.__name__,
                                                             self.name))


class PtParamPoint(PtParamBase):
    def __init__(self,name=None,value=None):
        PtParamBase.__init__(self,name=name,
                             parmType=PtCommon.TDC_TYPE_POINT)
        if value:
            self.setValue(value)
            self.default = value

    def __str__(self):
        return "[%s %s %s]"%(self.value.x,self.value.y,self.value.z)

    def setValue(self,value):
        if isinstance(value, PtGeom.PtPoint) :
            PtParamBase.setValue(self,value)
        elif type(value) == list:
            # make a point
            PtParamBase.setValue(self,PtGeom.PtPoint(value))
        else:
            raise PtParamError("Tried to assign %s to %s %s"%(value.__class__.__name__,
                                                              self.__class__.__name__,
                                                              self.name))

class PtParamVector(PtParamBase):
    def __init__(self,name=None,value=None):
        PtParamBase.__init__(self,name=name,
                             parmType=PtCommon.TDC_TYPE_VECTOR)
        if value:
            self.setValue(value)
            self.default = value

    def __str__(self):
        return "[%s %s %s]"%(self.value.x,self.value.y,self.value.z)
    
    def setValue(self,value):
        if isinstance(value, PtGeom.PtVector) :
            PtParamBase.setValue(self,value)
        elif type(value) == list:
            # make a vector
            PtParamBase.setValue(self,PtGeom.PtVector(value))
        else:
            raise PtParamError("Tried to assign %s to %s %s"%(value.__class__.__name__,
                                                              self.__class__.__name__,
                                                             self.name))
