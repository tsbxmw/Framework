# * coding: utf-8 *

''' 
# version : 0.1
# date : 20171107
# author : wei.meng
# function : write file (in fact, the all write to file is same ...)
'''

import sys, time
from Log import LogShow
import xml.etree.cElementTree as ET
import ConfigParser as CP

class FileWrite(object):

    def __init__(self):
        self.classname = "FileWrite"
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
                os.remove(filename)
        except Exception, e:
            self.ls.log_print("error", "[check_filename] failed with " + str(e))

    def write(self, filename, filetype, contents):
        try:
            if self.check_filetype(filetype):
                if self.check_filename(filename):
                    if filetype == "json":
                        self.write_json(filename, contents)
                    if filetype == "xml":
                        self.write_xml(filename, contents)
                    if filetype == "ini":
                        self.write_ini(filename, contents)
                    if filetype == "txt":
                        self.write_txt(filename, contents)
                    else:
                        self.write_other(filename, contents)
            else:
                self.ls.log_print("error", "[write] failed with xxx")
        except Exception, e:
            self.ls.log_print("error", "[write] failed with " + str(e))



    def write_json(self, filename, contents):
        try:
            f_open = open(filename, "w")
            f_open.write(contents)
            f_open.close()
        except Exception, e:
            self.ls.log_print("error", "[write_json] failed with " + str(e))
            return {}
    
    def write_xml(self, filename, contents):
        try:
            f_open = open(filename, "w")
            f_open.write(contents)
            f_open.close()
            return True
        except Exception, e:
            self.ls.log_print("error", "[write_xml] failed with " + str(e))
            return False
    
    def write_ini(self, filename, contents):
        try:
            f_open = open(filename, "w")
            f_open.write(contents)
            f_open.close()
            return True
        except Exception, e:
            self.ls.log_print("error", "[write_ini] failed with " + str(e))
            return False
    
    def write_txt(self, filename, contents):
        try:
            f_open = open(filename, "w")
            f_open.write(contents)
            f_open.close()
            return True
        except Exception, e:
            self.ls.log_print("error", "[write_txt] failed with " + str(e))
            return False
    
    def write_other(self, filename, contents):
        try:
            f_open = open(filename, "w")
            f_open.write(contents)
            f_open.close()
            return True
        except Exception, e:
            self.ls.log_print("error", "[write_other] failed with " + str(e))
            return False
