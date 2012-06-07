import os,glob
import unittest

rootdir = os.path.dirname(os.path.abspath(__file__))
allTests = glob.glob(os.path.join(rootdir,"*.py"))

for i in allTests:
    if "__init__.py" in i or \
       __file__ in i:
        continue
    moduleName = os.path.basename(i)[:-3]
    mod = __import__(moduleName,globals(),locals(),[],-1)
    suite = eval("unittest.TestLoader().loadTestsFromTestCase(mod.%s)"%moduleName)
    print "Testing %s"%moduleName[:-4]
    unittest.TextTestRunner().run(suite)
