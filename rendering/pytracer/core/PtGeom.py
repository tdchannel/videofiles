import copy

class PtPointError(Exception):
    def __init__(self,value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)


class PtPoint():
    def __init__(self,x=0,y=0,z=0):
        if type(x) == list and len(x) >1:
            self.x = x[0]
            self.y = x[1]
            if len(x) > 2:
                self.z = x[2]
        else:
            self.x = x
            self.y = y
            self.z = z

        self.w = 1
  
    def transform(self,xf,ret=False):
        #m = xf.m.m
        m = xf.m
        x = self.x; y=self.y; z=self.z;
        
        xp = m[0]*x + m[1]*y + m[2]*z + m[3]
        yp = m[4]*x + m[5]*y + m[6]*z + m[7]
        zp = m[8]*x + m[9]*y + m[10]*z+ m[11]
        wp = m[12]*x+ m[13]*y+ m[14]*z+ m[15]
        
        if wp == 0:
            raise PtPointError("Error transforming point")
        
        if ret:
            if wp == 1.:
                return self.__class__(xp,yp,zp)
            else:
                return self.__class__(xp/w,yp/w,zp/w)
        else:
            if wp == 1.:
                self.x = xp
                self.y = yp
                self.z = zp
            else:
                self.x = xp/w
                self.y = yp/w
                self.z = zp/w

    #
    # Add two points
    #
    def __add__(self,other):
        if other.__class__.__name__ in["PtPoint","PtVector"]:
            self.x += other.x
            self.y += other.y
            self.z += other.z
        elif type(other) in [int,float]:
            self.x += other
            self.y += other
            self.z += other
        else:
            raise PtPointError("Can not add to %s"%type(other))
        return self

    def __sub__(self,other):
        if other.__class__.__name__ in["PtPoint","PtVector"]:
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
        elif type(other) in [int,float]:
            self.x -= other
            self.y -= other
            self.z -= other
        else:
            raise PtPointError("Can not subtract to %s"%type(other))

        return self

    def __mul__(self,other):
        if other.__class__.__name__ in["PtPoint","PtVector"]:
            self.x *= other.x
            self.y *= other.y
            self.z *= other.z
        elif type(other) in [int,float]:
            self.x *= other
            self.y *= other
            self.z *= other
        else:
            raise PtPointError("Can not multiply to %s"%type(other))

        return self

    #
    # compare two points
    #
    # less than
    def __lt__(self, other):
        if other.__class__.__name__ != self.__class__.__name__:
            return False
        if other.x < self.x and other.y < self.y and other.z < self.z:
            return True
        else:
            return False

    # less than or equal
    def __le__(self,other):
        if other.__class__.__name__ != self.__class__.__name__:
            return False
        if other.x <= self.x and other.y <= self.y and other.z <= self.z:
            return True
        else:
            return False

    # equal
    def __eq__(self, other):
        if other.__class__.__name__ != self.__class__.__name__:
            return False
        if other.x == self.x and other.y == self.y and other.z == self.z:
            return True
        else:
            return False

    # not equal
    def __ne__(self,other):
        if other.__class__.__name__ != self.__class__.__name__:
            return False

        if other.x != self.x and other.y != self.y and other.z != self.z:
            return True
        else:
            return False

    # greater than or equal
    def __gt__(self, other):
        if other.__class__.__name__ != self.__class__.__name__:
            return False
        if other.x >= self.x and other.y >= self.y and other.z >= self.z:
            return True
        else:
            return False
    
    # greater than
    def __ge__(self, other):
        if other.__class__.__name__ != self.__class__.__name__:
            return False
        if other.x > self.x and other.y > self.y and other.z > self.z:
            return True
        else:
            return False


    def __str__(self):
        return "[%s,%s,%s]"%(self.x,self.y,self.z)


PtPoint2 = PtPoint
class PtVector(PtPoint):
    def __init__(self,x=0.,y=0.,z=0.):
        PtPoint.__init__(self,x=x,y=y,z=z)
        self.w = 0 

    def transform(self,xf,ret=False):
        m = xf.m
        x = self.x; y=self.y; z=self.z;
        
        xp = m[0]*x + m[1]*y + m[2]*z
        yp = m[4]*x + m[5]*y + m[6]*z
        zp = m[8]*x + m[9]*y + m[10]*z
        if ret:       
            return self.__class__(xp,yp,zp)
        else:
            self.x = xp
            self.y = yp
            self.z = zp


class PtBBox():
    def __init__(self,min=PtPoint(),max=PtPoint(),center=PtPoint()):
        self.min = min
        self.max = max
        self.center = center
    
    def __calculateCenter(self):
       self.min + (self.max * 0.5)

    def expandToPoint(self, point):
        if point < self.min:
            self.min = point
        if point > self.max:
            self.max = point

    def expandToBBox(self,PtBBox):
        pass


class PtRay():
    def __init__(self,origin=None,direction=None,
                    mint=None,maxt=None):
        if origin:
            self.o = origin
        else:
            self.o = PtPoint(0.,0.,0.)
        if direction:
            self.d = direction
        else:
            self.d = PtVector(0.,0.,1.)
        if mint:
            self.mint = mint
        else:
            self.mint = 0.
        if maxt:
            self.maxt = maxt
        else:
            self.maxt = 10000000.
   
    def offset(self,val,ret=False):
        rout = copy.copy(self)#.__class__() 
        rout.d *= val
        rout.o += rout.d
        if ret:
            return rout
        else:
            self.o = rout.o
            self.d = rout.d


    def transform(self,xform,ret=False):
        rout = self.__class__()
        rout.o = self.o.transform(xform,True)
        rout.d = self.d.transform(xform,True)
        
        if ret:
            return rout
        else:
            self.o = rout.o
            self.d = rout.d


    def __str__(self):
        return "o %s d %s\nmin %s  max %s"%(self.o,self.d,self.mint,self.maxt)
