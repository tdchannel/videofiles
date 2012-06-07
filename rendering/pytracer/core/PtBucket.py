
import PtGeom

class PtBucket():
    def  __init__(self,pos=PtGeom.PtPoint2(0,0),
                  width=32,
                  height=32):
        self.pos    = pos 
        self.width  = width
        self.height = height

    def process(self,pixels):
        for y in range(self.pos.y, self.pos.y+ self.height):
            for x in range(self.pos.x, self.pos.x + self.width):
                g = y / 100.0
                r = x / 100.0
                pixels[(y * 100)+x] = g



class PtBucketWorker():
    def __init__(self):
        self.buckets    = []
        self.numx       = 0
        self.numy       = 0

    def calculateBuckets(self,xres,yres,bucketSize):
        self.numx = xres / bucketSize
        self.numy = yres / bucketSize

        if xres % bucketSize != 0: self.numx +=1
        if yres % bucketSize != 0: self.numy +=1

        for y in range(0,yres,bucketSize):
            for x in range(0,xres,bucketSize):
                tmpBucket = PtBucket(pos=PtGeom.PtPoint2(x,y))
                nextx = x + bucketSize
                modx  = nextx % xres
                tmpBucket.width  = bucketSize if modx > bucketSize else bucketSize if modx == bucketSize else bucketSize - modx
                
                nexty = y + bucketSize
                mody  = nexty % yres
                tmpBucket.height = bucketSize if mody > bucketSize else bucketSize if mody == bucketSize else bucketSize - mody
                self.buckets.append(tmpBucket)
