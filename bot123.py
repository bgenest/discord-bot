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
from library import random_dict_key,randomx,tendies,roasts,whales,replys

# https://stackoverflow.com/questions/2349991/how-to-import-other-python-files
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
        
client.run(TOKEN)