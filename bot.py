import time
import datetime
import discord
from discord.ext import commands
from prettytable import PrettyTable
from dotenv import load_dotenv
from random import randint
from rps import rps
from fishing_game import fishing_0, inventory
from usernames import usernames
from library import random_dict_key,randomx,tendies,roasts,whales,replys

load_dotenv()
TOKEN = "NzM3ODI5NDM5NTg0NDY5MTEz.XyDDNg.K5Hku-Pec72VcsjcoyjmhsJBXZw"

client = discord.Client()


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
  
    if "cast me" in message.content.lower():
        message_list = fishing_0(cc)
        await message.channel.send(message_list[0])
        await message.channel.send(message_list[1])
        time.sleep(randint(1,3))
        await message.channel.send(message_list[2])
        time.sleep(randint(1,3))
        await message.channel. send(message_list[3])

    if "quick fish" in message.content.lower():
        message_list = fishing_0(cc)
        await message.channel.send(message_list[0])
        await message.channel.send(message_list[1])
        await message.channel.send(message_list[2])
        await message.channel. send(message_list[3])
        

    if '!inv' in message.content.lower():
        message_list = inventory(cc)
        await message.channel.send(message_list[0])
        await message.channel.send(message_list[1])
        await message.channel.send(message_list[2])

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

    if message.content.startswith("!rock"):
        await message.channel.send("ok time for you to lose:")
        await message.channel.send(rps("rock"))
    if message.content.startswith("!paper"):
        await message.channel.send("ok time for you to lose:")
        await message.channel.send(rps("paper"))
    if message.content.startswith("!scissors"):
        await message.channel.send("ok time for you to lose:")
        await message.channel.send(rps("scissors"))

client.run(TOKEN)