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

    @commands.command()
    async def perms(self, ctx):
        my_perms: discord.Permissions = ctx.guild.me.guild_permissions
        embed = discord.Embed(title="Bot Permissions", color=0xFFD414)

        if my_perms.manage_roles:
            embed.add_field(name='✅ Manage Roles', value='_ _', inline=True)
        else:
            embed.add_field(name='❌ Manage Roles', value='_ _', inline=True)

        if my_perms.kick_members:
            embed.add_field(name='✅ Kick Members', value='_ _', inline=True)
        else:
            embed.add_field(name='❌ Kick Members', value='_ _', inline=True)
        if my_perms.change_nickname:
            embed.add_field(name='✅ Change Nickname', value='_ _', inline=True)
        else:
            embed.add_field(name='❌ Change Nickname', value='_ _', inline=True)
        if my_perms.read_messages:
            embed.add_field(name='✅ Read Messages', value='_ _', inline=True)
        else:
            embed.add_field(name='❌ Read Messages', value='_ _', inline=True)
        if my_perms.send_messages:
            embed.add_field(name='✅ Send Messages', value='_ _', inline=True)
        else:
            embed.add_field(name='❌ Send Messages', value='_ _', inline=True)
        if my_perms.embed_links:
            embed.add_field(name='✅ Embed Links', value='_ _', inline=True)
        else:
            embed.add_field(name='❌ Embed Links', value='_ _', inline=True)
        if my_perms.attach_files:
            embed.add_field(name='✅ Attach Files', value='_ _', inline=True)
        else:
            embed.add_field(name='❌ Attach Files', value='_ _', inline=True)
        if my_perms.read_message_history:
            embed.add_field(name='✅ Read Message History', value='_ _', inline=True)
        else:
            embed.add_field(name='❌ Read Message History', value='_ _', inline=True)
        if my_perms.add_reactions:
            embed.add_field(name='✅ Add Reactions', value='_ _', inline=True)
        else:
            embed.add_field(name='❌ Add Reactions', value='_ _', inline=True)
        if my_perms.use_external_emojis:
            embed.add_field(name='✅ Use External Emojis', value='_ _', inline=True)
        else:
            embed.add_field(name='❌ Use External Emojis', value='_ _', inline=True)
        if my_perms.connect:
            embed.add_field(name='✅ Connect', value='_ _', inline=True)
        else:
            embed.add_field(name='❌ Connect', value='_ _', inline=True)
        if my_perms.speak:
            embed.add_field(name='✅ Speak', value='_ _', inline=True)
        else:
            embed.add_field(name='❌ Speak', value='_ _', inline=True)
        if my_perms.use_voice_activation:
            embed.add_field(name='✅ Use Voice Activity', value='_ _', inline=True)
        else:
            embed.add_field(name='❌ Use Voice Activity', value='_ _', inline=True)

        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Misc(bot))