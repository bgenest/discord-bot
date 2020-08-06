
import random
import time
import discord
import datetime
from discord.ext import commands
from prettytable import PrettyTable
from dotenv import load_dotenv
from random import randint


client = discord.Client()

@client.event
async def on_message(message):
    id = client.get_guild(738564244987052072)

    def fishing():
        if "cast me" in message.content.lower():
            await message.channel.send("fishing...")
            await message.channel.send("....")
            tme = randint(1, 5)
            time.sleep(tme)
            fish = randint(1, 1000)
            print(fish)
            for x, y in usernames.items():
                if cc == x :
                    v = usernames[cc]["first_name"]
                    await message.channel.send(f"{v.title()}'s bobber B o b s...")
            if fish in range(1, 760):
                time.sleep(tme)
                if fish in range(1, 500):
                    fish_name, fish_pic = random.choice(list(fish_common.items()))
                    await message.channel.send(f"You caught a {fish_name}! {fish_pic}\nRarity: Common.")
                if fish in range(501, 700):
                    fish_name, fish_pic = random.choice(list(fish_uncommon.items()))
                    await message.channel.send(f"You caught a {fish_name}! {fish_pic}\nRarity: uncommon.")
                if fish in range(700, 740):
                    fish_name, fish_pic = random.choice(list(fish_rare.items()))
                    await message.channel.send(f"You caught a {fish_name}! {fish_pic}\nRarity: rare!")
                if fish in range(740, 750):
                    fish_name, fish_pic = random.choice(list(fish_rare2.items()))
                    await message.channel.send(f"You caught a {fish_name}! {fish_pic}\nRarity: extremely ultra rare!")
                for x,y in usernames.items():
                    if cc == x:
                        d = open(usernames[cc]["file_path"]  + usernames[cc]["file_name"], "a+" )
                        d.write(f'{fish_name}\n')
            if fish in range(760,770):
                fish_name, fish_pic = random.choice(list(fish_rare2.items()))
                await message.channel.send(f"A {fish_name} bites your hook! but it pulls you into the water..\n Now you're wet, and fishless...\n https://imgur.com/cOZfpMO")
            if fish in range(770,1000):
                await message.channel.send('you attempt to reel it in, but the fish gets away.')
            return
            if fish in range(1,3):
                for x, y in usernames.items():
                    if cc == x :
                        v = usernames[cc]["first_name"]
                        await message.channel.send(f" A seagull came by and took some of your fish,{v.title()}!")
