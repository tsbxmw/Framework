##

"""
    # define setup
"""

import os, time, sys, json

sys.path.append("check")
from check.Check import Check
sys.path.append("set")
from set.Set import Set
sys.path.append("update")
from update.Update import Update

class SetUp(object):
    def __init__(self):
        pass
        
    def run(self):
        _check = Check()
        _set = Set()
        _update = Update()

        if _check.run():
            if _set.run():
                pass
            else:
                Exceptions.show()
            if _update.run():
                pass
            else:
                Exceptions.show()
        else:
            print("<<<framework-error>>> failed when check !!!!")

        

    
