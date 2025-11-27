import discord, time
from discord.ext import commands, tasks

class Anti(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.msg_times = {}  # {guild:{user:[timestamps]}}
        self.spam_threshold = 6
        self.spam_window = 6

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or not message.guild:
            return
        # anti-link
        if "http://" in message.content.lower() or "https://" in message.content.lower() or "discord.gg/" in message.content.lower():
            allowed = False
            for role in message.author.roles:
                if role.permissions.manage_messages:
                    allowed = True
            if not allowed:
                try:
                    await message.delete()
                    await message.channel.send(f"{message.author.mention} Links are not allowed.", delete_after=6)
                except Exception:
                    pass
                return

        # anti-spam
        gid = str(message.guild.id)
        uid = str(message.author.id)
        self.msg_times.setdefault(gid, {}).setdefault(uid, [])
        now = time.time()
        self.msg_times[gid][uid].append(now)
        # prune old
        self.msg_times[gid][uid] = [t for t in self.msg_times[gid][uid] if now - t <= self.spam_window]
        if len(self.msg_times[gid][uid]) >= self.spam_threshold:
            try:
                await message.channel.send(f"{message.author.mention} Slow down! You are being rate-limited.", delete_after=6)
            except Exception:
                pass

async def setup(bot):
    await bot.add_cog(Anti(bot))
