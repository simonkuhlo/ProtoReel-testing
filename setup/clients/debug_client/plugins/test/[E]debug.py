import discord
from tools import console_printer as p



class clone_cog(discord.commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @discord.commands.Cog.listener() 
    async def on_ready(self):
        p.print_status("info", 1, f"Module {__name__} loaded.")