# _*_ coding = utf-8 _*_

import os, time, sys




class CheckFile(object):
    def __init__(self):
        self.func_name = "CheckFile"
        
        localpath = os.path.split(os.path.realpath(__file__))[0]
        
        sys.path.append(os.path.abspath(os.path.join(localpath,"..\\..\\system")))

        from framework_tool import Framework_Tool as FT
        ft = FT()
        self.ls = ft.getLog(self.func_name)
        

    def run(self):
        self.ls.log_print("system", "--------------------------------------")
        self.ls.log_print("system", "run now...")
        self.ls.log_print("system", "run over...")
        self.ls.log_print("system", "=====================================")