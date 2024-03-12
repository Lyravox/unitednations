import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption

class Utilites(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
def setup(bot):
    bot.add_cog(Utilites(bot))