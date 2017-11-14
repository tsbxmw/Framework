# * coding: utf-8 *

''' 
# version : 0.1
# date : 20171107
# author : wei.meng
# function : read file
'''

from NetWork import Sftp
import sys, time
from Log import LogShow
import xml.etree.cElementTree as ET
import ConfigParser as CP

class FileRead(object):

    def __init__(self):
        self.classname = "FileRead"
        self.ls = LogShow(self.classname)
        self.filetypes = ["json", "xml", "ini", "txt", "other"]

    def check_filetype(self, filetype):
        if filetype in self.filetypes:
            return True
        else:
            return False

    def check_filename(self, filename):
        try:
            if os.path.exists(filename):
                return True
            else:
                return False
        except Exception, e:
            self.ls.log_print("error", "[check_filename] failed with " + str(e))
            return False

    def read(self, filename, filetype):
        try:
            if self.check_filetype(filetype):
                if self.check_filename(filename):
                    if filetype == "json":
                        self.read_json(filename)
                    if filetype == "xml":
                        self.read_xml(filename)
                    if filetype == "ini":
                        self.read_ini(filename)
                    if filetype == "txt":
                        self.read_txt(filename)
                    else:
                        self.read_other(filename)
            else:
                self.ls.log_print("error", "[read] failed with no file type found !")
        except Exception, e:
            self.ls.log_print("error", "[read] failed with " + str(e))



    def read_json(self, filename):
        try:
            f_open = open(filename, "r")
            return json.load(f_open)
            f_open.close()
        except Exception, e:
            self.ls.log_print("error", "[read_json] failed with " + str(e))
            return {}
    
    def read_xml(self, filename):
        try:
            tree = ET.parse(filename)
            return tree
        except Exception, e:
            self.ls.log_print("error", "[read_xml] failed with " + str(e))
            return {}
    
    def read_ini(self, filename):
        try:
            cp = CP.ConfigParser()
            cp.read(filename)
            return cp
        except Exception, e:
            self.ls.log_print("error", "[read_ini] failed with " + str(e))
            return {}
    
    def read_txt(self, filename):
        try:
            f_open = open(filename, "r")
            return f_open.getlines()
            f_open.close()
        except Exception, e:
            self.ls.log_print("error", "[read_txt] failed with " + str(e))
            return {}
    
    def read_other(self, filename):
        try:
            f_open = open(filename, "r")
            return f_open.getlines()
            f_open.close()
        except Exception, e:
            self.ls.log_print("error", "[read_other] failed with " + str(e))
            return {}
