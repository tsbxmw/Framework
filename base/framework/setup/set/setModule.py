# _*_ coding = utf-8 _*_

import os, time, sys, json


class SetModule(object):
    def __init__(self):
        
        self.func_name = "SetModule"
        
        self.localpath = os.path.split(os.path.realpath(__file__))[0]
        
        sys.path.append(os.path.abspath(os.path.join(self.localpath,"..\\..\\system")))

        from framework_tool import Framework_Tool as FT
        ft = FT()
        self.ls = ft.getLog(self.func_name)
        self.system_json_path = os.path.abspath(os.path.join(self.localpath,"..\\..\\system\\config\\system.json"))

        

    def run(self):
        self.ls.log_print("system", "--------------------------------------")
        self.ls.log_print("system", "run now...")
        if self.SetAllModule():
            self.ls.log_print("system", "run over...")
            self.ls.log_print("system", "=====================================")
            return True
        else:
            return False

        
    def SetAllModule(self):
        try:
            func_name_ = "SetSystemEnv"
            self.ls.log_print("system", func_name_ + " start now...")
            f_open = open(self.system_json_path)
            for file_line in json.load(f_open)["set"]["module"]:
                if self.SetModule(file_line):  
                    continue
                else:               
                    self.ls.log_print("system", func_name_ + " failed when Set ! ")
                    return False
            f_open.close()
            return True
        except Exception, e:
            self.ls.log_print("error", str(e))

    def SetModule(self, name):
        func_name_ = "SetModule"
        
        try:
            sys.path.append(name)
            self.ls.log_print("system", name + " Set ok")
            return True
        except Exception, e:            
            self.ls.log_print("system", name + " Set failed")
            return False