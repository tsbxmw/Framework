

import os, sys, time, json

sys.path.append("Log")

from Log.LogShow import LogShow


class Framework_Tool(object):
    def __init__(self):
        pass

    def getLog(self, func_name):
        return LogShow(func_name)

    def log_print(self, func_name, level, logstr):
        self.ls = LogShow(func_name)
        self.ls.log_print(level, logstr)

