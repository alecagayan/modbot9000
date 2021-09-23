import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import datetime
import sqlite3
from sqlite3 import connect

class Warnings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, user:discord.Member, *, reason = None):

        if user is not None:
            DB_PATH = "./data/db/database.db"

            db = connect(DB_PATH, check_same_thread=False)
            cur = db.cursor()

            cur.execute(f"SELECT WarningCount FROM warnings WHERE UserID = {user.id}")
            result = cur.fetchone()
            if result is None:
                cur.execute("INSERT INTO warnings(UserID, WarningCount, Warnings) VALUES(?,?,?)", (user.id, 1, reason))
            if result is not None:
                cur.execute("UPDATE warnings SET WarningCount = ? WHERE UserID = ?", ((result[0])+1, user.id))



        embed = discord.Embed(color=0xED4245) #Red
        embed.add_field(name=user.display_name + '#' + user.discriminator + ' has been warned!', value='_ _', inline=True)
        embed.set_footer(text='Requested on ' + str(datetime.datetime.now()))
        await ctx.send(embed=embed)
        db.commit()
        cur.close()
        db.close()

    @commands.command()
    async def warnings(self, ctx):
        DB_PATH = "./data/db/database.db"

        db = connect(DB_PATH, check_same_thread=False)
        cur = db.cursor()

        cur.execute(f"SELECT WarningCount FROM warnings WHERE UserID = {ctx.author.id}")
        warningCount = cur.fetchone()
        cur.execute(f"SELECT Warnings FROM warnings WHERE UserID = {ctx.author.id}")
        warnings = cur.fetchone()
        print(warnings)

        if warningCount is None:
            warningCount = 0
        else:
            warningCount = warningCount[0]

        warnings = list(warnings)
        while len(warnings) < warningCount:
            warnings.append('Reason not provided')

        embed = discord.Embed(color=0xFFD414) #Donut Yellow
        t=0
        while t < warningCount:
            embed.add_field(name='Warning ' + str(t+1) + ': ', value=warnings[t], inline=True)
            t+=1

        print(warnings)

        embed.set_footer(text='Requested on ' + str(datetime.datetime.now()))
        await ctx.send(embed=embed)

        db.commit()
        cur.close()
        db.close()


def setup(bot):
    bot.add_cog(Warnings(bot))
