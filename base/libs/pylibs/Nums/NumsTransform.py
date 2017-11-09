# _*_ coding: utf-8 _*_

"""
define NumsTransform
"""

import sys
import time
import binascii
from LogShow import LogShow

class NumsTransform(object):
    def __init__(self):
        self.func_name = "NumsTransform"
        self.ls = LogShow(self.func_name)

    def Ox2Ascii(self, data):
        try:
            if data != None:
                data_tmp = hex(str(data))[2:]
                return data_tmp
            else:
                return None
        except Exception, e:
            self.ls.log_print("error", str(e))
            return None

    def Ascii2Ox(self, data):
        try:
            if data != None:
                result = 0
                for tmp in data:
                    result = result * 256 + ord(tmp)
                return result
            else:
                return None
        except Exception, e:
            self.ls.log_print("error", str(e))
            return None


