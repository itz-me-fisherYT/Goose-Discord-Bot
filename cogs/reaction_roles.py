import discord
from discord.ext import commands
from discord.ui import View, Button

class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def createrr(self, ctx, message:str, role:discord.Role):
        """Create a button-role message. Usage: !createrr "Click to get role!" @rolename"""
        btn = Button(label=f"Get {role.name}", style=discord.ButtonStyle.primary)
        async def callback(interaction):
            member = interaction.user
            if role in member.roles:
                await member.remove_roles(role)
                await interaction.response.send_message(f"Removed {role.name}", ephemeral=True)
            else:
                await member.add_roles(role)
                await interaction.response.send_message(f"Added {role.name}", ephemeral=True)
        btn.callback = callback
        view = View()
        view.add_item(btn)
        await ctx.send(message, view=view)

async def setup(bot):
    await bot.add_cog(ReactionRoles(bot))
