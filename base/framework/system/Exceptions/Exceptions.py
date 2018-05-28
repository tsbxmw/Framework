# _*_ coding: utf-8 _*_

"""
    # define Exceptions
    # exceptions of io, file, base, system, check, log, network, tool, service
"""
import os, time, json, sys

sys.path.append("Log")
from Log.LogShow import LogShow

class Exceptions(object):
    def __init__(self):
        self.func_name = "Exceptions"
        self.ls = LogShow(self.func_name)

    def show(self,data):
        self.ls.log_print("Exceptions", str(data))

    def exception(self,exception):
        if exception:
            pass
        else:
            pass

class BaseException(object):
    def __init__(self):
        self.func_name = "Exceptions"

    
        