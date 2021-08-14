import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import datetime
import json

class Kickban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        await member.kick(reason = reason)

        if reason is None:
            reason = '_ _'

        embed = discord.Embed(color=0xED4245) #Golden
        embed.add_field(name=member.display_name + '#' + member.discriminator + ' has been kicked!', value='Reason: ' + reason, inline=True)
        embed.set_footer(text='Requested on ' + str(datetime.datetime.now()))
        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member):
        role = discord.utils.get(member.guild.roles, name = "Banned")
        await member.add_roles(role)

        with open('./data/json/bans.json') as f:
            data = json.load(f)

        if member.id not in data["banned-members"]:

            data["banned-members"].append(member.id)

            with open('./data/json/bans.json', 'w') as f:
                json.dump(data, f)

        
        embed = discord.Embed(color=0xED4245) #Red
        embed.add_field(name=member.display_name + '#' + member.discriminator + ' has been banned!', value='_ _', inline=True)
        embed.set_footer(text='Requested on ' + str(datetime.datetime.now()))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: discord.Member):
        role = discord.utils.get(member.guild.roles, name = "Banned")
        await member.remove_roles(role)

        with open('./data/json/bans.json') as f:
            data = json.load(f)
        
        banned_members = data["banned-members"]

        if member.id in data["banned-members"]:
            index = banned_members.index(member.id)

            del banned_members[index]

        data["banned-members"] = banned_members

        with open('./data/json/bans.json', 'w') as f:
            json.dump(data, f)

        
        embed = discord.Embed(color=0x57F287) #Green
        embed.add_field(name=member.display_name + '#' + member.discriminator + ' has been unbanned!', value='_ _', inline=True)
        embed.set_footer(text='Requested on ' + str(datetime.datetime.now()))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Kickban(bot))
