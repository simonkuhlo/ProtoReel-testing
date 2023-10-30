import asyncio
import setup.bot_setup as bot_setup
from tools.console_printer import SP
from tools import config_handler
from tools import logo_printer

async def start_bot():
    logo_printer.print_logo_1()
    client_name = config_handler.get_active_client_name(print_log = False)
    SP.print_status("info", 1, f"Welcome to ProtoReel7. Getting ready. Using {SP.highlighted(client_name)}")   
    active_client = await bot_setup.main_setup()
    await active_client.start(active_client.token)


if __name__ == "__main__":
    asyncio.run(start_bot()) 