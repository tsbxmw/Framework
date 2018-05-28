# _*_ coding=utf-8 _*_

import os, time, json, sys

class UpdateCase(object):
    def __init__(self):
        localpath = os.path.split(os.path.realpath(__file__))[0]
        
        sys.path.append(os.path.abspath(os.path.join(localpath,"..\\..\\system")))

        from framework_tool import Framework_Tool as FT
        ft = FT()
        self.func_name = "UpdateCase"
        self.ls = ft.getLog(self.func_name)
        

    def run(self):
        self.ls.log_print("system", "--------------------------------------")
        self.ls.log_print("system", "run now...")
        self.ls.log_print("system", "run over...")
        self.ls.log_print("system", "=====================================")


    def UpdateCase(self):
        func_name = "UpdateCase"
        self.ls.log_print("system", "update case now")
        