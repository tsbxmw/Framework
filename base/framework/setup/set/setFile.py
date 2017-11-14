# _*_ coding = utf-8 _*_

import os, time, sys
import json



class SetFile(object):
    def __init__(self):
        self.func_name = "SetFile"
        
        self.localpath = os.path.split(os.path.realpath(__file__))[0]
        self.rootpath =os.path.abspath(os.path.join(self.localpath,"..\\..\\..\\..\\")) + "\\"
        
        sys.path.append(os.path.abspath(os.path.join(self.localpath,"..\\..\\system")))

        self.system_json_path = os.path.abspath(os.path.join(self.localpath,"..\\..\\system\\config\\system.json"))
        from framework_tool import Framework_Tool as FT
        ft = FT()
        self.ls = ft.getLog(self.func_name)
        

    def run(self):
        try:
            self.ls.log_print("system", "--------------------------------------")
            self.ls.log_print("system", "run now...")
            if self.SetSystemFile():
                self.ls.log_print("system", "run over...")
                self.ls.log_print("system", "======================================")
                return True
            else:
                return False
        except Exception, e:        
            self.ls.log_print("error", "Exception " + str(e))

    def SetSystemFile(self):
        func_name_ = "SetSystemFile"
        self.ls.log_print("system", func_name_ + " start now...")
        return True


