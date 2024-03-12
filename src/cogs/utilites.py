import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption

class Utilites(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @nextcord.slash_command(description="Sends a list of the bot's commands")
    async def help(self, interaction: Interaction):
                
        embed = nextcord.Embed(
            color=0x7a0608
        )
        embed.add_field(name="", value="No commands... as of now ;)")
        
        await interaction.response.send_message(embed=embed)
        
def setup(bot):
    bot.add_cog(Utilites(bot))