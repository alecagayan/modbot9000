import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import datetime
import json

class Cooldown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def cooldown(self, ctx, member: discord.Member):
        role = discord.utils.get(member.guild.roles, name = "cooldown")
        await member.add_roles(role)

        with open('./data/json/cooldown.json') as f:
            data = json.load(f)

        if member.id not in data["cooldown-members"]:

            data["cooldown-members"].append(member.id)

            with open('./data/json/cooldown.json', 'w') as f:
                json.dump(data, f)

        
        embed = discord.Embed(color=0xED4245) #Red
        embed.add_field(name=member.display_name + '#' + member.discriminator + ' has been given the cooldown role!', value='_ _', inline=True)
        embed.set_footer(text='Requested on ' + str(datetime.datetime.now()))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def endcooldown(self, ctx, member: discord.Member):
        role = discord.utils.get(member.guild.roles, name = "cooldown")
        await member.remove_roles(role)

        with open('./data/json/cooldown.json') as f:
            data = json.load(f)
        
        cooldown_members = data["cooldown-members"]

        if member.id in data["cooldown-members"]:
            index = cooldown_members.index(member.id)

            del cooldown_members[index]

        data["cooldown-members"] = cooldown_members

        with open('./data/json/cooldown.json', 'w') as f:
            json.dump(data, f)

        
        embed = discord.Embed(color=0x57F287) #Green
        embed.add_field(name=member.display_name + '#' + member.discriminator + ' has been removed from cooldown!', value='_ _', inline=True)
        embed.set_footer(text='Requested on ' + str(datetime.datetime.now()))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Cooldown(bot))
