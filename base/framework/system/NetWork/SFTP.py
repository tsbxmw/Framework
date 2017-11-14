#-*- coding: utf-8 -*-
#!/usr/bin/python 


'''
# version : 1.4
# attention ：using paramiko module --- using 'pip install paramiko' to install the module
# functon : sftp function
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
from Log import LogShow

class Sftp(object):
    def __init__(self, ipadd, user, passwd):    
        self.ls = LogShow("SFTP")

    def Connect(self):
        try:            
            self.ip = ipadd    
            self.username = user
            self.password = passwd
            self.ls.log_print("system", "[Sftp connect] " + str(self.ip))
            self.sftp = paramiko.Transport(self.ip,22)
            self.sftp.connect(username=self.username,password=self.password)
            self.sf = paramiko.SFTPClient.from_transport(self.sftp)
        except Exception,e:
            self.ls.log_print("system", "[Sftp connect] : wrong with it -- " + str(e))

    def PutFile(self,localfile,remotefile):
        try:
            self.ls.log_print("system","[Sftp PutFile] : " + str(localfile) + " ====> " + str(remotefile))
            self.sf.put(localfile,remotefile)
            self.ls.log_print("system","[Sftp PutFile] : success")
        except Exception,e:
            self.ls.log_print("system","[Sftp PutFile] : wrong with it -- " + str(e))

    def GetFile(self,remotefile,localfile):
        try:
            self.ls.log_print("system","[Sftp GetFile] : " + str(localfile) + " <==== " + str(remotefile))
            self.sf.get(remotefile,localfile)
            self.ls.log_print("system","[Sftp GetFile] : success")
        except Exception,e:
            self.ls.log_print("system", "[Sftp GetFile] : wrong with -- " + str(e))
            
    def Close(self):
        self.sftp.close()
