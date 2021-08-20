import discord
from discord.ext import commands
import json
import random

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverlist(self, ctx):
        """List the servers that the bot is active on."""
        x = ', '.join([str(server) for server in self.bot.guilds])
        y = len(self.bot.guilds)
        print("Server list: " + x)
        if y > 40:
            embed = discord.Embed(title="Currently active on " + str(y) + " servers:", description="```json\nCan't display more than 40 servers!```", colour=0xFFD414)
            return await ctx.send(embed=embed)
        elif y < 40:
            embed = discord.Embed(title="Currently active on " + str(y) + " servers:", description="```json\n" + x + "```", colour=0xFFD414)
            return await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        """
        Pings the bot.
        """
        joke = random.choice(["NO FEAR", "MO INTERNET BABEH", "fire it up", "LIGHTNING"])
        ping_msg = await ctx.send("Pinging Server...")
        await ping_msg.edit(content=joke + f" // ***{self.bot.latency*1000:.0f}ms***")

def setup(bot):
    bot.add_cog(Misc(bot))