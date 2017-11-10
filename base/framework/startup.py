# _*_ coding: utf-8 _*_

"""
define Framework start up
"""

import sys, os
sys.path.append("setup")
from setup.SetUp import SetUp


class startup(object):
    def __init__(self):
        self.setup_ = SetUp()
        
        localpath = os.path.split(os.path.realpath(__file__))[0]
        
        sys.path.append(os.path.abspath(os.path.join(localpath,"system")))

        from framework_tool import Framework_Tool as FT
        ft = FT()
        self.ls = ft.getLog(self.func_name)

    def run(self):

        self.setup_.run()

