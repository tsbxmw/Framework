# _*_ coding = utf-8 _*_

import os, time, sys

from updateCase import UpdateCase
from updateEnv import UpdateEnv
from updateCase import UpdateCase
from updateFile import UpdateFile
from updateModule import UpdateModule
from updateOther import UpdateOther
from updateTool import UpdateTool




class Update(object):
    def __init__(self):
        self.func_name = "update"

        self.update_case = UpdateCase()
        self.update_file = UpdateFile()
        self.update_module = UpdateModule()
        self.update_other = UpdateOther()
        self.update_tool = UpdateTool()
        self.update_env = UpdateEnv()

        
        localpath = os.path.split(os.path.realpath(__file__))[0]
        
        sys.path.append(os.path.abspath(os.path.join(localpath,"..\\..\\system")))

        from framework_tool import Framework_Tool as FT
        ft = FT()
        self.ls = ft.getLog(self.func_name)
        

    def run(self):
        self.ls.log_print("system", "--------------------------------------")
        self.ls.log_print("system", "run now...")
        self.update_env.run()
        self.update_file.run()
        self.update_module.run()
        self.update_other.run()
        self.update_tool.run()
        self.update_case.run()
        self.ls.log_print("system", "=====================================")
