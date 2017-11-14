# _*_ coding = utf-8 _*_

import os, time, sys

from .setCase import SetCase
from .setEnv import SetEnv
from .setCase import SetCase
from .setFile import SetFile
from .setModule import SetModule
from .setOther import SetOther
from .setTool import SetTool




class Set(object):
    def __init__(self):
        self.func_name = "Set"

        self.Set_case = SetCase()
        self.Set_file = SetFile()
        self.Set_module = SetModule()
        self.Set_other = SetOther()
        self.Set_tool = SetTool()
        self.Set_env = SetEnv()
        
        localpath = os.path.split(os.path.realpath(__file__))[0]
        
        sys.path.append(os.path.abspath(os.path.join(localpath,"..\\..\\system")))

        from framework_tool import Framework_Tool as FT
        ft = FT()
        self.ls = ft.getLog(self.func_name)
        

    def run(self):
        self.ls.log_print("system", "--------------------------------------")
        self.ls.log_print("system", "run now...")
        if self.Set_file.run():
            pass
        else:
            return False
        if self.Set_env.run():
            pass
        else:
            return False
        if self.Set_module.run():
            pass
        else:
            return False
        if self.Set_other.run():
            pass
        else:
            return False
        if self.Set_tool.run():
            pass
        else:
            return False
        if self.Set_case.run():
            pass
        else:
            return False
        return True
        self.ls.log_print("system", "=====================================")
