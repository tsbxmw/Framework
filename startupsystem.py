# _*_ coding = utf-8 _*_

'''
# define startup system
# test system start function
# run()
'''


import time, os, json, sys
sys.path.append('base/framework')
from startup import startup


if __name__ == "__main__":
    
    sp = startup()
    sp.run()