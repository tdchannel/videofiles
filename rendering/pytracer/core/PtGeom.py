
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

    def __str__(self):
        return "[%s,%s,%s]"%(self.x,self.y,self.z)

PtPoint2 = PtPoint

class PtVector(PtPoint):
    def __init__(self,x=0,y=0,z=0):
        PtPoint.__init__(self,x=x,y=y,z=z)
        self.w = 0 
