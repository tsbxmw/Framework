# * coding: utf-8 *

''' 
# version : 0.1
# date : 20171107
# author : wei.meng
# function : copy file from path1 to path2
'''

from SFTP import Sftp
import sys, time
from LogShow import LogShow

class FileMove(object):

    def __init__(self):
        self.classname = "FileMove"
        self.ls = LogShow(self.classname)

    def move_one(self, path1, path2):
        try:
            self.ls.log_print("system", "[move] " + str(path1) + " =======> " + str(path2))
            os.system("move /yse \"" + str(path1) + "\" \"" + str(path2) +"\"")
        except Exception, e:
            self.ls.log_print("error", "[move] failed with " + str(e))

    def move_dir(self, path1, path2):
        try:
            self.ls.log_print("system", "[move] " + str(path1) + " =======> " + str(path2))
            os.system("move /yse \"" + str(path1) + "\"* \"" + str(path2) + "\"")
        except Exception, e:
            self.ls.log_print("error", "[move] failed with " + str(e))
