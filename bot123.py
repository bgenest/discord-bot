#bot123

import time
import datetime
import discord
from discord.ext import commands
from prettytable import PrettyTable
from dotenv import load_dotenv
from random import randint
from rps import rps
import random
from fishing_game import fishing_0, inventory
from usernames import usernames
from library import random_dict_key,randomx,tendies,roasts,whales,replys,tendie_func,rip

load_dotenv()
TOKEN = "NzM4NTY1MjIwMTE2NDYzNjQ3.XyNwdg.mHSRfmYICMOYhd-MCy1x_RZGeu4"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is alive! TESTING')


@client.event
async def on_message(message):
    id = client.get_guild(738564244987052072)

# this tells the bot to ignore its own messages
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

    if '!inv' in message.content.lower():
        message_list = inventory(cc)
        await message.channel.send(message_list[0])
        await message.channel.send(message_list[1])
        await message.channel.send(message_list[2])

    if "tendies pls" in message.content.lower():
        await message.channel.send(tendie_func())
    
    
    if message.author == client.user:
        return
  

    if "quick fish" in message.content.lower():
        message_list = fishing_0(cc)
        await message.channel.send(message_list[0])
        await message.channel.send(message_list[1])
        await message.channel.send(message_list[2])
        await message.channel. send(message_list[3])
        

    for key, value in replys.items():
        if key in message.content.lower():
            await message.channel.send(value)

    if message.content.startswith("!roastsam"):
        await message.channel.send(roasts[randomx(roasts)])
        await message.delete()

    if "whale watching" in message.content.lower():
        await message.channel.send(whales[randomx(whales)]) 


    if "rip" in message.content.lower():
        await message.channel.send(rip(message.content.lower()))

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