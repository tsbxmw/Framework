##

"""
    # define setup
"""

import os, time, sys, json

sys.path.append("check")
from check.Check import Check
sys.path.append("set")
from set.Set import Set
sys.path.append("update")
from update.Update import Update

class SetUp(object):
    def __init__(self):

        self.func_name = "SetUp"
        
        localpath = os.path.split(os.path.realpath(__file__))[0]
        
        sys.path.append(os.path.abspath(os.path.join(localpath,"..\\system")))

        from framework_tool import Framework_Tool as FT
        ft = FT()
        self.ls = ft.getLog(self.func_name)
        pass
        
    def run(self):
        _check = Check()
        _set = Set()
        _update = Update()

        if _check.run():
            if _set.run():
                pass
            else:
                pass
            if _update.run():
                pass
            else:
                pass
        else:
            self.ls.log_print("error","<<<framework-error>>> failed when check !!!!")

        

    
