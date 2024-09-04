from distutils import command
from http import client
import random
import discord
from discord.ext import commands
#variables
client = commands.Bot(command_prefix = "ü")
echoANS = ['Zamknij morde działam przecież', 'AHA.', '?', 'Zabij się','who?']


@client.event
async def on_ready():
    print('bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send(echoANS[random.randrange(0,len(echoANS))])

client.run('-----TOKEN------')
