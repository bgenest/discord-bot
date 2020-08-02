# bot.py
import os
import time
import datetime
import discord
from dotenv import load_dotenv
from random import randint

load_dotenv()
TOKEN = "NzM4NTY1MjIwMTE2NDYzNjQ3.XyNwdg.mHSRfmYICMOYhd-MCy1x_RZGeu4"

client = discord.Client()


def random(x):
    return randint(0, len(x) - 1)


def randomd(x):
    for line in x:


        return


replys = {}
with open("replys.txt") as f:
    for line in f:
        (key, val) = line.split(";")
        replys[key] = val
        val.lower()

f = open('roasts.txt', 'r+')
roasts = [line for line in f.readlines()]

k = open('tendies.txt', 'r+')
tendies = [line for line in k.readlines()]

s = open('fishing_common - Copy.txt', 'r+')
fish_common = [line for line in s.readlines()]

a = open('fishing_uncommon - Copy.txt', 'r+')
fish_uncommon = [line for line in a.readlines()]

b = open('fishing_rare - Copy.txt.txt', 'r+')
fish_rare = [line for line in b.readlines()]

c = open('fishing_rare2 - Copy.txt.txt', 'r+')
fish_rare2 = [line for line in c.readlines()]


@client.event
async def on_ready():
    print(f'{client.user} is alive!')


@client.event
async def on_message(message):
    id = client.get_guild(738564244987052072)

# this tells the bot to ignore its own messages
    cc = str(message.author)

    if message.author == client.user:
        return
  #  if c == "vendrzyk":
   #     "oh hey sam, nice to see you"

   # if c == "BryGuy#3945":
    #    await message.channel.send("oh hey bry guy")

# currently changing the data type of the fish.txt files from list to dictionary

    if "cast me" in message.content.lower():
        await message.channel.send("fishing...")
        await message.channel.send("....")
        tme = randint(1, 1)
        time.sleep(tme)
        fish = randint(1, 900)
        await message.channel.send("Your bobber bobs...")
        if fish in range(1, 750):
            time.sleep(tme)
            if fish in range(1, 400):
                z = fish_common[random(fish_common)]
                await message.channel.send(f"You caught a {z}\nRarity: common.")
                if cc == "BryGuy#3945":
                    d = open('fishing_inventory_bryan.txt', 'a+')
                    d.write(z)
            if fish in range(400, 600):
                z = fish_uncommon[random(fish_uncommon)]
                await message.channel.send(f"You caught a {z}\nRarity: uncommon.")
            if fish in range(601, 724):
                z = fish_rare[random(fish_rare)]
                await message.channel.send(f"You caught a {z}\nRarity: rare!")
            if fish in range(725, 750):
                z = fish_rare2[random(fish_rare2)]
                await message.channel.send(f"You caught a {z}\nRarity: extremely ultra rare!")
        else:
            await message.channel.send('alas, the fish got away.')
        return

    for key, value in replys.items():
        if key in message.content.lower():
            await message.channel.send(value)

    if message.content.startswith("!roastsam"):
        await message.channel.send(roasts[random(roasts)])
        await message.delete()

    if "tendies pls" in message.content.lower():
        num = randint(0, 10)
        print(num)
        if num in range(0, 6):
            await message.channel.send(f"Yes, my son, here are your tendies {tendies[random(tendies)]}")
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
