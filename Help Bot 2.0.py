import discord
from discord.ext import commands, tasks
import random
import feedparser

# ----- CONFIG -----
BOT_TOKEN = "DISCORD_BOT_TOKEN_HERE"
DISCORD_CHANNEL_ID = DISCORD_CHANNEL_ID  # Channel to send notifications

# Role pings
ROLE_STREAMS = "<@&STREAMS_ROLE_ID>"  # For testing only (simulate streams)
ROLE_VIDEOS = "<@&VIDEOS_ROLE_ID>"
ROLE_SHORTS = "<@&SHORTS_ROLE_ID>"

# YouTube channel
YOUTUBE_CHANNEL_ID = "YOUTUBE_HANDLE"  # Channel you want to track
RSS_FEED = f"https://www.youtube.com/feeds/videos.xml?channel_id={YOUTUBE_CHANNEL_ID}"

# ----- DISCORD BOT -----
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# ----- QUOTES -----
def load_quotes():
    try:
        with open("quotes.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return ["No quotes found!"]

@bot.command()
@commands.has_permissions(manage_messages=True)
async def addquote(ctx, *, new_quote):
    with open("quotes.txt", "a", encoding="utf-8") as f:
        f.write(new_quote + "\n")
    await ctx.send(f"Quote added!")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def listquotes(ctx):
    quotes = load_quotes()
    if not quotes:
        await ctx.send("No quotes found!")
        return

    embed = discord.Embed(
        title="Quotes List",
        description="Here are all the quotes:",
        color=discord.Color.green()
    )

    for i, quote in enumerate(quotes, start=1):
        embed.add_field(name=f"Quote {i}", value=quote, inline=False)
        if i % 25 == 0:
            await ctx.send(embed=embed)
            embed = discord.Embed(color=discord.Color.green())

    if len(quotes) % 25 != 0:
        await ctx.send(embed=embed)

@bot.command()
async def quote(ctx):
    quotes = load_quotes()
    await ctx.send(random.choice(quotes))

# ----- MODERATION -----
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} has been kicked. Reason: {reason}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} has been banned. Reason: {reason}")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Deleted {amount} messages!", delete_after=5)

@kick.error
@ban.error
@clear.error
async def perm_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to do that!")

# ----- HELP -----
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Bot Commands",
        description="Here are the commands you can use:",
        color=discord.Color.blue()
    )
    embed.add_field(name="!quote", value="Sends a random quote.", inline=False)
    embed.add_field(name="!addquote [text]", value="Adds a new quote to the file. (Mods only)", inline=False)
    embed.add_field(name="!listquotes", value="Lists all quotes. (Mods only)", inline=False)
    embed.add_field(name="!kick @user [reason]", value="Kicks a member. (Kick Members permission required)", inline=False)
    embed.add_field(name="!ban @user [reason]", value="Bans a member. (Ban Members permission required)", inline=False)
    embed.add_field(name="!clear [number]", value="Deletes a number of messages. (Manage Messages permission required)", inline=False)
    embed.add_field(name="!testnotify", value="Simulates stream/video/short notifications.", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
    await ctx.send(embed=embed)

# ----- YOUTUBE RSS NOTIFICATIONS -----
last_video_id = None

@tasks.loop(minutes=5)
async def check_youtube():
    global last_video_id
    feed = feedparser.parse(RSS_FEED)
    if not feed.entries:
        return

    latest = feed.entries[0]
    video_id = latest.yt_videoid
    video_url = latest.link
    title = latest.title

    if video_id == last_video_id:
        return  # Already posted

    last_video_id = video_id
    channel = bot.get_channel(DISCORD_CHANNEL_ID)

    # Detect Shorts
    if '/shorts/' in video_url:
        await channel.send(f"{ROLE_SHORTS} New Short uploaded: {title}\n{video_url}")
    else:
        await channel.send(f"{ROLE_VIDEOS} New Video uploaded: {title}\n{video_url}")

# ----- TEST NOTIFY COMMAND -----
@bot.command()
async def testnotify(ctx):
    """Simulate pings for stream, video, and short"""
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    await channel.send(f"{ROLE_STREAMS} Simulated Stream is now live! Watch here: https://youtu.be/teststream")
    await channel.send(f"{ROLE_VIDEOS} Simulated Video uploaded: Test Video!\nhttps://youtu.be/testvideo")
    await channel.send(f"{ROLE_SHORTS} Simulated Short uploaded: Test Short!\nhttps://youtu.be/testshort")
    await ctx.send("Test notifications sent!")

# ----- ON READY -----
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    check_youtube.start()

# ----- RUN BOT -----
bot.run(BOT_TOKEN)
