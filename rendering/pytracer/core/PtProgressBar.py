#!/usr/bin/env python
#
#  Corey Goldberg - 2010
#  ascii command-line progress bar with percentage and elapsed time display
# 

import sys
import time
#import ctypes


HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
WARNING = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

STD_OUTPUT_HANDLE= -11
FOREGROUND_BLUE = 0x0003 # text color contains blue.
FOREGROUND_GREEN= 0x0002 # text color contains green.
FOREGROUND_RED  = 0x0006 # text color contains red.
FOREGROUND_GREY = 0x0007 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.

std_out_handle = None
#if rt.OsTag() == "windows":
#    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

WINDOWS_COLORS = {BLUE:FOREGROUND_BLUE,
                  GREEN:FOREGROUND_GREEN,
                  RED:FOREGROUND_RED}

def set_color(color, handle=std_out_handle):
    """(color) -> BOOL
    
    Example: set_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
    """
    bool = False
    #if rt.OsTag() == "windows":
    #    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool


class PtProgressBar:
    def __init__(self, steps, fill_char="#",width=50,color=BLUE):
        self.steps = steps
        self.prog_bar = '[]'
        self.fill_char = fill_char
        self.width = width
        self.color = color
       
    def setValue(self,percent):
        stars = (self.fill_char * max(1, int( (percent/100.0)*self.width) ) )
        spaces= (" "*(self.width-len(stars)))
        self.prog_bar = "[%s] %s%%" % ((stars+spaces),percent)
        if sys.platform.lower().startswith('win'):
            set_color(WINDOWS_COLORS[self.color])
            sys.stdout.write( self.__str__()+'\r')
            set_color(FOREGROUND_GREY)
        else:
            print self, chr(27) + '[A'
        
    def increment(self, newVal):
        percent = int((newVal/float(self.steps))*100)
        self.setValue(percent)
        
    def __str__(self):
        #if rt.OsTag() == "windows":
        #    return "%s"%str(self.prog_bar)
        #else:
        return "%s%s%s"%(self.color,str(self.prog_bar),ENDC)
        
        


if __name__ == '__main__':
    """ example usage """   
    
    #
    # print a dynamic updating progress bar on one line:
    #
    #  [################100%##################]  100%
    #  
    #
    print 'Using increment:'
    steps = 20
    p = ProgressBar(steps)
    for i in range(steps):
        p.increment(i)
        time.sleep(0.1)
    p.setValue(100)
    print '\ndone'

    #
    # Using manual update and all constructor options
    #
    # [=======================================]  100%
    #
    #
    print '\nManual Update:'
    steps = 20
    p = ProgressBar(steps,fill_char="=",width=80,color=RED)
    for i in range(steps):
        percent = int((i/float(steps))*100)
        p.setValue(percent)
        time.sleep(0.1)
    p.setValue(100)
    print '\ndone'
