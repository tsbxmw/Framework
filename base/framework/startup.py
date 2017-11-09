# _*_ coding: utf-8 _*_

"""
define Framework start up
"""

import sys
sys.path.append("setup")
from setup.SetUp import SetUp


class startup(object):
    def __init__(self):
        self.setup_ = SetUp()
        pass

    def run(self):
        self.setup_.run()

