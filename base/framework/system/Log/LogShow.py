#! encoding='utf-8'

'''
# LogShow : LogShow()
# description : format the log output 
# date : 20170811
# version : 0.2.0
# author : wei.meng
# m : 20170825 - key -> keys[key]
# m : 20180528 - change to using logging module
'''

import time
import os,sys
import logging

class LogShow(object):

    def __init__(self, logflag):
        self.logflag = logflag
        self.log_set_rank() 
        logging.basicConfig(level = logging.INFO,format = '%(asctime)s %(levelname)s [%(name)s] %(message)s')
        self.logger = logging.getLogger(logflag)

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


    # print log with 'rank' 'funcname' 'self.log_flag'
    def log_print(self, rank, log_str, funcname=None):
        if funcname is None:
            self.log_string = self.log_getsystime() + " [ " + self.logflag + " ] (" + self.log_rank[rank] + ") " + str(log_str)
            self.log_str_temp = log_str
            #print self.log_string
        else:
            self.log_string = self.log_getsystime() + " [ " + self.logflag + " ] (" + self.log_rank[rank] + ") [" + str(funcname) + '] ' + str(log_str)
            self.log_str_temp = '[' + str(funcname) + ']' + log_str
            #print self.log_string
        
        if rank == 'system':
            self.logger.info(self.log_str_temp)
        if rank == 'info':
            self.logger.info(self.log_str_temp)
        if rank == 'debug':
            self.logger.debug(self.log_str_temp)
        if rank == 'error':
            self.logger.error(self.log_str_temp)
        if rank == 'fatal':
            self.logger.fatal(self.log_str_temp)
        if rank == 'warn':
            self.logger.warn(self.log_str_temp)

        #self.log_save_to_file("./log", self.logflag + '.log')
        #self.log_save_to_one_file('./log')

    '''# now, remove the old log_print() function
    def log_print(self, rank, log_str):
        self.log_string = self.log_getsystime() + " [ " + self.logflag + " ] (" + self.log_rank[rank] + ") " + str(log_str)
        print self.log_string
    '''
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