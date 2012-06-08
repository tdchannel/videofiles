import sys, inspect
from PtPluginManager import PtPluginManager
import PtPlugin
import PtCommon
import PtParam 

class PtNode():

    def __init__(self,pluginName,name=None):
        # create an instance of the plugin
        #plugin = eval("PtPluginManager.getPlugin('%s').%s"%(pluginName,pluginName))
        plugin = eval("PtPluginManager.getPlugin('%s')"%pluginName)
        if not inspect.isclass(plugin):
            plugin = eval("plugin.%s"%pluginName)

        ins = plugin()
        self.name   = name if name else PtCommon.getRandomName(ins.name)
        self.type   = ins.name
        self.params = ins.params 
        for i in self.params:
            exec("self.%s = self.params[i]"%i)

        for i in ins.methods:
            exec("self.%s = ins.methods[i]"%i)
        
    #
    # Public
    #
    ######### Properties ########
    @property
    def numParams(self):
        return len(self.params.keys())

    def paramValue(self,paramName):
        param = self.params[paramName]
        return param.value

    def setParamValue(self,paramName,paramValue):
        param = self.params[paramName]
        param.setValue(paramValue)
       
    def info(self,fout=sys.stdout,defaults=True):
        colw = 15

        fout.write("%s%s\n"%("Name:".ljust(colw),self.name)) 
        fout.write("%s%s\n"%("Type:".ljust(colw),self.type)) 
        fout.write("Params:\n") 

        colw = 24
        separator = "-"*60
        fout.write(separator+"\n")
        if defaults:
            fout.write("%s%s%s\n"%("name".ljust(colw),"type".ljust(colw),"default".ljust(colw)))
        else:
            fout.write("%s%s%s\n"%("name".ljust(colw),"type".ljust(colw),"value".ljust(colw)))
        fout.write(separator+"\n")

        for p in self.params:
            par = self.params[p]
            if defaults:
                fout.write("%s%s%s\n"%(par.name.ljust(colw),par.typeStr.ljust(colw),par.default))
            else:
                fout.write("%s%s%s\n"%(par.name.ljust(colw),par.typeStr.ljust(colw),par.value))

    def diagnose(self,fout=sys.stdout):
        self.info(fout=fout,defaults=False)
