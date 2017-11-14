# _*_ coding = utf-8 _*_

import os, time, sys, json

class SetEnv(object):
    def __init__(self):
        self.func_name = "SetEnv"
        self.localpath = os.path.split(os.path.realpath(__file__))[0]
        
        sys.path.append(os.path.abspath(os.path.join(self.localpath,"..\\..\\system")))

        from framework_tool import Framework_Tool as FT
        ft = FT()
        self.ls = ft.getLog(self.func_name)
        self.system_json_path = os.path.abspath(os.path.join(self.localpath,"..\\..\\system\\config\\system.json"))
        

    def run(self):
        self.ls.log_print("system", "--------------------------------------")
        self.ls.log_print("system", "run now...")
        if self.SetSystemEnv():
            self.ls.log_print("system", "run over...")
            self.ls.log_print("system", "=====================================")
            return True
        else:
            return False

    def SetSystemEnv(self):
        try:

            func_name_ = "SetSystemEnv"
            self.ls.log_print("system", func_name_ + " start now...")
            f_open = open(self.system_json_path)
            for file_line in json.load(f_open)["set"]["env"]:
                if self.SetPath("PATH", file_line):  
                    continue
                else:               
                    self.ls.log_print("system", func_name_ + " failed when Set ! ")
                    return False
            f_open.close()
            return True
        except Exception, e:
            self.ls.log_print("error", str(e))


    def SetPath(self, path_name, value):
        func_name_ = "SetPath"
        path = os.environ.get(path_name)  
        if path_name in path:
            self.ls.log_print("system", path_name + " + " + value + " do not need set")
        else:
            os.environ[path_name] = path + ";" + value
            self.ls.log_print("system", path_name + "|" + value + " Set ok")
        return True    