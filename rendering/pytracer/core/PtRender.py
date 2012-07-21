import os,array
import datetime

from PtPluginManager import PtPluginManager
import PtWorld
import PtPixel
import PtCommon
import PtBucket
import PtProgressBar
from PtNode import PtNode
import PtScreenIO as io
import PtThreading

__all__=['PtBegin','PtRender','PtEnd']

def PtBegin(verbose=0):
    # initialize world
    PtWorld.initialize()
    io.initialize()
    PtWorld.getOptions().verbose.setValue(verbose)

    # Welcome msg
    msg ="Pytrace Rendering API\n"
    msg+="by Rudy Cortes - rudy@rudycortes.com\n\n"
    io.oInfo(msg,0,label=False)

    # Load Plugins
    corePlugins = ['camera','driver','shape']
     
    io.oInfo("Loading Plugins:\n",1)
    for dir in corePlugins:
        pdir = os.path.join(PtCommon.rootDir,dir)
        if os.path.exists(pdir):
            io.oInfo("\t%s\n"%os.path.basename(pdir).capitalize(),
                     2,
                     label=False)
            PtPluginManager.loadPlugins(pdir,core=True)    

    PtWorld.driver = PtNode("jpeg_driver")


def PtRender():

    xres = PtWorld.options.xres.value
    yres = PtWorld.options.yres.value
    bucketSize = PtWorld.options.bucketSize.value

    # calculate the buckets that we will need
    bw = PtBucket.PtBucketWorker()
    bw.calculateBuckets(xres,yres,bucketSize)
    processed = len(bw.buckets)

    # local function to process buckets
    def processBucket(tbucket,pixels):
        PtWorld.driver.prepareBucket(tbucket)
        tbucket.process(pixels)
        PtWorld.driver.writeBucket(tbucket)
        #progress.increment(i)
        #," - %02d:%02d:%02d:%02d"%(hours,minutes,seconds,timeDiff.microseconds))


    timeStart = datetime.datetime.now()

    io.oInfo("Rendering image with %s x %s\n"%(xres,yres),1) 
    io.oInfo("Bucket Size %s\n"%bucketSize,1) 
    
    # create list of empty pixels
    pixels = []
    for i in range(xres * yres):
        pixels.append(PtPixel.PtPixel())
    

    # open the driver
    q = PtWorld.driver.open(PtWorld.options)
    progress = PtProgressBar.PtProgressBar(len(bw.buckets))
    
    # initialize threadpool
    #pool = PtThreading.PtThreadPool(4)

    # process buckets
    for i,tbucket in enumerate(bw.buckets):
        processBucket(tbucket,pixels)

        timeNow = datetime.datetime.now()
        timeDiff = timeNow - timeStart
        hours, remainder = divmod(timeDiff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        progress.increment(i," - %02d:%02d:%02d:%02d"%(hours,minutes,seconds,timeDiff.microseconds))
    progress.setValue(100)
    print "\n"

    # wait for pool to complete
    #pool.wait_completion()
    #progress.setValue(100)
    #print "\n"

    timeEnd = datetime.datetime.now()
    timeDiff = timeEnd - timeStart
    hours, remainder = divmod(timeDiff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print "process time %02d:%02d:%02d:%02d"%(hours,minutes,seconds,timeDiff.microseconds)

    # close the driver
    PtWorld.driver.close()


def PtEnd():
    pass

