#library 
from random import randint
import datetime
from usernames import usernames
from random import randint
import time
from alcohol import alcohols
import random

def randomx(x):
    return randint(0, len(x) - 1)


def random_dict_key(x):
    random = randint(0, len(x) - 1)
    return x[random]


replys = {}
with open("replys.txt") as f:
    for line in f:
        (key, val) = line.split(";")
        replys[key] = val
        val.lower()

f = open('roasts.txt', 'r+')
roasts = [line for line in f.readlines()]

z = open('whales.txt', 'r+')
whales = [line for line in z.readlines()]

k = open('tendies.txt', 'r+')
tendies = [line for line in k.readlines()]

b = open('alcohol.txt', 'r+')
alcohol = [line for line in b.readlines()]

def rip(message):
        user_msg = message
        for x in usernames.values():
            for y in x.values():
                name = y
                if name in user_msg:
                    x = str(datetime.datetime.now())
                    msg = (f"Rip {name.title()},\n Time of Death: {x[:-7]}")
        return msg
        

def tendie_func():
    num = randint(0,10)
    if num in range(0, 6):
        msg = (f"Yes, my son, here are your tendies {tendies[randomx(tendies)]}")
    else:
        msg = ("Not enough good boi points.")
    return msg


def get_drink(choice):
    for x, y in alcohols.items():
        if x in choice:
            key, val = random.choice(list(y.items()))
            return key.title(), val
