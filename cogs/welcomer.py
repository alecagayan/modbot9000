import discord
import asyncio
from discord.ext import commands
import json


class Welcomer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):

        print('member')

        role = discord.utils.get(member.guild.roles, name = "Banned")

        with open('./data/json/bans.json') as f:
            data = json.load(f)
        
        for userid in data["banned-members"]:
            try:
                if member.id == userid:
                    await member.add_roles(role)

            except:
                pass

def setup(bot):
    bot.add_cog(Welcomer(bot))
