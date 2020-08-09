#cooldowntimer.py

import time 
import datetime
from usernames import usernames
import os
import sys
import ast

def cooldowntimer(cc):
    cooldown = {}
    with open("cooldown.txt") as f:
        contents = f.read()
        cooldown = ast.literal_eval(contents)
        for user,value in cooldown.items():
            if cc == user :
                cooldown[cc] = str(time.time())
                with open("cooldown.txt",'w' ) as f:
                    print(cooldown,file = f)
            return cooldown[cc]
        else:
            return "false"


def cooldowntimer2(cc,wait):
    cooldown = {}
    with open("cooldown.txt" ) as f:
        contents = f.read()
        cooldown = ast.literal_eval(contents)
        for username,usertime in cooldown.items():
            if cc == username:
                usertime = int(float(usertime))
                now = int(float(time.time()))
                if usertime <= int(now - wait):
                    return 'true'
                else:
                    return 'false'