import PIL.Image as Image

from .core import PtCommon
from .core import PtDriver
from .core.PtWorld import PtWorld

class jpeg_driver(PtDriver.PtDriver):
    def __init__(self,name=None):
        PtDriver.PtDriver.__init__(self,name=name)
        self.im = None

    def open(self,options):
        self.options = options

        xres = self.options.xres.value
        yres = self.options.yres.value

        self.im = Image.new("RGB",(xres,yres))
    
    
    def writeBucket(self,bucket):
        mb = Image.new("RGB",(bucket.width,bucket.height))
        px= []
        for i,val in enumerate(bucket.pixels):
            px.append((int(val.r),int(val.g),int(val.b)))
        
        mb.putdata(px)
        self.im.paste(mb,(bucket.pos.x,
                          bucket.pos.y))

    def close(self):
        outFile = "%s.jpg"%(self.options.outputFile)
        self.im.save(outFile,"JPEG")
