import math

import PtGeom
import PtWorld
import PtPixel
import random

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
        samples = PtWorld.options.samples.value

        # right now we are just getting the first camera, we should get this
        #with a node accessor
        cam = PtWorld.cameras[0]
        if samples >= 0:
            realSamples = 1
        else:
            realSamples = int(pow(2,abs(samples)))
            realSamples = abs(samples)

        
        for y in range(self.pos.y, self.pos.y+ self.height, realSamples):
            for x in range(self.pos.x, self.pos.x + self.width, realSamples):
               
                # get the center of the pixel
                pixelDelta = 0
                if samples < 0:
                    pixelDelta = 0.5 * realSamples

                bucketColorR = random.randint(0,255)
                bucketColorG = random.randint(0,255)
                bucketColorB = random.randint(0,255)
                
                #print "-"*20
                #print "orig sample ",x,y
                #print "real sample ",x+pixelDelta,y+pixelDelta
                #print "paint x from %s to %s"%(x,x+(realSamples-1))
                #print "paint y from %s to %s"%(y,y+(realSamples-1)) 
                #print "-"*20
                ray = cam.createRay(x+pixelDelta,y+pixelDelta)
                # get a pointer to the current pixel
                #print "px ",(y * xres) + x
                #print "#"*20

                px = pixels[(y * xres)+x]

                #for j in range(realSamples):
                #    for i in range(realSamples):
                #        bpos = (((y+i) - self.pos.y) * self.width) + ((x+j) -self.pos.x)
                #        pxb = self.pixels[min(bpos,len(self.pixels)-1)]
                #        pxb.r = px.r = bucketColorR
                #        pxb.g = px.g = bucketColorG
                #        pxb.b = px.b = bucketColorB

                for shape in PtWorld.shapes:
                    if shape.intersectP(ray):
                        #print "hit at ",x+pixelDelta,y+pixelDelta
                        #print "-"*20
                        for j in range(realSamples):
                            for i in range(realSamples):
                                #bpos = (((y+j) - self.pos.y) * self.width) + ((x+i)-self.pos.x)
                                bpos = (((y+i) - self.pos.y) * self.width) + ((x+j)-self.pos.x)
                                #if bpos > (PtWorld.options.bucketSize.value**2):    
                                #print bpos,x+i+(realSamples*2),y+j+(realSamples*2)
                                pxb = self.pixels[min(bpos,len(self.pixels)-1)]
                                pxb.r = px.r = 255
                                pxb.g = px.g = 255
                                pxb.b = px.b = 255
                                #pxb.r = px.r = (x / float(xres)) * 255
                                #pxb.g = px.g = (y / float(yres)) * 255
                                #pxb.b = px.b = 255
                    else:
                        #print "miss at ",x+pixelDelta,y+pixelDelta
                        #print "-"*20
                        for j in range(realSamples):
                            for i in range(realSamples):
                                #bpos = (((y+j) - self.pos.y) * self.width) + ((x+i)-self.pos.x)
                                bpos = ((((y+i) - self.pos.y) *self.width) + ((x+j)-self.pos.x))
                                #if bpos > (PtWorld.options.bucketSize.value**2):    
                                #print bpos,x+i+(realSamples*2),y+j+(realSamples*2)
                                pxb = self.pixels[min(bpos,len(self.pixels)-1)]
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
                nextx = x + bucketSize
                modx  = nextx % xres
                tmpBucketWidth  = bucketSize if modx > bucketSize else bucketSize if modx == bucketSize else bucketSize - modx
                

                nexty = y + bucketSize
                mody  = nexty % yres
                tmpBucketHeight = bucketSize if mody > bucketSize else bucketSize if mody == bucketSize else bucketSize - mody

                # create a bucket and append it to the buckets list
                tmpBucket = PtBucket(pos=PtGeom.PtPoint2(x,y),
                                     width=tmpBucketWidth,
                                     height=tmpBucketHeight)
                self.buckets.append(tmpBucket)

