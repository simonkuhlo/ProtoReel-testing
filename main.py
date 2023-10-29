import asyncio
import setup.bot_setup as bot_setup
from tools import console_printer as p
from tools import config_handler
from tools import logo_printer

async def start_bot():
    logo_printer.print_logo_1()
    client_name = config_handler.get_active_client_name(print_log = False)
    p.print_status("info", 1, f"Welcome to ProtoReel7. Getting ready. Using {p.highlighted(client_name)}")   
    active_client = await bot_setup.create_active_client()
    #await bot_setup.load_all_extensions(active_client)
    await active_client.start(active_client.token)


if __name__ == "__main__":
    asyncio.run(start_bot()) 