import discord
from discord.ext import commands
from discord import app_commands
import time
from .db import init_db

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_load(self):
        await init_db()

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str="No reason"):
        await member.kick(reason=reason)
        await ctx.send(f"{member} kicked. Reason: {reason}")

    @app_commands.command(name="ban", description="Ban a member")
    @app_commands.checks.has_permissions(ban_members=True)
    async def slash_ban(self, interaction: discord.Interaction, member: discord.Member, reason: str="No reason"):
        await member.ban(reason=reason)
        await interaction.response.send_message(f"{member} banned. Reason: {reason}")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
