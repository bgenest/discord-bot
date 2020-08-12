#bot123.py

#epoc, compare times to stored value
import praw
import time
import datetime
import discord
from discord.ext import commands
from prettytable import PrettyTable
from dotenv import load_dotenv
from random import randint
from rps import rps
import random
from fishing_game0 import fishing_0, inventory0
from usernames import usernames
from library import random_dict_key,randomx,tendies,roasts,whales,replys,tendie_func,rip
from cooldowntimer import cooldowntimer, cooldowntimer2
from rando_functions import message_counter_add, message_counter_tell


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


    for x,y in usernames.items():
        if x == cc:
#checks if usrtime <= time.time() - 20, or, user cooldown time is less than or equal to current time minus twenty.
            if message.author == client.user:
                return
            message_counter_add(cc)
            
#fishing game
            if "cast me" in message.content.lower():
                if cooldowntimer2(cc,10) != 'true':
                    await message.delete()
                    return
                else:
                    cooldowntimer(cc)
                    
                    message_list = fishing_0(cc)
                    await message.channel.send(message_list[0])
                    await message.channel.send(message_list[1])
                    time.sleep(randint(1,3))
                    await message.channel.send(message_list[2])
                    time.sleep(randint(1,3))
                    await message.channel. send(message_list[3])
#inventory
            if '!inv' in message.content.lower():
                message_list = inventory0(cc)
                await message.channel.send(message_list[0])
                await message.channel.send(message_list[1])
                await message.channel.send(message_list[2])
#tendies
            if "tendies pls" in message.content.lower():
                if cooldowntimer2(cc,10) != 'true':
                    await message.channel.send("you gotta wait...")
                else:
                    cooldowntimer(cc)
                    await message.channel.send(tendie_func())
#quick cast
            if "quick cast" in message.content.lower():
                if cooldowntimer2(cc,10) != 'true':
                    await message.delete()
                    return
                else:
                    cooldowntimer(cc)
                    message_list = fishing_0(cc)
                    await message.channel.send(message_list[0])
                    await message.channel.send(message_list[1])
                    await message.channel.send(message_list[2])
                    await message.channel. send(message_list[3])
#reply
            for key, value in replys.items():
                if key in message.content.lower():
                    await message.channel.send(value)
#roastsam
            if message.content.startswith("!roastsam"):
                await message.channel.send(roasts[randomx(roasts)])
                await message.delete()
#Whale
            if "whale watching" in message.content.lower():
                await message.channel.send(whales[randomx(whales)]) 
#rip
            if "rip" in message.content.lower():
                await message.channel.send(rip(message.content.lower()))
#off
            if "!159753" in message.content.lower():
                await message.channel.send("I'm going offline. Peace out dood. \n https://imgur.com/8ooVGWv ")
                await message.delete()
                exit(69)
#rock paper scissors
            if message.content.startswith("!rock"):
                await message.channel.send("ok time for you to lose:")
                await message.channel.send(rps("rock"))
            if message.content.startswith("!paper"):
                await message.channel.send("ok time for you to lose:")
                await message.channel.send(rps("paper"))
            if message.content.startswith("!scissors"):
                await message.channel.send("ok time for you to lose:")
                await message.channel.send(rps("scissors"))
            #message counting per user call
            if message.content.startswith("!messagecount"):
                await message.channel.send(message_counter_tell(cc))
            
client.run(TOKEN)