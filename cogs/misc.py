import discord
from discord.ext import commands
import json

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

def setup(bot):
    bot.add_cog(Misc(bot))