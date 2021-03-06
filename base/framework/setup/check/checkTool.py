# _*_ coding = utf-8 _*_

import os, time, sys

class CheckTool(object):
    def __init__(self):
        
        self.func_name = "CheckTool"
        
        localpath = os.path.split(os.path.realpath(__file__))[0]
        
        sys.path.append(os.path.abspath(os.path.join(localpath,"..\\..\\system")))

        from framework_tool import Framework_Tool as FT
        ft = FT()
        self.ls = ft.getLog(self.func_name)
        
    def run(self):
        self.ls.log_print("system", "--------------------------------------")
        self.ls.log_print("system", "run now...")
        if self.checkTool():
            self.ls.log_print("system", "run over...")
            self.ls.log_print("system", "=====================================")
            return True
        else:
            return False

    def checkTool(self):
        func_name_ = "checkTool"
        self.ls.log_print("system", func_name_ + " start now...")
        if True:          
             return True
        else :
            return False