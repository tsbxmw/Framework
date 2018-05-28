# _*_ coding = utf-8 _*_

import os, time, sys

from checkCase import CheckCase
from checkEnv import CheckEnv
from checkCase import CheckCase
from checkFile import CheckFile
from checkModule import CheckModule
from checkOther import CheckOther
from checkTool import CheckTool




class Check(object):
    def __init__(self):
        self.func_name = "Check"

        self.check_case = CheckCase()
        self.check_file = CheckFile()
        self.check_module = CheckModule()
        self.check_other = CheckOther()
        self.check_tool = CheckTool()
        self.check_env = CheckEnv()

        
        localpath = os.path.split(os.path.realpath(__file__))[0]
        
        sys.path.append(os.path.abspath(os.path.join(localpath,"..\\..\\system")))

        from framework_tool import Framework_Tool as FT
        ft = FT()
        self.ls = ft.getLog(self.func_name)
    
    def __str__(self):
        return "Check"

    def run(self):
        self.ls.log_print("system", "--------------------------------------")
        self.ls.log_print("system", "run now...")
        if self.check_file.run():
            pass
        else:
            return False
        if self.check_env.run():
            pass
        else:
            return False
        if self.check_module.run():
            pass
        else:
            return False
        if self.check_other.run():
            pass
        else:
            return False
        if self.check_tool.run():
            pass
        else:
            return False
        if self.check_case.run():
            pass
        else:
            return False
        return True
        self.ls.log_print("system", "=====================================")
