import math, sys
from struct import unpack

import maya.OpenMaya as OM
import maya.OpenMayaMPx as OMPx

################################
#
# Read Node 
#
################################
kTdcMddReadNodeName = "tdcMddRead"
tdcMddReadId = OM.MTypeId(0x87024400)


# Node definition
class tdcMddRead(OMPx.MPxDeformerNode):
    # class variables
    offset = OM.MObject()
    time = OM.MObject()
    cycle = OM.MObject()
    mddFile = OM.MObject()

    # constructor
    def __init__(self):
        OMPx.MPxDeformerNode.__init__(self)
        self.mddFileVal = ""
        self.frames     = 0
        self.points     = 0
        self.times      = None
        self.deltas     = None
        self.fileHandle = None

    def loadData(self,fileName,frame,offset,cycle):
        if not self.fileHandle and fileName != self.mddFileVal:
            self.deltas = {}
            self.mddFileVal = fileName
            self.fileHandle = open(fileName, 'rb')
            self.frames, self.points = unpack(">2i", self.fileHandle.read(8))
            self.times = unpack((">%df" % self.frames), self.fileHandle.read(self.frames * 4))
        
        #if frame not in self.deltas.keys() and not self.fileHandle.closed:
        if self.fileHandle and not self.fileHandle.closed:
            headerOffset = 8 + (self.frames * 4)
           
            if cycle:
                frame = (frame + offset) % self.frames
            else:
                frame = frame + offset
                if frame > self.frames:
                    frame = self.frames
                elif frame < 1:
                    frame = 1
       

            self.fileHandle.seek(headerOffset + ((frame) * 12 * self.points))
            pointList = []
            for pp in range(self.points):
                pointvals = unpack('>3f', self.fileHandle.read(12))
                point = OM.MPoint(pointvals[0],
                                        pointvals[1],
                                        pointvals[2])
                pointList.append(point)
            
            self.deltas[frame]=pointList

        return frame


    # deform
    def deform(self,dataBlock,geomIter,matrix,multiIndex):
        fileHandle = dataBlock.inputValue( self.mddFile )
        fileValue = fileHandle.asString()
        
        timeHandle = dataBlock.inputValue( self.time )
        timeValue = timeHandle.asInt()

        offsetHandle = dataBlock.inputValue( self.offset )
        offsetValue = offsetHandle.asInt() * -1

        cycleHandle = dataBlock.inputValue( self.cycle )
        cycleValue = cycleHandle.asBool()

        if fileValue != "":
            frame = self.loadData(fileValue,timeValue,offsetValue,cycleValue)
            while geomIter.isDone() == False:
               pp = self.deltas[frame][geomIter.index()]
               geomIter.setPosition(pp)
               geomIter.next() 
    

# creator
def nodeCreator():
    return OMPx.asMPxPtr( tdcMddRead() )


# initializer
def nodeInitializer():
    nAttr = OM.MFnNumericAttribute()
    tAttr = OM.MFnTypedAttribute()

    tdcMddRead.time = nAttr.create( "time", "ti", OM.MFnNumericData.kInt, 0 )
    nAttr.setKeyable(True)
    nAttr.setHidden(True)

    tdcMddRead.offset = nAttr.create( "offset", "of", OM.MFnNumericData.kInt, 0 )
    nAttr.setKeyable(True)

    tdcMddRead.cycle = nAttr.create( "cycle", "cy", OM.MFnNumericData.kBoolean, False )
    nAttr.setKeyable(True)

    tdcMddRead.mddFile = tAttr.create("mddFile","mf",
                                      OM.MFnData.kString)
    tAttr.setStorable(True)
    tAttr.setKeyable(False)

    # add attribute
    try:
        tdcMddRead.addAttribute( tdcMddRead.time )
        tdcMddRead.addAttribute( tdcMddRead.offset )
        tdcMddRead.addAttribute( tdcMddRead.cycle )
        tdcMddRead.addAttribute( tdcMddRead.mddFile )

        outputGeom = OMPx.cvar.MPxDeformerNode_outputGeom
        tdcMddRead.attributeAffects( tdcMddRead.time, outputGeom )
        tdcMddRead.attributeAffects( tdcMddRead.cycle, outputGeom )
        tdcMddRead.attributeAffects( tdcMddRead.offset, outputGeom )
        tdcMddRead .attributeAffects( tdcMddRead.mddFile, outputGeom )
    except:
        sys.stderr.write("Failed to create attributes of %s node\n", 
                         kTdcMddReadNodeName )


################################
#
# Command
#
################################

kTdcMddReadCmdName      = "tdcMddRead"
kTdcMddReadFileFlag     = "-f"
kTdcMddReadLongFileFlag = "-file"
kTdcMddReadOffsetFlag   = "-o"
kTdcMddReadOffsetLongFlag= "-offset"
kTdcMddReadCycleFlag    = "-c"
kTdcMddReadCycleLongFlag= "-cycle"

# command
class TdcMddReadCommand(OMPx.MPxCommand):
    def __init__(self):
        OMPx.MPxCommand.__init__(self)

    def setFlagValues(self,
                      argData,
                      mfn,
                      fileFlagSet,
                      offsetFlagSet,
                      cycleFlagSet):

        if fileFlagSet:
            fileArg = argData.flagArgumentString(kTdcMddReadFileFlag, 0)
            # get the plug form mddFile 
            mplug = mfn.findPlug("mddFile")
            mplug.setString(fileArg)
        
        if offsetFlagSet:
            offset = argData.flagArgumentInt(kTdcMddReadOffsetFlag, 0)
            # get the plug form mddFile 
            mplug = mfn.findPlug("offset")
            mplug.setInt(offset)
        
        if cycleFlagSet:
            cycle = argData.flagArgumentBool(kTdcMddReadCycleFlag, 0)
            # get the plug form mddFile 
            mplug = mfn.findPlug("cycle")
            mplug.setBool(cycle)


    def doIt(self,argList):
        argData = OM.MArgDatabase(self.syntax(),argList)
        mg = OM.MGlobal
        # Create a selection list
        selist = OM.MSelectionList()
        argData.getCommandArgument(0,selist)
        
        # create an MObject instance
        depNode = OM.MObject()
        mdg     = OM.MDGModifier()

        # flags
        fileFlagSet     = argData.isFlagSet(kTdcMddReadFileFlag)
        offsetFlagSet   = argData.isFlagSet(kTdcMddReadOffsetFlag)
        cycleFlagSet    = argData.isFlagSet(kTdcMddReadCycleFlag)
        
        if argData.isQuery():
            # get the first element of our selection list
            selist.getDependNode(0,depNode)

            # make an instance of a MFnDependencyNode class
            mfn = OM.MFnDependencyNode(depNode)
            if fileFlagSet:
                mplug = mfn.findPlug("mddFile")
                self.setResult(mplug.asString())
                return
            if offsetFlagSet:
                mplug = mfn.findPlug("offset")
                self.setResult(mplug.asInt())
                return
            if cycleFlagSet:
                mplug = mfn.findPlug("cycle")
                self.setResult(mplug.asBool())
                return

        elif argData.isEdit():
            # get the first element of our selection list
            selist.getDependNode(0,depNode)
            # make an instance of a MFnDependencyNode class
            mfn = OM.MFnDependencyNode(depNode)
            self.setFlagValues(argData,
                               mfn,
                               fileFlagSet,
                               offsetFlagSet,
                               cycleFlagSet)
        else:
            mg.selectCommand(selist)
            res = OM.MCommandResult()
            mg.executeCommand("deformer -type %s;"%kTdcMddReadNodeName,res)


            mar = []
            res.getResult(mar)
            selist.clear()
            # add new MDDRead to the selection list
            selist.add(mar[0])
            # get the first element of our selection list
            selist.getDependNode(0,depNode)
            # make an instance of a MFnDependencyNode class
            mfn = OM.MFnDependencyNode(depNode)
            mg.executeCommand("connectAttr -f time1.outTime %s.time"%mar[0]);
            self.setFlagValues(argData,
                               mfn,
                               fileFlagSet,
                               offsetFlagSet,
                               cycleFlagSet)

# Creator
def tdcMddReadCmdCreator():
    return OMPx.asMPxPtr( TdcMddReadCommand() )
    
# Syntax creator
def tdcMddReadSyntaxCreator():
    syntax = OM.MSyntax()
    syntax.addFlag(kTdcMddReadFileFlag,kTdcMddReadLongFileFlag,
                   OM.MSyntax.kString)
    syntax.addFlag(kTdcMddReadOffsetFlag, kTdcMddReadOffsetLongFlag,
                   OM.MSyntax.kDouble)
    syntax.addFlag(kTdcMddReadCycleFlag, kTdcMddReadCycleLongFlag,
                   OM.MSyntax.kBoolean)
    syntax.addArg(OM.MSyntax.kString)
    syntax.enableQuery(True)
    syntax.enableEdit(True)
    return syntax
    
################################
#
# Plugin Initialization
#
################################

# initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OMPx.MFnPlugin(mobject,"TDChannel", "1.0", "Any")
    try:
        # register node
        mplugin.registerNode(kTdcMddReadNodeName, tdcMddReadId,
                             nodeCreator, nodeInitializer, 
                             OMPx.MPxNode.kDeformerNode )
        # register command
        mplugin.registerCommand(kTdcMddReadCmdName, 
                                tdcMddReadCmdCreator,
                                tdcMddReadSyntaxCreator )
    except:
        sys.stderr.write("Failed to register node: %s\n"%kTdcMddReadNodeName)

# uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( tdcMddReadId )
        mplugin.deregisterCommand( kTdcMddReadCmdName)
    except:
        sys.stderr.write("Failed to unregister node: %s\n"%kTdcMddReadNodeName)

