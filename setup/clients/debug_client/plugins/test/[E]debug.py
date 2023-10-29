import discord
from tools import console_printer as p



class readychecker(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @discord.ext.commands.Cog.listener() 
    async def on_ready(self):
        p.print_status("info", 1, f"Module {p.lowighted(__name__)} loaded.")

       
async def setup(bot):
    cogs_to_load = [readychecker]
    for cog in cogs_to_load:
        await bot.add_cog(cog(bot))