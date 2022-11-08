#cooldowntimer.py

import time 
import datetime
from usernames import usernames

print(time.time())

def cooldowntimer(user):
    for user in usernames.key():
        if cc == user :
            usernames[cc]["cooldown"] = time.time()
            return usernames[cc]["cooldown"]
    else:
        return  usernames[cc]["cooldown"]



def cooldowntimer2(usrtime):
    if usrtime <= time.time() - 20:
        return true
    else:
        return false
        