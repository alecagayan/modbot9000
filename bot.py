import discord
import config
from discord.ext import commands
from discord.ext.commands import Bot
import platform
from textblob import TextBlob
import sqlite3
from sqlite3 import connect
import os

intents = discord.Intents.default()
intents.members = True
client = Bot(description='none', command_prefix='?', intents=intents)

client.load_extension("cogs.dm")
client.load_extension("cogs.kickban")
client.load_extension("cogs.welcomer")
client.load_extension("cogs.cooldown")
client.load_extension("cogs.misc")
client.load_extension("cogs.warnings")

@client.event
async def on_ready():

    print("Bot online!\n")
    print("Discord.py API version:", discord.__version__)
    print("Python version:", platform.python_version())
    print("Running on:", platform.system(),
          platform.release(), "(" + os.name + ")")
    print("Name : {}".format(client.user.name))
    print("Client ID : {}".format(client.user.id))
    print("Currently active on " + str(len(client.guilds)) + " server(s).\n")

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over everyone"))

    DB_PATH = "./data/db/database.db"

    db = connect(DB_PATH, check_same_thread=False)
    cur = db.cursor()

    cur.execute('''
            CREATE TABLE IF NOT EXISTS warnings (
            UserID integer,
            WarningCount integer,
            Warnings text
            );''')

    db.commit()
    cur.close()
    db.close()

    print("TABLES SET")


client.run(config.token)
