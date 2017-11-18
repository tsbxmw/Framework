# _*_ encode=utf-8 _*_

'''
    # defined Service Network
'''

import os, sys, time, json
from Log import LogShow

class Network(object):
    def __init__(self):
        self.func_name = "Network"
        self.ls = LogShow(self.func_name)

    def HttpServer(self):
        func_name = "HttpSrever"
    
    def TcpServer(self):
        func_name = "TcpServer"

