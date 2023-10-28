import asyncio
import setup_helper.bot_setup as bot_setup
from discord.ext import commands


async def start_bot():   
    active_client = await bot_setup.create_active_client()
    #await bot_setup.load_all_extensions(active_client)
    await active_client.start(active_client.token)


if __name__ == "__main__":
    asyncio.run(start_bot())