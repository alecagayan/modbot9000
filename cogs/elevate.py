import discord
from discord.ext import commands
import json


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def elevate(self, ctx, member: discord.Member):
        if ctx.author.id == 401063536618373121:
            with open('./data/json/elevated.json') as f:
                data = json.load(f)

            if member.id not in data["elevated-members"]:

                data["elevated-members"].append(member.id)

                with open('./data/json/elevated.json', 'w') as f:
                    json.dump(data, f)
        
            await ctx.send('ELEVATED')




def setup(bot):
    bot.add_cog(Misc(bot))