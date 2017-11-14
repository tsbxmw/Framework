# * coding: utf-8 *

''' 
# version : 0.1
# date : 20171107
# author : wei.meng
# function : put file from local to remote
'''


from NetWork import Sftp
import sys, time
from Log import LogShow
from File import FileCopy

class FilePut(object):

    def __init__(self):
        self.classname = "FilePut"
        self.ls = LogShow(self.classname)
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
            self.ls.log_print("system", "start put the files by " + str(servertype))
            if servertype == "SFTP":
                self.SFTPPut(ip, user, password, remote, local)
            if servertype == "SHARE":
                self.SHAREGET(remote, local)
            if servertype == "FTP":
                self.FTPGET(ip, user, password, remote, local)
        else:
            self.ls.log_print("system", "the type of " + servertype + " is not found ")

    def SFTPPUT(self, ip, user, password, remote, local):
        try:
            sftp_connect = Sftp(ip, user, password)
            sftp_connect.Connect()
            sftp_connect.PutFile(local, remote)
        except Exception,e:
            self.ls.log_print("error", "[SFTPGET] failed with " + str(e))

    def SHAREPUT(self, remote, local):
        try:
            fc = FileCopy()
            fc.copy_one(remote, local)
        except Exception,e:
            self.ls.log_print("error", "[SHAREGET] failed with " + str(e))

    # not complete now ...
    def FTPPUT(self, remote, local):
        try:
            None
        except Exception,e:
            self.ls.log_print("error", "[SHAREGET] failed with " + str(e))