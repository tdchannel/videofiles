import os,array

from PtPluginManager import PtPluginManager
import PtWorld
import PtPixel
import PtCommon
import PtBucket
import PtProgressBar

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
    progress = PtProgressBar.PtProgressBar(len(bw.buckets))
    # process buckets
    for i,tbucket in enumerate(bw.buckets):
        tbucket.process(pixels)
        PtWorld.driver.writeBucket(tbucket)
        progress.increment(i)
    progress.setValue(100)
    print "\n"
    PtWorld.driver.close()


def PtEnd():
    pass

