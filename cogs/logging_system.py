import discord
from discord.ext import commands

class LoggingSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not message.guild: return
        log = discord.utils.get(message.guild.text_channels, name="logs")
        if log:
            await log.send(f"[Message Deleted] {message.author} in {message.channel.mention}: {message.content}")

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not before.guild: return
        log = discord.utils.get(before.guild.text_channels, name="logs")
        if log:
            await log.send(f"[Message Edited] {before.author} in {before.channel.mention}\nBefore: {before.content}\nAfter: {after.content}")

async def setup(bot):
    await bot.add_cog(LoggingSystem(bot))
