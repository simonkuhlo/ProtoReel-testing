import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

client_command_prefix = commands.when_mentioned_or("!")
client_intents = discord.Intents.all()

class Client(commands.Bot):
    def __init__(self):
        #TODO: Change to getting the token from separate file
        #self.token = token
        super().__init__(
            command_prefix = client_command_prefix,
            intents = client_intents,
            )
        
    async def on_ready(self):
        print(f'\n[ Logged on as {self.user}! ]\n')
        #await setup.setup_all_databases(self)
        await self.tree.sync()