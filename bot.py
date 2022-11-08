#bot.py
from cProfile import label
import time
import datetime
import discord
from discord.ext import commands
from prettytable import PrettyTable
from dotenv import load_dotenv
from random import randint
from games.rps import rps
from games.fishing_game import fishing_0, inventory
from usernames import usernames
from scripts.library import random_dict_key,randomx,tendies,roasts,whales,replys,get_drink
from scripts.rando_functions import tendie_func, rip, message_counter_add, message_counter_tell, dicttoprettytable
from scripts.cooldowntimer import cooldowntimer, cooldowntimer2
from scripts.commands import commands

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is alive!')
    import tkinter as tk

    label = tk.Label(
    text="Wordbot Is alive!",
    foreground="#FFFFFF",  # Set the text color to white
    background="#3EB489",
    width = 20,
    height = 10
    )
    label.pack(fill=tk.BOTH,expand=1)

@client.event
async def on_message(message):  # sourcery skip: avoid-builtin-shadow
    id = client.get_guild(463170484373028865)
    cc = str(message.author)

    for x,y in usernames.items():
            if x == cc:
                # this tells the bot to ignore its own messages  \/ \/
                if message.author == client.user:
                    return
                message_counter_add(cc)
            #fishing game - normal speed
                if "cast me" in message.content.lower():
                    if cooldowntimer2(cc,15) != 'true':
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
            #fishing game - quick
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
            #fishing game - inv
                if '!inv' in message.content.lower():
                    message_list = inventory(cc)
                    await message.channel.send(message_list[0])
                    await message.channel.send(message_list[1])
                    await message.channel.send(message_list[2])
            #replys
                for key, value in replys.items():
                    if key in message.content.lower():
                        await message.channel.send(value)
            #roasting sam function
                if message.content.startswith("!roastsam"):
                    await message.channel.send(roasts[randomx(roasts)])
                    await message.delete()
            #whale stuff
                if "whale watching" in message.content.lower():
                    await message.channel.send(whales[randomx(whales)]) 
            #alcohol
                if "gimme a drink, " in message.content.lower():
                    await message.channel.send("Here you go sir:")
                    list = get_drink(message.content.lower())
                    await message.channel.send(list[0])
                    await message.channel.send(list[1])
            #random tendies
                if "tendies pls" in message.content.lower():
                    if cooldowntimer2(cc,10) != 'true':
                        await message.channel.send("you gotta wait...")
                    else:
                        cooldowntimer(cc)
                        await message.channel.send(tendie_func())
            #rip
                if "rip" in message.content.lower():
                    await message.channel.send(rip(message.content.lower()))
            #nighty night
                if "!byebye9900" in message.content.lower():
                    await message.channel.send("I'm going offline. Peace out dood. \n https://imgur.com/8ooVGWv ")
                    await message.delete()
                    exit(69)
                if "!repair" in message.content.lower():
                    await message.channel.send("I'm going offline for repairs. \n https://imgur.com/8ooVGWv ")
                    await message.delete()
                    exit(69)
                if "!morefeatures" in message.content.lower():
                    await message.channel.send("I'm going offline, more features coming. \n https://imgur.com/8ooVGWv ")
                    await message.delete()
                    exit(69)
            #rock paper scissors
                if message.content.startswith("!rock"):
                    if cooldowntimer2(cc,3) != 'true':
                        await message.delete()
                        return
                    else:
                        cooldowntimer(cc)
                    await message.channel.send("ok time for you to lose:")
                    await message.channel.send(rps("rock"))
                if message.content.startswith("!paper"):
                    if cooldowntimer2(cc,3) != 'true':
                        await message.delete()
                        return
                    else:
                        cooldowntimer(cc)
                    await message.channel.send("ok time for you to lose:")
                    await message.channel.send(rps("paper"))
                if message.content.startswith("!scissors"):
                    if cooldowntimer2(cc,3) != 'true':
                        await message.delete()
                        return
                    else:
                        cooldowntimer(cc)
                    await message.channel.send("ok time for you to lose:")
                    await message.channel.send(rps("scissors"))
            #message counter
                if message.content.startswith("!messagecount"):
                    await message.channel.send(message_counter_tell(cc))
            #help function
                if message.content.startswith("!!help"):
                    await message.channel.send("Here's a list of the current available commands:")
                    await message.channel.send(dicttoprettytable(commands))
client.run(TOKEN)
