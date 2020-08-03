import time
import datetime
import discord
from discord.ext import commands
from prettytable import PrettyTable
from dotenv import load_dotenv
from random import randint
import random

load_dotenv()
TOKEN = "NzM3ODI5NDM5NTg0NDY5MTEz.XyDDNg.K5Hku-Pec72VcsjcoyjmhsJBXZw"

client = discord.Client()


def randomx(x):
    return randint(0, len(x) - 1)


def random_dict_key(x):
    random = randint(0, len(x) - 1)
    return x[random]


replys = {}
with open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + "replys.txt") as f:
    for line in f:
        (key, val) = line.split(";")
        replys[key] = val
        val.lower()

f = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'roasts.txt', 'r+')
roasts = [line for line in f.readlines()]

k = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'tendies.txt', 'r+')
tendies = [line for line in k.readlines()]

fish_common = {}
with open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + "fishing_common - Copy.txt" ) as f:
    for line in f:
        (key, val) = line.split(";")
        fish_common[key] = val
        val.lower()

fish_uncommon = {}
with open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + "fishing_uncommon - Copy.txt") as f:
    for line in f:
        (key, val) = line.split(";")
        fish_uncommon[key] = val
        val.lower()

fish_rare = {}
with open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + "fishing_rare - Copy.txt") as f:
    for line in f:
        (key, val) = line.split(";")
        fish_rare[key] = val
        val.lower()

fish_rare2 = {}
with open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + "fishing_rare2 - Copy.txt") as f:
    for line in f:
        (key, val) = line.split(";")
        fish_rare2[key] = val
        val.lower()

@client.event
async def on_ready():
    print(f'{client.user} is alive!')


@client.event
async def on_message(message):
   # 
    id = client.get_guild(463170484373028865)

# this tells the bot to ignore its own messages
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
        tme = randint(1, 1)
        time.sleep(tme)
        fish = randint(1, 900)
        await message.channel.send("Your bobber bobs...")
        if fish in range(1, 750):
            time.sleep(tme)
            if fish in range(1, 500):
                fish_name, fish_pic = random.choice(list(fish_common.items()))
                await message.channel.send(f"You caught a {fish_name}! {fish_pic}\nRarity: common.")
                if cc == "BryGuy#3945":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_bryan.txt', 'a+')
                    d.write(f'{fish_name}\n')
                if cc == "SpeedRt66#4481":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" +'fishing_inventory_peter.txt', 'a+')
                    d.write(f'{fish_name}\n')
                if cc == "Nick#4611":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_nick.txt', 'a+')
                    d.write(f'{fish_name}\n')
                if cc == "vendrzyk#2835":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_sam.txt', 'a+')
                    d.write(f'{fish_name}\n')
                if cc == "thirddulig#5481":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_victor.txt', 'a+')
                    d.write(f'{fish_name}\n')
            if fish in range(501, 700):
                fish_name, fish_pic = random.choice(list(fish_uncommon.items()))
                await message.channel.send(f"You caught a {fish_name}! {fish_pic}\nRarity: uncommon.")
                if cc == "BryGuy#3945":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_bryan.txt', 'a+')
                    d.write(f'{fish_name}\n')
                if cc == "SpeedRt66#4481":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" +'fishing_inventory_peter.txt', 'a+')
                    d.write(f'{fish_name}\n')
                if cc == "Nick#4611":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_nick.txt', 'a+')
                    d.write(f'{fish_name}\n')
                if cc == "vendrzyk#2835":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_sam.txt', 'a+')
                    d.write(f'{fish_name}\n')
                if cc == "thirddulig#5481":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_victor.txt', 'a+')
                    d.write(f'{fish_name}\n')
            if fish in range(701, 740):
                fish_name, fish_pic = random.choice(list(fish_rare.items()))
                await message.channel.send(f"You caught a {fish_name}! {fish_pic}\nRarity: rare!")
                if cc == "BryGuy#3945":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_bryan.txt', 'a+')
                    d.write(f'{fish_name}\n')
                if cc == "SpeedRt66#4481":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" +'fishing_inventory_peter.txt', 'a+')
                    d.write(f'{fish_name}\n')
                if cc == "Nick#4611":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_nick.txt', 'a+')
                    d.write(f'{fish_name}\n')
                if cc == "vendrzyk#2835":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_sam.txt', 'a+')
                    d.write(f'{fish_name}\n')
                if cc == "thirddulig#5481":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_victor.txt', 'a+')
                    d.write(f'{fish_name}\n')
            if fish in range(741, 750):
                fish_name, fish_pic = random.choice(list(fish_rare2.items()))
                await message.channel.send(f"You caught a {fish_name}! {fish_pic}\nRarity: extremely ultra rare!")
                if cc == "BryGuy#3945":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_bryan.txt', 'a+')
                    d.write(f'{fish_name}\n')
                if cc == "SpeedRt66#4481":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" +'fishing_inventory_peter.txt', 'a+')
                    d.write(f'{fish_name}\n')
                if cc == "Nick#4611":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_nick.txt', 'a+')
                    d.write(f'{fish_name}\n')
                if cc == "vendrzyk#2835":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_sam.txt', 'a+')
                    d.write(f'{fish_name}\n')
                if cc == "thirddulig#5481":
                    d = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_victor.txt', 'a+')
                    d.write(f'{fish_name}\n')
        else:
            await message.channel.send('alas, the fish got away.')
        return

    if message.content.startswith("!inv"):
        await message.channel.send(f"Pulling that up for you...")
        if cc == "vendrzyk#2835":
            unique_fish = []
            v = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_sam.txt', 'r+')
            fishing_inventory_sam = [line for line in v.readlines()]
            fishing_inventory_sam1 = []
            print(fishing_inventory_sam)
            for i in fishing_inventory_sam:
                fishing_inventory_sam1.append(i.strip())
            set_list = sorted(set(fishing_inventory_sam1))
            for i in set_list:
                unique_fish.append(fishing_inventory_sam1.count(i))
            print(unique_fish)
            print(set_list)
            await message.channel.send(f"Sam's inventory:")
            fishing_dict = {}
            for i in unique_fish:
                fishing_dict = dict(zip(set_list, unique_fish))
            table = PrettyTable()
            table.field_names = ["Fish", "Qty"]
            for x, y in fishing_dict.items():
                table.add_row([x, y])
            await message.channel.send(table)
        if cc == "BryGuy#3945":
            unique_fish = []
            v = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_bryan.txt', 'r+')
            fishing_inventory_bryan = [line for line in v.readlines()]
            fishing_inventory_bryan1 = []
            print(fishing_inventory_bryan)
            for i in fishing_inventory_bryan:
                fishing_inventory_bryan1.append(i.strip())
            set_list = sorted(set(fishing_inventory_bryan1))
            for i in set_list:
                unique_fish.append(fishing_inventory_bryan1.count(i))
            print(unique_fish)
            print(set_list)
            await message.channel.send(f"Bryan's inventory:")
            fishing_dict = {}
            for i in unique_fish:
                fishing_dict = dict(zip(set_list, unique_fish))
            table = PrettyTable()
            table.field_names = ["Fish", "Qty"]
            for x, y in fishing_dict.items():
                table.add_row([x, y])
            await message.channel.send(table)
        if cc == "SpeedRt66#4481":
            unique_fish = []
            v = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" +'fishing_inventory_peter.txt', 'r+')
            fishing_inventory_peter = [line for line in v.readlines()]
            fishing_inventory_peter1 = []
            print(fishing_inventory_peter)
            for i in fishing_inventory_peter:
                fishing_inventory_peter1.append(i.strip())
            set_list = sorted(set(fishing_inventory_peter1))
            for i in set_list:
                unique_fish.append(fishing_inventory_peter1.count(i))
            print(unique_fish)
            print(set_list)
            await message.channel.send(f"Peter's inventory:")
            fishing_dict = {}
            for i in unique_fish:
                fishing_dict = dict(zip(set_list, unique_fish))
            table = PrettyTable()
            table.field_names = ["Fish", "Qty"]
            for x, y in fishing_dict.items():
                table.add_row([x, y])
            await message.channel.send(table)
        if cc == "Nick#4611":
            unique_fish = []
            v = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_nick.txt', 'r+')
            fishing_inventory_nick = [line for line in v.readlines()]
            fishing_inventory_nick1 = []
            print(fishing_inventory_nick)
            for i in fishing_inventory_nick:
                fishing_inventory_nick1.append(i.strip())
            set_list = sorted(set(fishing_inventory_nick1))
            for i in set_list:
                unique_fish.append(fishing_inventory_nick1.count(i))
            print(unique_fish)
            print(set_list)
            await message.channel.send(f"Nick's inventory:")
            fishing_dict = {}
            for i in unique_fish:
                fishing_dict = dict(zip(set_list, unique_fish))
            table = PrettyTable()
            table.field_names = ["Fish", "Qty"]
            for x, y in fishing_dict.items():
                table.add_row([x, y])
            await message.channel.send(table)

        if cc == "thirddulig#5481":
            unique_fish = []
            v = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_victor.txt', 'r+')
            fishing_inventory_victor = [line for line in v.readlines()]
            fishing_inventory_victor1 = []
            print(fishing_inventory_victor)
            for i in fishing_inventory_victor:
                fishing_inventory_victor1.append(i.strip())
            set_list = sorted(set(fishing_inventory_victor1))
            for i in set_list:
                unique_fish.append(fishing_inventory_victor1.count(i))
            print(unique_fish)
            print(set_list)
            await message.channel.send(f"Victor's inventory:")
            fishing_dict = {}
            for i in unique_fish:
                fishing_dict = dict(zip(set_list, unique_fish))
            table = PrettyTable()
            table.field_names = ["Fish", "Qty"]
            for x, y in fishing_dict.items():
                table.add_row([x, y])
            await message.channel.send(table)

    for key, value in replys.items():
        if key in message.content.lower():

            await message.channel.send(value)

    if message.content.startswith("!roastsam"):
        await message.channel.send(roasts[randomx(roasts)])
        await message.delete()

    if "tendies pls" in message.content.lower():
        num = randint(0, 10)
        print(num)
        if num in range(0, 6):
            await message.channel.send(f"Yes, my son, here are your tendies {tendies[randomx(tendies)]}")
        else:
            await message.channel.send("Not enough good boi points. Mommy said no.")
    if "rip nick" in message.content.lower():
        await message.channel.send(f"Rip Nick Orr,\n Time of Death: {datetime.datetime.now()}")
    if "rip sam" in message.content.lower():
        await message.channel.send(f"Rip Sam Gordon, \n Time of Death: {datetime.datetime.now()}")
    if 'rip victor' in message.content.lower():
        await message.channel.send(f"Rip Victor Dulig,\n Time of Death: {datetime.datetime.now()}")
    if 'rip pete' in message.content.lower():
        await message.channel.send(f"Rip Peter Sands,\n Time of Death: {datetime.datetime.now()}")
    if 'rip bryan' in message.content.lower():
        await message.channel.send(f"Rip Bryan Genest,\n Time of Death: {datetime.datetime.now()}")
    if 'rip bot' in message.content.lower():
        await message.channel.send(f"I am not dead, I am eternal.")

    if "!killme" in message.content.lower():
        await message.channel.send("ok, here you go: https://imgur.com/DtHksfe")

    if "!night" in message.content.lower():
        await message.channel.send("I'm going offline. Peace out dood. \n https://imgur.com/8ooVGWv ")
        await message.delete()
        exit(69)

client.run(TOKEN)