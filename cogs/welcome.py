import discord, os
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        os.makedirs(os.path.join(os.path.dirname(__file__), "..", "data", "welcome"), exist_ok=True)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        ch = discord.utils.get(guild.text_channels, name="welcome")
        if not ch:
            return
        # create simple welcome image
        img = Image.new("RGBA", (800, 250), (30,30,30))
        d = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except Exception:
            font = ImageFont.load_default()
        d.text((20, 30), f"Welcome to {guild.name}", font=font, fill=(255,255,255))
        d.text((20, 100), f"{member.name}#{member.discriminator}", font=font, fill=(200,200,200))
        p = os.path.join(os.path.dirname(__file__), "..", "data", "welcome", f"{member.id}.png")
        img.save(p)
        await ch.send(f"Welcome {member.mention}!", file=discord.File(p))

async def setup(bot):
    await bot.add_cog(Welcome(bot))
