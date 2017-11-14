# _*_ coding = utf-8 _*_

import os, time, sys
import json



class CheckFile(object):
    def __init__(self):
        self.func_name = "CheckFile"
        
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
            if self.checkSystemFile():
                self.ls.log_print("system", "run over...")
                self.ls.log_print("system", "======================================")
                return True
            else:
                return False
        except Exception, e:        
            self.ls.log_print("error", "Exception " + str(e))

    def checkSystemFile(self):
        func_name_ = "checkSystemFile"
        self.ls.log_print("system", func_name_ + " start now...")
        
        if self.checkIsExists(self.system_json_path):
            pass
        else:
            self.ls.log_print("system", func_name_ + " stop check ")
            sys.exit(1)
        
        f_open = open(self.system_json_path)
        for file_line in json.load(f_open)["check"]["files"]:
            if self.checkIsExists(self.rootpath + file_line):
                continue
            else:               
                self.ls.log_print("system", func_name_ + " failed when check ! ")
                return False
        f_open.close()


        return True



    def checkIsFile(self, filename):
        func_name_ = "checkSystemFile"
        try:
            return os.path.isfile(filename)
        except Exception, e:            
            self.ls.log_print("error", func_name_ + " " + str(e))
            return False
    
    def checkIsExists(self, filename):
        func_name_ = "checkIsExists"
        try:
            if os.path.exists(filename):                
                self.ls.log_print("info", filename + " check ok")
                return True
            else:
                self.ls.log_print("info", filename + " check failed")
                return False
        except Exception, e:            
            self.ls.log_print("error", func_name_ + " " + str(e))
            return False