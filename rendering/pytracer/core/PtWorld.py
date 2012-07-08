from PtPluginManager import PtPluginManager
from PtNode import PtNode

class PtWorld():

    cameras=[]
    options = None
    driver  = None
    shapes  = []

    @classmethod
    def initialize(self):
        PtPluginManager.loadPlugin("PtOptions")
        self.options = PtNode("PtOptions")
        self.driver  = PtNode("jpeg_driver")

    @classmethod
    def getOptions(self):
        return self.options
