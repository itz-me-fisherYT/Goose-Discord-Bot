import discord, os, json, time
from discord.ext import commands

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "levels.json")
if not os.path.exists(DATA):
    with open(DATA,"w") as f: f.write("{}")

def load():
    return json.load(open(DATA,"r"))

def save(d):
    json.dump(d, open(DATA,"w"), indent=4)

class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.data = load()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or not message.guild: return
        gid=str(message.guild.id); uid=str(message.author.id)
        self.data.setdefault(gid, {}).setdefault(uid, {"xp":0,"level":0,"last":0})
        now=time.time()
        if now - self.data[gid][uid].get("last",0) < 30:
            return
        self.data[gid][uid]["last"]=now
        self.data[gid][uid]["xp"] += 10
        lvl=self.data[gid][uid]["level"]
        if self.data[gid][uid]["xp"] >= (lvl+1)*100:
            self.data[gid][uid]["level"] += 1
            await message.channel.send(f"{message.author.mention} leveled up to **{lvl+1}**!")
        save(self.data)

    @commands.command()
    async def level(self, ctx, member:discord.Member=None):
        member = member or ctx.author
        gid=str(ctx.guild.id); uid=str(member.id)
        if gid in self.data and uid in self.data[gid]:
            xp=self.data[gid][uid]["xp"]; lvl=self.data[gid][uid]["level"]
            await ctx.send(f"{member.name} | Level: **{lvl}** XP: **{xp}**")
        else:
            await ctx.send("No data yet.")

async def setup(bot):
    await bot.add_cog(Levels(bot))
