import datetime
from random import randint 
from library import tendies
from usernames import usernames
from library import randomx
import random
import string
import time
from commands import commands
from prettytable import PrettyTable

def rip(message):
        user_msg = message
        message = str(message)
        for x in usernames.values():
            for y in x.values():
                name = y
                name = str(name)
                if name in user_msg.lower():
                    i = str(datetime.datetime.now())
                    return f"Rip {name.title()},\n Time of Death: {i[:-7]}"

def tendie_func():
    num = randint(0,10)
    if num in range(0, 6):
        return f"Yes, my son, here are your tendies {tendies[randomx(tendies)]}"
    else:
        return "Not enough good boi points."


def message_counter_tell(cc):
    return f"{(usernames.get(cc)).get('messagecount')}"


#add 69 and 420 functionality
def message_counter_add(cc):
    usernames[cc]['messagecount'] += 1


def dicttoprettytable(dict):
    table = PrettyTable()
    table.field_names = ["Command", "Function"]
    for x, y in dict.items():
        table.add_row([x.title(), y])

    return table