import random
import time
import discord
import datetime
from discord.ext import commands
from prettytable import PrettyTable
from dotenv import load_dotenv
from random import randint
from usernames import usernames
from scripts.cooldowntimer import cooldowntimer


fish_common = {}
with open("fishing_common.txt" ) as f:
    for line in f:
        (key, val) = line.split(";")
        fish_common[key] = val
        val.lower()

fish_uncommon = {}
with open("fishing_uncommon.txt") as f:
    for line in f:
        (key, val) = line.split(";")
        fish_uncommon[key] = val
        val.lower()

fish_rare = {}
with open("fishing_rare.txt") as f:
    for line in f:
        (key, val) = line.split(";")
        fish_rare[key] = val
        val.lower()

fish_rare2 = {}
with open("fishing_rare2.txt") as f:
    for line in f:
        (key, val) = line.split(";")
        fish_rare2[key] = val
        val.lower()



def fishing_0(cc):
    msg0 = ("fishing...")
    msg1 = ("....")
    fish = randint(1, 1000)
    print(fish)
    for x, y in usernames.items():
        if cc == x :
            v = usernames[cc]["first_name"]
            msg2 = (f"{v.title()}'s bobber B o b s...")
    if fish in range(1, 760):
        if fish in range(1, 500):
            fish_name, fish_pic = random.choice(list(fish_common.items()))
            msg = (f"You caught a {fish_name}! {fish_pic}\nRarity: Common.")
        if fish in range(500, 700):
            fish_name, fish_pic = random.choice(list(fish_uncommon.items()))
            msg = (f"You caught a {fish_name}! {fish_pic}\nRarity: uncommon.")
        if fish in range(700, 740):
            fish_name, fish_pic = random.choice(list(fish_rare.items()))
            msg = (f"You caught a {fish_name}! {fish_pic}\nRarity: rare!")
        if fish in range(740, 750):
            fish_name, fish_pic = random.choice(list(fish_rare2.items()))
            msg = (f"You caught a {fish_name}! {fish_pic}\nRarity: extremely ultra rare!")
        for x,y in usernames.items():
            if cc == x:
                d = open(usernames[cc]["file_name"], "a+" )
                d.write(f'{fish_name}\n')
        return msg0,msg1,msg2,msg
    if fish in range(751,770):
        msg = (f"lol no")
    if fish in range(770,1001):
        msg = ('you attempt to reel it in, but the fish gets away.')
        return msg0,msg1,msg2,msg

def inventory0(cc):
        msg0 = (f"Pulling that up for you...")
        r = str()
        for x, y in usernames.items():
            if cc == x :
                v = usernames[cc]["first_name"]
                msg1 = (f"{v.title()}'s inventory")
            for x, y in usernames.items():
                if cc == x:
                    unique_fish = []
                    v = open(usernames[cc]["file_name"], "r+" )
                    fishing_inventory = [line for line in v.readlines()]
                    fishing_inventory1 = []
                    print(fishing_inventory)
                    for i in fishing_inventory:
                        fishing_inventory1.append(i.strip())
                    set_list = sorted(set(fishing_inventory1))
                    for i in set_list:
                        unique_fish.append(fishing_inventory1.count(i))
                    print(unique_fish)
                    print(set_list)
                    fishing_dict = {}
                    for i in unique_fish:
                        fishing_dict = dict(zip(set_list, unique_fish))
                    table = PrettyTable()
                    table.field_names = ["Fish", "Qty", "Rarity"]
                    for x, y in fishing_dict.items():
                        if x in fish_common.keys():
                            r = "common"
                            table.add_row([x.title(), y, r.title()])
                    for x, y in fishing_dict.items():
                        if x in fish_uncommon.keys():
                            r = "uncommon"
                            table.add_row([x.title(), y, r.title()])
                    for x, y in fishing_dict.items():
                        if x in fish_rare.keys():
                            r = "rare"
                            table.add_row([x.title(), y, r.title()])
                    for x, y in fishing_dict.items():
                        if x in fish_rare2.keys():
                            r = "very rare"
                            table.add_row([x.title(), y, r.title()])
        return msg0,msg1,table