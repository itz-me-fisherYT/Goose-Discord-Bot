import os, asyncio, json
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = "!"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

INITIAL_COGS = [
    "cogs.moderation",
    "cogs.logging_system",
    "cogs.levels",
    "cogs.tickets",
    "cogs.reaction_roles",
    "cogs.economy",
    "cogs.anti",
    "cogs.welcome",
    "cogs.slash",
    "cogs.backups"
]

@bot.event
async def on_ready():
    print(f"Bot ready: {bot.user} (ID: {bot.user.id})")
    for cog in INITIAL_COGS:
        if cog not in bot.extensions:
            try:
                await bot.load_extension(cog)
                print("Loaded", cog)
            except Exception as e:
                print("Failed to load", cog, e)
    try:
        await bot.tree.sync()
        print("Slash commands synced.")
    except Exception as e:
        print("Failed to sync slash commands:", e)

async def main():
    async with bot:
        await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
