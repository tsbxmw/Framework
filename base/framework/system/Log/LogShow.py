#! encoding='utf-8'

'''
# LogShow : LogShow()
# description : format the log output 
# date : 20170811
# version : 0.2.0
# author : wei.meng
# m : 20170825 - key -> keys[key]
'''

import time
import os,sys

class LogShow(object):

    def __init__(self, logflag):
        self.logflag = logflag
        self.log_set_rank()

    def log_set_rank(self):
        self.log_rank = {
            "system" : "SYSTEM",
            "debug" : "DEBUG",
            "info" : "INFO", 
            "warn" : "WARN",
            "error" : "ERROR",
            "fatal" : "FATAL"
        }
        self.log_color = {
            "system" : "white",
            "debug" : "yellow",
            "info" : "blue", 
            "warn" : "red",
            "error" : "red",
            "fatal" : "red"
        }
        self.log_level_num = {
            "system" : 5 ,
            "debug"  : 4 ,
            "info"   : 3 ,
            "warn"   : 2 ,
            "error"  : 1 ,
            "fatal"  : 0 ,
        }

    def log_getsystime(self):
        return time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()) )

    def log_print(self, rank, log_str):
        self.log_string = self.log_getsystime() + " [ " + self.logflag + " ] (" + self.log_rank[rank] + ") " + str(log_str)
        print self.log_string

    def log_print_func(self, func_name, rank, log_str):
        log_string = self.log_getsystime() + " [ " + self.logflag + " ] (" + self.log_rank[rank] + ") {" + func_name + "} " + str(log_str)
        print log_string

    def log_print_func_success(self, func_name, rank):
        log_string = self.log_getsystime() + " [ " + self.logflag + " ] (" + self.log_rank[rank] + ") {" + func_name + "} " + str("success !")
        print log_string

    def log_print_func_failed(self, func_name, rank):
        log_string = self.log_getsystime() + " [ " + self.logflag + " ] (" + self.log_rank[rank] + ") {" + func_name + "} " + str("failed !")
        print log_string

    def log_print_color(self, rank, log_str):
        log_string = self.log_getsystime() + " [ " + self.logflag + " ] (" + self.log_rank[rank] + ")" + str(log_str)
        print log_string
        
    def log_print_level(self, level, rank, log_str):
        log_string = self.log_getsystime() + " [ " + level + "-" + rank + " ] (" + self.log_rank[rank] + ")" + str(log_str)

    def log_file_read(self, local, name):
        try:
            if os.path.exists(local + "/" + name):
                files = open(local + "/" + name, "r")
                for line in files.readlines():
                    print line
                files.close()
        except Exception, e:
            print str(e)
            raise e

    def log_save_to_file(self, local, name):
        #print "|--> debug model"
        try:
            files = open(local+ "/" + name, "a")
            files.write(self.log_string)
            files.close()
        except Exception,e:
            print str(e)
            raise e