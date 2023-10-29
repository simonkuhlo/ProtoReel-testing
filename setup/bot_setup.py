import os
import imp
import discord
from tools import config_handler
from tools import console_printer as p
from tools import dotenv_handler
from setup.helpers import bot_modules as modules

client_path = None

async def create_active_client():
    p.print_status("info", 4, f"Creating active client")
    active_client_name = config_handler.get_active_client_name()
    client_path = f"setup_helper/clients/{active_client_name}"
    p.print_status("info", 4, f"Checking if client path exists")
    if os.path.exists(client_path):
        p.print_status("info", 4, f"Checking for client module")
        file, pathname, description = imp.find_module(name="client", path=[client_path])
        p.print_status("info", 4, f"Loading client module")
        client = imp.load_module("client", file, pathname, description)
        p.print_status("success", 5, f"Loded client module")
    else:
        p.print_status("error", 1, f"Client [{active_client_name}] doesn't exist. Check the config at res/config.json\nPath: {client_path}")
        exit()
    token = dotenv_handler.get_config_token()
    p.print_status("info", 4, f"Instantiating client")
    active_client = client.Client(token)
    await load_all_plugins(active_client)
    p.print_status("success", 5, f"Active client created.")
    return active_client

async def load_all_plugins(client : discord.Client):
    p.print_status("info", 4, f"Loading all modules for: {client}")
    module_dict = await modules.get_modules_by_type("[E]", f"{client_path}/plugins")
    for key in module_dict.keys():
      for module in module_dict[key]:
        module = module[:-3]
        path = f"plugins.{key}.{module}"
        await client.load_extension(path)
