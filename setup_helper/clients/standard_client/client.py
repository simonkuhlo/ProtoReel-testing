import discord
from discord.ext import commands
from tools import dotenv_handler

client_command_prefix = commands.when_mentioned_or("!")
client_intents = discord.Intents.all()

class Client(commands.Bot):
    def __init__(self):
        self.token = self.get_token()
        super().__init__(
            command_prefix = client_command_prefix,
            intents = client_intents,
            )
        
    def get_token(self):
        token = dotenv_handler.get_active_client_token()
        return(token)
    
    async def on_ready(self):
        print(f'\n[ Logged on as {self.user}! ]\n')
        #await setup.setup_all_databases(self)
        await self.tree.sync()