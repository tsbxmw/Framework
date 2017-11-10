# _*_ coding = utf-8 _*_

import os, time, sys


class CheckModule(object):
    def __init__(self):
        
        self.func_name = "CheckModule"
        
        localpath = os.path.split(os.path.realpath(__file__))[0]
        
        sys.path.append(os.path.abspath(os.path.join(localpath,"..\\..\\system")))

        from framework_tool import Framework_Tool as FT
        ft = FT()
        self.ls = ft.getLog(self.func_name)

        

    def run(self):
        self.ls.log_print("system", "--------------------------------------")
        self.ls.log_print("system", "run now...")
        if self.checkAllModule():
            self.ls.log_print("system", "run over...")
            self.ls.log_print("system", "=====================================")
            return True
        else:
            return False

        
    def checkAllModule(self):
        func_name_ = "checkSystemEnv"
        self.ls.log_print("system", func_name_ + " start now...")
        if self.checkModule("sys"):            
            return True
        else :
            return False

    def checkModule(self, name):
        func_name_ = "checkPath"
        
        try:
            __import__(name)
            
            self.ls.log_print("system", name + " is installed, check ok")
            return True
        except Exception, e:            
            self.ls.log_print("system", name + " is not installed, check faile")
            return False