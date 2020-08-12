#bot.py
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
from rando_functions import tendie_func, rip, message_counter_add, message_counter_tell
from cooldowntimer import cooldowntimer, cooldowntimer2

load_dotenv()
TOKEN = "NzM3ODI5NDM5NTg0NDY5MTEz.XyDDNg.K5Hku-Pec72VcsjcoyjmhsJBXZw"

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} is alive!')


@client.event
async def on_message(message):
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
                    await close()
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

client.run(TOKEN)