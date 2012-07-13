
import PtGeom
import PtWorld
import PtPixel

class PtBucket():
    def  __init__(self,pos=PtGeom.PtPoint2(0,0),
                  width=32,
                  height=32):
        self.pos    = pos 
        self.width  = width
        self.height = height

        self.pixels =[]
        for i in range(self.width * self.height):
            self.pixels.append(PtPixel.PtPixel())
        
    def process(self,pixels):
        xres = PtWorld.options.xres.value
        yres = PtWorld.options.yres.value


        cam = PtWorld.cameras[0]
        for y in range(self.pos.y, self.pos.y+ self.height):
            for x in range(self.pos.x, self.pos.x + self.width):
                ray = cam.createRay(x,y)
                px = pixels[(y * xres)+x]
                bpos = ((y - self.pos.y) * self.width) + (x-self.pos.x)
                pxb = self.pixels[bpos]
                
                for shape in PtWorld.shapes:
                    if shape.intersectP(ray):
                        pxb.r = px.r = 255
                        pxb.g = px.g = 255
                        pxb.b = px.b = 255
                    else:
                        pxb.r = px.r = (x / float(xres)) * 255
                        pxb.g = px.g = (y / float(yres)) * 255
                        pxb.b = px.b = 255

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

