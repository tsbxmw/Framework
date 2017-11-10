# _*_ coding = utf-8 _*_

import os, time, sys

class CheckEnv(object):
    def __init__(self):
        self.func_name = "CheckEnv"
        localpath = os.path.split(os.path.realpath(__file__))[0]
        
        sys.path.append(os.path.abspath(os.path.join(localpath,"..\\..\\system")))

        from framework_tool import Framework_Tool as FT
        ft = FT()
        self.ls = ft.getLog(self.func_name)
        

    def run(self):
        self.ls.log_print("system", "--------------------------------------")
        self.ls.log_print("system", "run now...")
        if self.checkSystemEnv():

            self.ls.log_print("system", "run over...")
            self.ls.log_print("system", "=====================================")
            return True
        else:
            return False

    def checkSystemEnv(self):
        func_name_ = "checkSystemEnv"
        self.ls.log_print("system", func_name_ + " start now...")
        if self.checkPath("Python"):
            return True
        else :
            return False

    def checkPath(self, name):
        func_name_ = "checkPath"
        path = os.environ.get("PATH")  
        if name in path:
            self.ls.log_print("system", name + " check ok")
            return True
        else:
            self.ls.log_print("system", name + " check fail")
            return False