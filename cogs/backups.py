import discord, os, json
from discord.ext import commands, tasks
from datetime import datetime

BACKUP_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "backups")
os.makedirs(BACKUP_DIR, exist_ok=True)

class Backups(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.hourly.start()

    def cog_unload(self):
        self.hourly.cancel()

    @tasks.loop(hours=1.0)
    async def hourly(self):
        for g in self.bot.guilds:
            data = {
                "id": g.id,
                "name": g.name,
                "roles": [{ "id": r.id, "name": r.name, "permissions": r.permissions.value } for r in g.roles],
                "channels": [{ "id": c.id, "name": c.name, "type": str(c.type) } for c in g.channels],
                "timestamp": datetime.utcnow().isoformat()
            }
            path = os.path.join(BACKUP_DIR, f"guild_{g.id}.json")
            with open(path,"w",encoding="utf-8") as f:
                json.dump(data,f,indent=2)
    @hourly.before_loop
    async def before(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(Backups(bot))
