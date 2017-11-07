#-*- coding: utf-8 -*-
#!/usr/bin/python 

'''
# version : 1.4
# attention ：using paramiko module --- using 'pip install paramiko' to install the module
# functon : ssh and sftp function
# author : mengwei
# date : 2017.03.01
# modify : -add Sftp module to transport the file
# modify : 2017.03.02 - change the Ssh() to Ssh(ip,user,pass)
# modify : 2017.03.09 - change to the module
# modify : 2017.03.17 - add new function getfile
# modify : 2017.05.25 - add new function Exec_noreturn , try to run the 'reboo' command, but not work fine
'''

import paramiko
import sys
import time
from LogShow import LogShow

class Ssh(object):
    def __init__(self,ipadd,username,password):
        self.ip = ipadd
        self.username = username
        self.password = password
        self.ls = LogShow("SSH")

    def Connect(self):
        try:
            self.connect = paramiko.SSHClient()
            self.connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.connect.connect(self.ip,22,self.username,self.password,timeout=5)
        except Exception,e:
            self.ls.log_print("system","[SSH Connect] : wrong with it -- " + str(e))

    def Exec(self,cmd):
        try:
            self.ls.log_print("system","[exec] " + str(cmd))
            stdin, stdout, stderr = self.connect.exec_command(cmd)
            out = stdout.readlines()
            return out
        except Exception,e:
            self.ls.log_print("system","[SSH Exec] : wrong with it -- " + str(e)   )
    def Exec_noreturn(self,cmd):
        try:
            self.ls.log_print("system", "[exec-noreturn] " + str(cmd))
            stdin, stdout, stderr = self.connect.exec_command(cmd)
        except Exception,e:
            self.ls.log_print("system", "[SSH Exec-noreturn] : wrong with it -- " + str(e))
    
    def Close(self):
        try:
            self.connect.close()
        except Exception,e:
            self.ls.log_print("system", "[SSH Close] : wrong with it -- " + str(e))
