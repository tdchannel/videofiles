import sys
import ctypes
import BFD.lib.Runtime as rt

all = [
    'oError',
    'oInfo',
    'iQuery'
    ]

HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
WARNING = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'


#############################################################
#####################################
#
# Windows CRAP
#
#####################################
# {{{ http://code.activestate.com/recipes/496901/ (r3)
# See http://msdn.microsoft.com/library/default.asp?url=/library/en-us/winprog/winprog/windows_api_reference.asp
# for information on Windows APIs.
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12

FOREGROUND_BLUE = 0x0003 # text color contains blue.
FOREGROUND_GREEN= 0x0002 # text color contains green.
FOREGROUND_RED  = 0x0004 # text color contains red.
FOREGROUND_GREY = 0x0007 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.

BACKGROUND_BLUE = 0x10 # background color contains blue.
BACKGROUND_GREEN= 0x20 # background color contains green.
BACKGROUND_RED  = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

std_out_handle = None
if rt.OsTag() == "windows":
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_color(color, handle=std_out_handle):
    """(color) -> BOOL
    
    Example: set_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
    """
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool


#############################################################


def _mkMsg(msg,preStr="",label=None):
    if label:
        return "%s%s: %s"%(preStr,label,msg)
    else:
        return "%s%s"%(preStr,msg)


################
# Status Prints

def oError(msg,preStr="\n",postStr="",label=True):
    if rt.OsTag() == "windows":
        set_color(FOREGROUND_RED)
        if label:
            sys.stdout.write("%s"%_mkMsg(msg,preStr,"ERROR"))
        else:
            sys.stdout.write("%s"%_mkMsg(msg,preStr))
        set_color(FOREGROUND_GREY)
        sys.stdout.write("%s\n"%postStr)
    else:
        if label:
            print "%s%s%s%s"%(RED,_mkMsg(msg,preStr,"ERROR"),ENDC,postStr)
        else:
            print "%s%s%s%s"%(RED,_mkMsg(msg,preStr),ENDC,postStr)

def oInfo(msg,preStr="",postStr="",label=True):
    if rt.OsTag() == "windows":
        set_color(FOREGROUND_GREEN)
        if label:
            sys.stdout.write("%s"%_mkMsg(msg,preStr,"INFO"))
        else:
            sys.stdout.write("%s"%_mkMsg(msg,preStr))
        set_color(FOREGROUND_GREY)
        sys.stdout.write("%s\n"%postStr)
    else:
        if label:
            print "%s%s%s%s"%(GREEN,_mkMsg(msg,preStr,"INFO"),ENDC,postStr)
        else:
            print "%s%s%s%s"%(GREEN,_mkMsg(msg,preStr),ENDC,postStr)


################
# Color Prints
################
def oRed(msg,preStr="",postStr=""):
    if rt.OsTag() == "windows":
        sys.stdout.write("%s"%preStr)
        set_color(FOREGROUND_RED)
        sys.stdout.write("%s"%msg)
        set_color(FOREGROUND_GREY)
        sys.stdout.write("%s\n"%postStr)
    else:
        print "%s%s%s%s%s"%(preStr,RED,msg,ENDC,postStr)

def oGreen(msg,preStr="",postStr=""):
    if rt.OsTag() == "windows":
        sys.stdout.write("%s"%preStr)
        set_color(FOREGROUND_GREEN)
        sys.stdout.write("%s"%msg)
        set_color(FOREGROUND_GREY)
        sys.stdout.write("%s\n"%postStr)
    else:
        print "%s%s%s%s%s"%(preStr,GREEN,msg,ENDC,postStr)


################
# Query
################
def iQuery(msg):
    if rt.OsTag() == "windows":
        set_color(FOREGROUND_BLUE)
        sys.stdout.write("\n%s"%msg)
        set_color(FOREGROUND_GREY)
        retval =  raw_input("")
        return retval
    else:
        return raw_input("%s\n%s%s"%(BLUE,msg,ENDC))


