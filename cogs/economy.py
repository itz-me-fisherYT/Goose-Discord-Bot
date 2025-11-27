import discord, aiosqlite
from discord.ext import commands
from .db import get_db

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def ensure_user(self, guild_id, user_id):
        async with await get_db() as db:
            await db.execute("INSERT OR IGNORE INTO economy(guild_id,user_id,coins) VALUES(?,?,?)",(guild_id,user_id,0))
            await db.commit()

    @commands.command()
    async def bal(self, ctx, member:discord.Member=None):
        member = member or ctx.author
        await self.ensure_user(ctx.guild.id, member.id)
        async with await get_db() as db:
            cur = await db.execute("SELECT coins FROM economy WHERE guild_id=? AND user_id=?",(ctx.guild.id, member.id))
            r = await cur.fetchone()
            await ctx.send(f"{member.display_name} has {r[0]} coins.")

    @commands.command()
    async def daily(self, ctx):
        await self.ensure_user(ctx.guild.id, ctx.author.id)
        async with await get_db() as db:
            await db.execute("UPDATE economy SET coins = coins + 100 WHERE guild_id=? AND user_id=?",(ctx.guild.id, ctx.author.id))
            await db.commit()
            await ctx.send("You collected your daily 100 coins!")

async def setup(bot):
    await bot.add_cog(Economy(bot))
