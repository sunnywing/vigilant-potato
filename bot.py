import discord
#from discord.ext.commands import Bot
from discord.ext import commands
#import asyncio
#import subprocess
#import time
#import datetime
import os
import youtube_dl

client = commands.Bot(command_prefix = '.')

players = {}

@client.event
async def on_ready():
        print("Bot is ready!")

@client.command(pass_context=True)
async def join(ctx):
        channel = ctx.message.author.voice.voice_channel
        await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        await voice_client.disconnect()
        
@client.command(pass_context=True)
async def play(ctx, url):
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()

@client.command()
async def ping(ctx):
        await ctx.send('Pong!' + {round(client.latency * 1000)}+'ms')

   

#log = str(489107138711650304)

#@bot.event
#async def on_member_update(before,after):
#        f = open("log.txt", "a+")
#        f.write(str(datetime.datetime.now()) + "\n")
#        if after.nick != before.nick:
#                f.write(str(before) + " has changed nickname from " + str(before.nick) + " to " + str(after.nick) + ".\n")
#                await bot.send_message(discord.Object(id=log), str(before) + " has changed nickname from " + str(before.nick) + " to " + str(after.nick) + ".")
#        if after.status != before.status:
#                f.write(str(before) + "'s status has changed from " + str(before.status) + " to " + str(after.status) + ".\n")
#                await bot.send_message(discord.Object(id=log), str(before) + "'s status has changed from " + str(before.status) + " to " + str(after.status) + ".")
#        if after.game != before.game:
#                if (after.game != None) and (before.game != None):
#                        f.write(str(before) + " has stopped playing " + str(before.game) + " and started playing " + str(after.game) + ".\n")
#                        await bot.send_message(discord.Object(id=log), str(before) + " has stopped playing " + str(before.game) + " and started playing " + str(after.game) + ".")
#                elif (before.game is None) and (after.game != None):
#                        f.write(str(before) + " has started playing " + str(after.game) + ".\n")
#                        await bot.send_message (discord.Object(id=log), str(before) + " has started playing " + str(after.game) + ".")
#                else:
#                        f.write(str(before) + " has stopped playing " + str(before.game) + ".\n")
#                        await bot.send_message (discord.Object(id=log), str(before) + " has stopped playing " + str(before.game) + ".")
#
#        f.close()
#



                
client.run(os.getenv('token'))
