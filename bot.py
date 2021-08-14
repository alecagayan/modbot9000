import discord
import config
from discord.ext import commands
from discord.ext.commands import Bot
import platform
import os

intents = discord.Intents.default()
intents.members = True
client = Bot(description='none', command_prefix='?', intents=intents)

client.load_extension("cogs.dm")
client.load_extension("cogs.kickban")
client.load_extension("cogs.welcomer")



@client.event
async def on_ready():

    print("Bot online!\n")
#    print("Discord.py API version:", discord.__version__)
#    print("Python version:", platform.python_version())
#    print("Running on:", platform.system(), platform.release(), "(" + os.name + ")")
#    print("Name : {}".format(client.user.name))
#    print("Client ID : {}".format(client.user.id))
#    print("Currently active on " + str(len(client.guilds)) + " server(s).\n")
#    logger.info("Bot started successfully.")

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over everyone"))

client.run(config.token)
