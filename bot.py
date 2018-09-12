import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import subprocess
import time
import datetime
import os

bot = commands.Bot('!')

@bot.event
async def on_ready():
        print("Bot is ready!")
   

log = str(489107138711650304)

@bot.event
async def on_member_update(before,after):
        f = open("log.txt", "a+")
        f.write(str(datetime.datetime.now()) + "\n")
        if after.nick != before.nick:
                f.write(str(before) + " has changed nickname from " + str(before.nick) + " to " + str(after.nick) + ".\n")
                await bot.send_message(discord.Object(id=log), str(before) + " has changed nickname from " + str(before.nick) + " to " + str(after.nick) + ".")
        if after.status != before.status:
                f.write(str(before) + "'s status has changed from " + str(before.status) + " to " + str(after.status) + ".\n")
                await bot.send_message(discord.Object(id=log), str(before) + "'s status has changed from " + str(before.status) + " to " + str(after.status) + ".")
        if after.game != before.game:
                if (after.game != None) and (before.game != None):
                        f.write(str(before) + " has stopped playing " + str(before.game) + " and started playing " + str(after.game) + ".\n")
                        await bot.send_message(discord.Object(id=log), str(before) + " has stopped playing " + str(before.game) + " and started playing " + str(after.game) + ".")
                elif (before.game is None) and (after.game != None):
                        f.write(str(before) + " has started playing " + str(after.game) + ".\n")
                        await bot.send_message (discord.Object(id=log), str(before) + " has started playing " + str(after.game) + ".")
                else:
                        f.write(str(before) + " has stopped playing " + str(before.game) + ".\n")
                        await bot.send_message (discord.Object(id=log), str(before) + " has stopped playing " + str(before.game) + ".")

        f.close()

class Main_Commands():
        def __init__(self, bot):
                self.bot = bot


                
bot.run(os.getenv('token'))
