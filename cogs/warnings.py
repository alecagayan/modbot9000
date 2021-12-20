import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import datetime
import sqlite3
from sqlite3 import connect
import json

class Warnings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def warn(self, ctx, user:discord.Member, *, reason = None):

        with open('./data/json/elevated.json') as f:
            data = json.load(f)

        if ctx.author.id in data["elevated-members"]:

            if reason is None:
                reason = "Reason not provided"

            if user is not None:
                DB_PATH = "./data/db/database.db"

                db = connect(DB_PATH, check_same_thread=False)
                cur = db.cursor()
            

                cur.execute(f"SELECT WarningCount FROM warnings WHERE UserID = {user.id}")
                result = cur.fetchone()
                cur.execute(f"SELECT Warnings FROM warnings WHERE UserID = {user.id}")
                reasons = cur.fetchone()


                if result is None:
                    cur.execute("INSERT INTO warnings(UserID, WarningCount, Warnings) VALUES(?,?,?)", (user.id, 1, reason))
                if result is not None:
                    cur.execute("UPDATE warnings SET WarningCount = ? WHERE UserID = ?", ((result[0])+1, user.id))
                    cur.execute("UPDATE warnings SET Warnings = ? WHERE UserID = ?", ((''.join(reasons)+'|'+reason, user.id)))

                cur.execute(f"SELECT Warnings FROM warnings WHERE UserID = {user.id}")
                updatedreasons = cur.fetchone()


            embed = discord.Embed(color=0xED4245) #Red
            embed.add_field(name=user.display_name + '#' + user.discriminator + ' has been warned!', value='Reason: ' + reason, inline=True)
            embed.set_footer(text='Requested on ' + str(datetime.datetime.now()))
            await ctx.send(embed=embed)
            await user.send(embed=embed)

            db.commit()
            cur.close()
            db.close()

    @commands.command()
    async def warnings(self, ctx, user:discord.Member = None):
        DB_PATH = "./data/db/database.db"

        db = connect(DB_PATH, check_same_thread=False)
        cur = db.cursor()

        if user == None:
            user = ctx.author

        cur.execute(f"SELECT WarningCount FROM warnings WHERE UserID = {user.id}")
        warningCount = cur.fetchone()
        cur.execute(f"SELECT Warnings FROM warnings WHERE UserID = {user.id}")
        warnings = cur.fetchone()

        if warningCount is None:
            warningCount = 0
        else:
            warningCount = warningCount[0]

        warningList = ''.join(warnings).split('|')

        embed = discord.Embed(color=0xFFD414) #Donut Yellow
        t=0
        while t < warningCount:
            embed.add_field(name='Warning ' + str(t+1) + ': ', value=warningList[t], inline=True)
            t+=1

        embed.set_footer(text='Requested on ' + str(datetime.datetime.now()))
        #only send the embed if the user is requesting their own warnings
        if user == ctx.author:
            #dm the user their warnings
            await user.send(embed=embed)
        #if not, check if the user is elevated and send them the embed
        else:
            with open('./data/json/elevated.json') as f:
                data = json.load(f)

            if user.id in data["elevated-members"]:
                await user.send(embed=embed)

        db.commit()
        cur.close()
        db.close()


def setup(bot):
    bot.add_cog(Warnings(bot))
