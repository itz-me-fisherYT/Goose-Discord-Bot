import discord
from discord.ext import commands

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ticket(self, ctx):
        guild = ctx.guild
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.author: discord.PermissionOverwrite(read_messages=True)
        }
        ch = await guild.create_text_channel(f"ticket-{ctx.author.name}", overwrites=overwrites)
        await ch.send("Support will be with you shortly. Staff use !close to close this ticket.")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def close(self, ctx):
        if "ticket" in ctx.channel.name:
            await ctx.channel.delete()
        else:
            await ctx.send("Not a ticket channel.")

async def setup(bot):
    await bot.add_cog(Tickets(bot))
