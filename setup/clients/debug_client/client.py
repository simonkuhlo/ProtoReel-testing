import discord
from discord.ext import commands
from tools import console_printer as p

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
        p.print_status("success", 1, f'Logged on as {p.highlighted(self.user)}!')
        p.print_status("info", 4, f'Syncing command tree...')
        await self.tree.sync()