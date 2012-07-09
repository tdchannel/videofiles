from PtPluginManager import PtPluginManager

#class PtWorld():
cameras=[]
options = None
driver  = None
shapes  = []


#@classmethod
def initialize():
    from PtNode import PtNode
    global options, driver, cameras, shapes
    PtPluginManager.loadPlugin("PtOptions")
    options = PtNode("PtOptions")
    driver  = PtNode("jpeg_driver")
    cameras = []
    shapes = []

#@classmethod
def getOptions():
    return options

#@classmethod
def getCameras():
    return cameras

