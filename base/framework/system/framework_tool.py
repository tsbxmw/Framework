

import os, sys, time, json

sys.path.append("Log")

from Log.LogShow import LogShow
from Exceptions.Exceptions import Exceptions

from File.FileCopy import FileCopy
from File.FileGet import FileGet
from File.FileMove import FileMove
from File.FilePut import FilePut
from File.FileRead import FileRead
from File.FileWrite import FileWrite

from NetWork.SFTP import Sftp
from NetWork.SSH import Ssh
from service.service import Service

from tools.tools import Tools



class Framework_Tool(object):
    def __init__(self):
        pass

    def getLog(self, func_name):
        return LogShow(func_name)

    def getExceptions(self):
        return Exceptions()

    def getFileCopy(self):
        return FileCopy()
    
    def getFileGet(self):
        return FileGet()

    def getFileMove(self):
        return FileMove()

    def getFilePut(self):
        return FilePut()

    def getFileRead(self):
        return FileRead()

    def getFileWrite(self):
        return FileWrite()

    def getService(self):
        return Service()

    def getSftp(self, ip, user, passwd):
        return Sftp(ip, user, passwd)

    def getSsh(self, ip, user, passwd):
        return Ssh(ip, user, passwd)

    def log_print(self, func_name, level, logstr):
        self.ls = LogShow(func_name)
        self.ls.log_print(level, logstr)

