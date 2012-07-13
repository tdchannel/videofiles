import PtCommon
import PtGeom

import math
import copy

class PtMatrix():
    def __init__(self,*args):
        if len(args) > 0 and type(args[0]) == list and len(args[0]) == 16:
            self.m = copy.copy(args[0])
        else:
            self.m = [1.,0.,0.,0.,
                      0.,1.,0.,0.,
                      0.,0.,1.,0.,
                      0.,0.,0.,1.]

    def fromList(self,lst):
        self.m = copy.copy(lst)
    
    @property
    def identity(self):
        for i in range(4):
            for j in range(4):
                if i == j:
                    self.m[i*4 + j] = 1.
                else:
                    self.m[i*4+j] = 0.
    @property
    def determinant(self):
        m = self.m
        c0 = m[0] * (m[10]*m[15]*m[5]-m[14]*m[11]*m[5] +
                           m[6]*m[15]*-m[9]-m[14]*m[7]*-m[9] + 
                           m[6]*m[11]*m[13]-m[10]*m[7]*m[13]);
        c1 =-m[4] * (m[10]*m[15]*m[1]-m[14]*m[11]*m[1] +
                           m[2]*m[15]*-m[9]-m[14]*m[3]*-m[9] +
                           m[2]*m[11]*m[13]-m[10]*m[3]*m[13]);
        c2 = m[8] * (m[6] *m[15]*m[1]-m[14]*m[7] *m[1] +
                           m[2]*m[15]*-m[5]-m[14]*m[3]*-m[5] +
                           m[2]*m[7] *m[13]-m[6] *m[3]*m[13]);
        c3 = -m[12]*(m[6] *m[11]*m[1]-m[10]*m[7] *m[1] +
                           m[2]*m[11]*-m[5]-m[10]*m[3]*-m[5] +
                           m[2]*m[7] *m[9] -m[6] *m[3]*m[9]);
        return c0 + c1 + c2 + c3;


    @property
    def transpose(self):
        m = self.m
        tmp = [0,0,0,0,
               0,0,0,0,
               0,0,0,0,
               0,0,0,0]
        tmp[0]=m[0];  tmp[1]=m[4];  tmp[2]=m[8];   tmp[3]=m[12];
        tmp[4]=m[1];  tmp[5]=m[5];  tmp[6]=m[9];   tmp[7]=m[13];
        tmp[8]=m[2];  tmp[9]=m[6];  tmp[10]=m[10]; tmp[11]=m[14];
        tmp[12]=m[3]; tmp[13]=m[7]; tmp[14]=m[11]; tmp[15]=m[15];
        self.m = tmp


    @property
    def invert(self):	
        d = copy.copy(self.m)
        m = self.m
        dtr = 1./self.determinant

        ## Row 1
        d[0] = (m[10]*m[15]*m[5] - m[11]*m[14]*m[5]  + 
                m[6] *m[15]*-m[9]- m[7] *m[14]*-m[9] + 
                m[6] *m[11]*m[13]- m[7] *m[10]*m[13])*dtr;
        d[1] = -1*(m[10]*m[15]*m[4] - m[11]*m[14]*m[4] +
                   m[6]*m[15]*-m[8] - m[7]*m[14]*-m[8] +
                   m[6]*m[11]*m[12] - m[7]*m[10]*m[12])*dtr;
        d[2] = (m[9]*m[15]*m[4] - m[11]*m[13]*m[4] +
                m[5]*m[15]*-m[8]- m[7]*m[13]*-m[8] +
                m[5]*m[11]*m[12]- m[7]*m[9]*m[12])*dtr;
        d[3] = -1*(m[9]*m[14]*m[4] - m[10]*m[13]*m[4] +
                   m[5]*m[14]*-m[8]- m[6]*m[13]*-m[8]  +
                   m[5]*m[10]*m[12]- m[6]*m[9]*m[12])*dtr;
        ## Row 2
        d[4] = -1*(m[10]*m[15]*m[1] - m[11]*m[14]*m[1] +
                   m[2]*m[15]*-m[9] - m[3]*m[14]*-m[9]  +
                   m[2]*m[11]*m[13] - m[3]*m[10]*m[13])*dtr;
        d[5] = (m[10]*m[15]*m[0] - m[11]*m[14]*m[0] +
                m[2]*m[15]*-m[8] - m[3]*m[14]*-m[8]  +
                m[2]*m[11]*m[12] - m[3]*m[10]*m[12])*dtr;
        d[6] = -1*(m[9]*m[15]*m[0] - m[11]*m[13]*m[0] +
                   m[1]*m[15]*-m[8]- m[3]*m[13]*-m[8] +
                   m[1]*m[11]*m[12]- m[3]*m[9]*m[12])*dtr;
        d[7] = (m[9]*m[14]*m[0] - m[10]*m[13]*m[0] +
                m[1]*m[14]*-m[8]- m[2]*m[13]*-m[8] +
                m[1]*m[10]*m[12]- m[2]*m[9]*m[12])*dtr;
        d[12] = -1*(m[6]*m[11]*m[1]- m[7]*m[10]*m[1] +
                   m[2]*m[11]*-m[5]- m[3]*m[10]*-m[5]+
                   m[2]*m[7]*m[9]  - m[3]*m[6]*m[9])*dtr;
        ## Row 3
        d[8] = (m[6]*m[15]*m[1]  - m[7]*m[14]*m[1]  + 
                m[2] *m[15]*-m[5]- m[3] *m[14]*-m[5]+ 
                m[2] *m[7]*m[13] - m[3] *m[6]*m[13])*dtr;
        d[9] = -1*(m[6]*m[15]*m[0] - m[7]*m[14]*m[0] +
                   m[2]*m[15]*-m[4]- m[3]*m[14]*-m[4]+
                   m[2]*m[7]*m[12] - m[3]*m[6]*m[12])*dtr;
        d[10] = (m[5]*m[15]*m[0]- m[7]*m[13]*m[0] +
                m[1]*m[15]*-m[4]- m[3]*m[13]*-m[4]+
                m[1]*m[7]*m[12] - m[3]*m[5]*m[12])*dtr;
        d[11] = -1*(m[5]*m[14]*m[0]- m[6]*m[13]*m[0] +
                   m[1]*m[14]*-m[4]- m[2]*m[13]*-m[4]+
                   m[1]*m[6]*m[12] - m[2]*m[5]*m[12])*dtr;
        ## Row 4
        d[12] = -1*(m[6]*m[11]*m[1] - m[7]*m[10]*m[1] +
                    m[2]*m[11]*-m[5]- m[3]*m[10]*-m[5]+
                    m[2]*m[7]*m[9]  - m[3]*m[6]*m[9])*dtr

        d[13] = (m[6]*m[11]*m[0]- m[7]*m[10]*m[0] +
                m[2]*m[11]*-m[4]- m[3]*m[10]*-m[4]+
                m[2]*m[7]*m[8]  - m[3]*m[6]*m[8])*dtr

        d[14] = -1*(m[5]*m[11]*m[0] - m[7]*m[9]*m[0] +
                    m[1]*m[11]*-m[4]- m[3]*m[9]*-m[4]+
                    m[1]*m[7]*m[8]  - m[3]*m[5]*m[8])*dtr

        d[15] = (m[5]*m[10]*m[0] - m[6]*m[9]*m[0] +
                 m[1]*m[10]*-m[4]- m[2]*m[9]*-m[4]+
                 m[1]*m[6]*m[8]  - m[2]*m[5]*m[8])*dtr

        dst = self.__class__()
        dst.fromList(d)
        dst.transpose
        self.m = dst.m

    def __mul__(self,other):
        if other.__class__.__name__ == "PtMatrix":
            ret = PtMatrix()
            a = self.m
            b = other.m
            
            ret[0]  = a[0]*b[0] + a[1]*b[4] + a[2]*b[8] + a[3]*b[12]
            ret[1]  = a[0]*b[1] + a[1]*b[5] + a[2]*b[9] + a[3]*b[13]
            ret[2]  = a[0]*b[2] + a[1]*b[6] + a[2]*b[10] + a[3]*b[14]
            ret[3]  = a[0]*b[3] + a[1]*b[7] + a[2]*b[11] + a[3]*b[15]
            
            ret[4]  = a[4]*b[0] + a[5]*b[4] + a[6]*b[8] + a[7]*b[12]
            ret[5]  = a[4]*b[1] + a[5]*b[5] + a[6]*b[9] + a[7]*b[13]
            ret[6]  = a[4]*b[2] + a[5]*b[6] + a[6]*b[10] + a[7]*b[14]
            ret[7]  = a[4]*b[3] + a[5]*b[7] + a[6]*b[11] + a[7]*b[15]
            
            ret[8]  = a[8]*b[0] + a[9]*b[4] + a[10]*b[8] + a[11]*b[12]
            ret[9]  = a[8]*b[1] + a[9]*b[5] + a[10]*b[9] + a[11]*b[13]
            ret[10] = a[8]*b[2] + a[9]*b[6] + a[10]*b[10] + a[11]*b[14]
            ret[11] = a[8]*b[3] + a[9]*b[7] + a[10]*b[11] + a[11]*b[15]
            
            ret[12] = a[12]*b[0] + a[13]*b[4] + a[14]*b[8] + a[15]*b[12]
            ret[13] = a[12]*b[1] + a[13]*b[5] + a[14]*b[9] + a[15]*b[13]
            ret[14] = a[12]*b[2] + a[13]*b[6] + a[14]*b[10] + a[15]*b[14]
            ret[15] = a[12]*b[3] + a[13]*b[7] + a[14]*b[11] + a[15]*b[15]
            
            return ret

    def __getitem__(self,key):
        return self.m[key]

    def __setitem__(self,key,value):
        self.m[key] = float(value)
	
    def __str__(self):
        stout = ""
        for i in range(4):
            stout += "%.10f %.10f %.10f %.10f\n" %(self.m[i*4],self.m[i*4+1],
                                                   self.m[i*4+2],self.m[i*4+3])
        return stout
	  
#class PtTransform():
#    def __init__(self,*args):
#        if len(args) > 0 and args[0].__class__.__name__ == "PtMatrix":
#            self.m = args[0] 
#            self.mInv = args[0]
#        else:
#            self.m = PtMatrix()
#            self.mInv = PtMatrix()
#
#        #self.mInv.invert
#
#    def __mul__(self,other):
#        if other.__class__.__name__ == "PtTransform":
#            ret = PtMatrix()
#            a = self.m.m
#            b = other.m.m
#            
#            ret[0]  = a[0]*b[0] + a[1]*b[4] + a[2]*b[8] + a[3]*b[12]
#            ret[1]  = a[0]*b[1] + a[1]*b[5] + a[2]*b[9] + a[3]*b[13]
#            ret[2]  = a[0]*b[2] + a[1]*b[6] + a[2]*b[10] + a[3]*b[14]
#            ret[3]  = a[0]*b[3] + a[1]*b[7] + a[2]*b[11] + a[3]*b[15]
#            
#            ret[4]  = a[4]*b[0] + a[5]*b[4] + a[6]*b[8] + a[7]*b[12]
#            ret[5]  = a[4]*b[1] + a[5]*b[5] + a[6]*b[9] + a[7]*b[13]
#            ret[6]  = a[4]*b[2] + a[5]*b[6] + a[6]*b[10] + a[7]*b[14]
#            ret[7]  = a[4]*b[3] + a[5]*b[7] + a[6]*b[11] + a[7]*b[15]
#            
#            ret[8]  = a[8]*b[0] + a[9]*b[4] + a[10]*b[8] + a[11]*b[12]
#            ret[9]  = a[8]*b[1] + a[9]*b[5] + a[10]*b[9] + a[11]*b[13]
#            ret[10] = a[8]*b[2] + a[9]*b[6] + a[10]*b[10] + a[11]*b[14]
#            ret[11] = a[8]*b[3] + a[9]*b[7] + a[10]*b[11] + a[11]*b[15]
#            
#            ret[12] = a[12]*b[0] + a[13]*b[4] + a[14]*b[8] + a[15]*b[12]
#            ret[13] = a[12]*b[1] + a[13]*b[5] + a[14]*b[9] + a[15]*b[13]
#            ret[14] = a[12]*b[2] + a[13]*b[6] + a[14]*b[10] + a[15]*b[14]
#            ret[15] = a[12]*b[3] + a[13]*b[7] + a[14]*b[11] + a[15]*b[15]
#            
#            return PtTransform(ret)

def PiTranslate(*args):
    if len(args) > 0 and type(args[0]) == list:
        vec = args[0]
        x = float(vec[0])
        y = float(vec[1])
        z = float(vec[2])
    elif len(args) and args[0].__class__.__name__ in["PtVector",'PtPoint']:
        vec = args[0]
        x = vec.x
        y = vec.y
        z = vec.z;
    elif len(args) == 0:
        x = 0.
        y = 0.
        z = 0.
    else:  
        raise PtCommon.PtTypeError("PiTranslate requires a list or a PtVector")

    l = [1.,0.,0.,x,
         0.,1.,0.,y,
         0.,0.,1.,z,
         0.,0.,0.,1.]
    mat = PtMatrix(l)
    return mat
    #return PtTransform(mat)

def PiScale(*args):
    if len(args) > 0 and type(args[0]) == list:
        vec = args[0]
        x = float(vec[0])
        y = float(vec[1])
        z = float(vec[2])
    elif len(args) > 0 and args[0].__class__.__name__ == "PtVector":
        vec = args[0]
        x = vec.x
        y = vec.y
        z = vec.z;
    elif len(args) == 0:
        x = 1.
        y = 1.
        z = 1.
    else:
        raise PtCommon.PtTypeError("PiScale requires a list or a PtVector")

    m = PtMatrix([x,0.,0.,0.,
                  0.,y,0.,0.,
                  0.,0.,z,0.,
                  0.,0.,0.,1.])
    #mi = PtMatrix([1./x,0.,0.,0.,
    #              0.,1./y,0.,0.,
    #              0.,0.,1./z,0.,
    #              0.,0.,0.,1.])
    #t = PtTransform()
    #t.m = m
    #t.mInv =mi
    return m


def PiRotateX(angle):
    sin_t = math.sin(float(angle))
    cos_t = math.cos(float(angle))
    rotl = [1.,0.,   0.,    0.,
            0.,cos_t,-sin_t,0.,
            0.,sin_t,cos_t ,0.,
            0.,0.,   0.,    1.]
    rotm = PtMatrix(rotl)
    return rotm
    #return PtTransform(rotm)

def PiRotateY(angle):
    sin_t = math.sin(float(angle))
    cos_t = math.cos(float(angle))
    rotl = [cos_t, 0., sin_t,0.,
            0.,    1., 0     ,0.,
            -sin_t,0., cos_t, 0.,
            0.,    0., 0.,    1.]
    rotm = PtMatrix(rotl)
    return rotm
    #return PtTransform(rotm)

def PiRotateZ(angle):
    sin_t = math.sin(float(angle))
    cos_t = math.cos(float(angle))
    rotl = [cos_t, -sin_t, 0., 0.,
            sin_t, cos_t,  0.,0.,
            0.,    0.,     1.,0.,
            0.,    0.,     0.,1.]
    rotm = PtMatrix(rotl)
    return rotm
    #return PtTransform(rotm)

# ////////////
# // TO DO: rotate by axis
#/////////////
