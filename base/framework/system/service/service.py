#! _*_ encode=utf-8 _*_


'''
    # define system services
    # make system always run
'''

import os, sys, time, datetime
from Log import LogShow


class Service(object):
    def __init__(self):
        self.func_name = "Service"
        
        self.ls = LogShow(self.func_name)
        
    def check_service(self):
        self.ls.log_print("system", "check service now...")

    def check_base(self):
        self.ls.log_print("system", "check base service now...")

    def check_network(self):
        self.ls.log_print("system", "check network service now...")

    def run(self):
        self.ls.log_pring("system", "run system service now ...")
        

        