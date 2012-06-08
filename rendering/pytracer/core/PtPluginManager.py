
import glob, os, sys
import PtCommon

class PtPluginManagerError(Exception):
    def __init__(self,value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)

class PtPluginManager():
    plugins = {}

    @classmethod
    def loadPlugin(self,module):
        fname = module.split(".")[-1]
        tmp = __import__(module, globals(), locals(), [], -1)
        if fname not in self.plugins.keys():
            self.plugins[fname] = eval("tmp.%s"%fname)

    @classmethod 
    def loadPlugins(self,dir,core=False):
        files = glob.glob(os.path.join(dir,"*.py"))
        if len(files) > 0:
            # add the parent directory to the path
            parentDir = os.path.dirname(dir)
            if parentDir not in sys.path:
                sys.path.append(parentDir)

        for file in files:
            if "__init__.py" in file: continue

            # store a copy of each plugin
            fname,ext = os.path.splitext(os.path.basename(file))
            module = "%s.%s"%(os.path.basename(dir),fname)
            self.loadPlugin(module)

    @classmethod
    def getPlugin(self,name):
        if name in self.plugins.keys():
            return self.plugins[name]
        else:
            raise PtPluginManagerError("Plugin %s not found"%name) 
