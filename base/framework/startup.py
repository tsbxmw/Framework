# _*_ coding: utf-8 _*_

"""
define Framework start up
this is the startup() function define and test
using run() function to startup all the framework system
"""

import sys, os
sys.path.append("setup")
from setup.SetUp import SetUp


class startup(object):
    def __init__(self):
        self.func_name = "startup"
        self.setup_ = SetUp()
        
        localpath = os.path.split(os.path.realpath(__file__))[0]
        
        sys.path.append(os.path.abspath(os.path.join(localpath,"system")))
        from framework_tool import Framework_Tool as FT
        ft = FT()
        self.ls = ft.getLog(self.func_name)

    def run(self):
        self.setup_.run()
   
if __name__ == "__main__":
    print("[startup] DEBUG this is local test in startup at Framework")
    startup = startup()
    startup.run()
    print("[startup] DEBUG running now ...")
        

