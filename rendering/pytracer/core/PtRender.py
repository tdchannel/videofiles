import os,array

from PtPluginManager import PtPluginManager
from PtWorld import PtWorld
import PtPixel
import PtCommon
import PtBucket

__all__=['PtBegin','PtRender','PtEnd']

def PtBegin():
    # Load Plugins
    corePlugins = ['camera','driver','shape']
    
    print "loading Plugins:"
    for dir in corePlugins:
        pdir = os.path.join(PtCommon.rootDir,dir)
        if os.path.exists(pdir):
            print "\t%s"%os.path.basename(pdir).capitalize()
            PtPluginManager.loadPlugins(pdir,core=True)    

    # initialize world
    PtWorld.initialize()

def PtRender():
    xres = PtWorld.options.xres.value
    yres = PtWorld.options.yres.value
    bucketSize = PtWorld.options.bucketSize.value

    pixels = []
    for i in range(xres * yres):
        pixels.append(PtPixel.PtPixel())
    # calculate the buckets that we will need
    bw = PtBucket.PtBucketWorker()
    bw.calculateBuckets(xres,yres,bucketSize)
    # open the driver
    q = PtWorld.driver.open(PtWorld.options)
    # process buckets
    for tbucket in bw.buckets:
        tbucket.process(pixels)
        PtWorld.driver.writeBucket(tbucket)   

    PtWorld.driver.close()


def PtEnd():
    pass

