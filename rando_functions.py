import datetime
from random import randint 
from library import tendies
from usernames import usernames
from library import randomx


def rip(message):
        user_msg = message
        for x in usernames.values():
            for y in x.values():
                name = y
                if name in user_msg:
                    x = str(datetime.datetime.now())
                    msg = (f"Rip {name.title()},\n Time of Death: {x[:-7]}")
                else:
                    return "false"
        return msg


def tendie_func():
    num = randint(0,10)
    if num in range(0, 6):
        msg = (f"Yes, my son, here are your tendies {tendies[randomx(tendies)]}")
    else:
        msg = ("Not enough good boi points.")
    return msg