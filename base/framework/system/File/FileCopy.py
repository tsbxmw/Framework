# * coding: utf-8 *

''' 
# version : 0.1
# date : 20171107
# author : wei.meng
# function : copy file from path1 to path2
'''

from NetWork import Sftp
import sys, time
from Log import LogShow

class FileCopy(object):

    def __init__(self):
        self.classname = "FileCopy"
        self.ls = LogShow(self.classname)

    def copy_one(self, path1, path2):
        try:
            self.ls.log_print("system", "[copy_one] " + str(path1) + " =======> " + str(path2))
            os.system("copy /yse \"" + str(path1) + "\" \"" + str(path2) +"\"")
        except Exception, e:
            self.ls.log_print("error", "[copy_one] failed with " + str(e))

    def xcopy_one(self, path1, path2):
        try:
            self.ls.log_print("system", "[xcopy_one] " + str(path1) + " =======> " + str(path2))
            os.system("xcopy /yse \"" + str(path1) + "\" \"" + str(path2) + "\"")
        except Exception, e:
            self.ls.log_print("error", "[xcopy_one] failed with " + str(e))

    def copy_dir(self, path1, path2):
        try:
            self.ls.log_print("system", "[copy_dir] " + str(path1) + " =======> " + str(path2))
            os.system("xcopy /yse \"" + str(path1) + "\"* \"" + str(path2) + "\"")
        except Exception, e:
            self.ls.log_print("error", "[copy_dir] failed with " + str(e))


    def xcopy_dir(self, path1, path2):
        try:
            self.ls.log_print("system", "[xcopy_dir] " + str(path1) + " =======> " + str(path2))
            os.system("xcopy /yse \"" + str(path1) + "\"* \"" + str(path2) + "\"")
        except Exception, e:
            self.ls.log_print("error", "[xcopy_dir] failed with " + str(e))