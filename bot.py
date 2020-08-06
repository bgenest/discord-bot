import time
import datetime
import discord
from discord.ext import commands
from prettytable import PrettyTable
from dotenv import load_dotenv
from random import randint
import random

# https://stackoverflow.com/questions/2349991/how-to-import-other-python-files
load_dotenv()
TOKEN = "NzM3ODI5NDM5NTg0NDY5MTEz.XyDDNg.K5Hku-Pec72VcsjcoyjmhsJBXZw"

client = discord.Client()


def randomx(x):
    return randint(0, len(x) - 1)


def random_dict_key(x):
    random = randint(0, len(x) - 1)
    return x[random]


usernames = {"BryGuy#3945" :{"first_name": "bryan" ,"file_path": "C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" , 'file_name': 'fishing_inventory_bryan.txt'},
            "SpeedRt66#4481":{'first_name':"pete","file_path": "C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" , 'file_name': 'fishing_inventory_peter.txt' },
            "Nick#4611":{'first_name':"nick","file_path": "C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" , 'file_name': 'fishing_inventory_nick.txt' },
            "vendrzyk#2835":{'first_name':"sam","file_path": "C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" , 'file_name': 'fishing_inventory_sam.txt' },
            "thirddulig#5481":{'first_name':"victor","file_path": "C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" , 'file_name': 'fishing_inventory_victor.txt' },
}



replys = {}
with open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + "replys.txt") as f:
    for line in f:
        (key, val) = line.split(";")
        replys[key] = val
        val.lower()

f = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'roasts.txt', 'r+')
roasts = [line for line in f.readlines()]

z = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'whales.txt', 'r+')
whales = [line for line in z.readlines()]

k = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'tendies.txt', 'r+')
tendies = [line for line in k.readlines()]



fish_common = {}
with open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + "fishing_common.txt" ) as f:
    for line in f:
        (key, val) = line.split(";")
        fish_common[key] = val
        val.lower()

fish_uncommon = {}
with open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + "fishing_uncommon.txt") as f:
    for line in f:
        (key, val) = line.split(";")
        fish_uncommon[key] = val
        val.lower()

fish_rare = {}
with open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + "fishing_rare.txt") as f:
    for line in f:
        (key, val) = line.split(";")
        fish_rare[key] = val
        val.lower()

fish_rare2 = {}
with open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + "fishing_rare2.txt") as f:
    for line in f:
        (key, val) = line.split(";")
        fish_rare2[key] = val
        val.lower()

@client.event
async def on_ready():
    print(f'{client.user} is alive!')

@client.event
async def on_message(message):
    id = client.get_guild(463170484373028865)

# this tells the bot to ignore its own messages  \/ \/
    cc = str(message.author)
    

    if message.author == client.user:
        return
  #  if c == "vendrzyk":
   #     "oh hey sam, nice to see you"

   # if c == "BryGuy#3945":
    #    await message.channel.send("oh hey bry guy")
# For levels, make commons more rare 

    if "cast me" in message.content.lower():
        await message.channel.send("fishing...")
        await message.channel.send("....")
        tme = randint(1, 4)
        time.sleep(tme)
        fish = randint(1, 899) 
        print(fish)
        for x,y in usernames.items():
            if cc == x :
                v = usernames[cc]["first_name"]
                await message.channel.send(f"{v.title()}'s bobber B o b s...")
        if fish in range(1, 760):
            time.sleep(tme)
            if fish in range(1, 500):
                fish_name, fish_pic = random.choice(list(fish_common.items()))
                await message.channel.send(f"You caught a {fish_name}! {fish_pic}\nRarity: Common.")
            if fish in range(501, 675):
                fish_name, fish_pic = random.choice(list(fish_uncommon.items()))
                await message.channel.send(f"You caught a {fish_name}! {fish_pic}\nRarity: uncommon.")
            if fish in range(675, 740):
                fish_name, fish_pic = random.choice(list(fish_rare.items()))
                await message.channel.send(f"You caught a {fish_name}! {fish_pic}\nRarity: rare!")
            if fish in range(740, 750):
                fish_name, fish_pic = random.choice(list(fish_rare2.items()))
                await message.channel.send(f"You caught a {fish_name}! {fish_pic}\nRarity: extremely ultra rare!")
            for x,y in usernames.items():
                if cc == x:
                    d = open(usernames[cc]["file_path"]  + usernames[cc]["file_name"], "a+" )
                    d.write(f'{fish_name}\n')
        if fish in range(750,760):
            fish_name, fish_pic = random.choice(list(fish_rare2.items()))
            await message.channel.send(f"A {fish_name} bites your hook! but it pulls you into the water..\n Now you're wet, and fishless...\n https://imgur.com/cOZfpMO")
        if fish in range(760,900):
            await message.channel.send('you attempt to reel it in, but the fish gets away....')
        return

    if "quick fish" in message.content.lower():
        await message.channel.send("fishing...")
        await message.channel.send("....")
        fish = randint(1, 899) 
        print(fish)
        for x,y in usernames.items():
            if cc == x :
                v = usernames[cc]["first_name"]
                await message.channel.send(f"{v.title()}'s bobber B o b s...")
        if fish in range(1, 760):
            if fish in range(1, 500):
                fish_name, fish_pic = random.choice(list(fish_common.items()))
                await message.channel.send(f"You caught a {fish_name}! {fish_pic}\nRarity: Common.")
            if fish in range(501, 675):
                fish_name, fish_pic = random.choice(list(fish_uncommon.items()))
                await message.channel.send(f"You caught a {fish_name}! {fish_pic}\nRarity: uncommon.")
            if fish in range(675, 740):
                fish_name, fish_pic = random.choice(list(fish_rare.items()))
                await message.channel.send(f"You caught a {fish_name}! {fish_pic}\nRarity: rare!")
            if fish in range(740, 750):
                fish_name, fish_pic = random.choice(list(fish_rare2.items()))
                await message.channel.send(f"You caught a {fish_name}! {fish_pic}\nRarity: extremely ultra rare!")
            for x,y in usernames.items():
                if cc == x:
                    d = open(usernames[cc]["file_path"]  + usernames[cc]["file_name"], "a+" )
                    d.write(f'{fish_name}\n')
        if fish in range(750,760):
            fish_name, fish_pic = random.choice(list(fish_rare2.items()))
            await message.channel.send(f"A {fish_name} bites your hook! but it pulls you into the water..\n Now you're wet, and fishless...\n https://imgur.com/cOZfpMO")
        if fish in range(760,900):
            await message.channel.send('you attempt to reel it in, but the fish gets away....')
        return

    if message.content.startswith("!inv"):
        await message.channel.send(f"Pulling that up for you...")
        r = str()
        for x, y in usernames.items():
            if cc == x :
                v = usernames[cc]["first_name"]
                await message.channel.send(f"{v.title()}'s inventory")
            for x, y in usernames.items():
                if cc == x:
                    unique_fish = []
                    v = open(usernames[cc]["file_path"]  + usernames[cc]["file_name"], "r+" )
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
        await message.channel.send(table)

    for key, value in replys.items():
        if key in message.content.lower():

            await message.channel.send(value)

    if message.content.startswith("!roastsam"):
        await message.channel.send(roasts[randomx(roasts)])
        await message.delete()

    if "whale watching" in message.content.lower():
        await message.channel.send(whales[randomx(whales)]) 

    if "tendies pls" in message.content.lower():
        num = randint(0, 10)
        print(num)
        if num in range(0, 6):
            await message.channel.send(f"Yes, my son, here are your tendies {tendies[randomx(tendies)]}")
        else:
            await message.channel.send("Not enough good boi points. Mommy said no.")

    if "rip" in message.content.lower():
        user_msg = message.content.lower()
        for x in usernames.values():
            for y in x.values():
                name = y
                if name in user_msg:
                    x = str(datetime.datetime.now())
                    await message.channel.send(f"Rip {name.title()},\n Time of Death: {x[:-7]}")

    if "!night" in message.content.lower():
        await message.channel.send("I'm going offline. Peace out dood. \n https://imgur.com/8ooVGWv ")
        await message.delete()
        exit(69)


client.run(TOKEN)