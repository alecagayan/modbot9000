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

        banrole = discord.utils.get(member.guild.roles, name = "Banned")
        cooldownrole = discord.utils.get(member.guild.roles, name = "cooldown")


        with open('./data/json/bans.json') as f:
            data = json.load(f)
        
        for userid in data["banned-members"]:
            try:
                if member.id == userid:
                    await member.add_roles(banrole)

            except:
                pass

        with open('./data/json/cooldown.json') as f:
            data = json.load(f)
        
        for userid in data["cooldown-members"]:
            try:
                if member.id == userid:
                    await member.add_roles(cooldownrole)

            except:
                pass

def setup(bot):
    bot.add_cog(Welcomer(bot))
