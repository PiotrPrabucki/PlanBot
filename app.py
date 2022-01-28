from distutils import command
from http import client
import random
import discord
from discord.ext import commands
#variables
client = commands.Bot(command_prefix = "ü")
echoANS = ['Zamknij morde działam przecież', 'AHA.', '?', 'Zabij się','Spierdalaj','who?','starego ci w 5']


@client.event
async def on_ready():
    print('bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send(echoANS[random.randrange(0,len(echoANS))])

client.run('ODI3MTg2OTAxNzE4MjY5OTgy.YGXX1Q.ppZ0-U5NUF6_IJwX1377W7JspWs')