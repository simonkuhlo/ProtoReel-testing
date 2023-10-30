import discord
from discord.ext import commands
from tools.console_printer import SP

client_command_prefix = commands.when_mentioned_or("!")
client_intents = discord.Intents.all()

class Client(commands.Bot):
    def __init__(self, token):
        self.token = token
        super().__init__(
            command_prefix = client_command_prefix,
            intents = client_intents,
            )
    
    async def on_ready(self):
        SP.print_status("success", 1, f'Logged on as {self.user}!')
        SP.print_status("info", 4, f'Syncing command tree...')
        await self.tree.sync()