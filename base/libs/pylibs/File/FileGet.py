# * coding: utf-8 *

''' 
# version : 0.1
# date : 20171106
# author : wei.meng
# function : get file from network
'''

from SFTP import Sftp
import sys, time
from LogShow import LogShow
from FileCopy import FileCopy
from FileMove import FileMove

class FileGet(object):
    def __init__(self):
        self.ls = LogShow("FileGet")
        self.types = ["SFTP", "SHARE", "FTP"]

    def typecheck(self,servertype):
        if servertype in self.types:
            self.ls.log_print("system", servertype + "check ok")
            return True
        else :
            self.ls.log_print("error", servertype + "check failed")
            return False

    def getfile(self, ip, user, password, remote, local, servertype):
        if self.typecheck(servertype):
            self.ls.log_print("system", "start get the files by " + str(servertype))
            if servertype == "SFTP":
                self.SFTPGET(ip, user, password, remote, local)
            if servertype == "SHARE":
                self.SHAREGET(remote, local)
            if servertype == "FTP":
                self.FTPGET(ip, user, password, remote, local)
        else:
            self.ls.log_print("system", "the type of " + servertype + " is not found ")

    def SFTPGET(self, ip, user, password, remote, local):
        try:
            sftp_connect = Sftp(ip, user, password)
            sftp_connect.Connect()
            sftp_connect.GetFile(remote, local)
        except Exception,e:
            self.ls.log_print("error", "[SFTPGET] failed with " + str(e))

    def SHAREGET(self, remote, local):
        try:
            fc = FileCopy()
            fc.copy_one(remote, local)
        except Exception,e:
            self.ls.log_print("error", "[SHAREGET] failed with " + str(e))

    # not complete now ...
    def FTPGET(self, remote, local):
        try:
            None
        except Exception,e:
            self.ls.log_print("error", "[SHAREGET] failed with " + str(e))