import discord
from tools.console_printer import SP



class readychecker(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @discord.ext.commands.Cog.listener() 
    async def on_ready(self):
        SP.print_status("info", 1, f"Module {SP.lowighted(__name__)} loaded.")

       
async def setup(bot):
    cogs_to_load = [readychecker]
    for cog in cogs_to_load:
        await bot.add_cog(cog(bot))