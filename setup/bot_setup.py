import os
import imp
import discord
from tools import config_handler
from tools import console_printer as p
from tools import dotenv_handler
from setup.helpers import bot_modules as modules

client_path = None

async def main_setup():
    p.print_status("info", 4, f"Creating active client")
    active_client = await create_active_client
    await load_all_plugins(active_client)
    p.print_status("success", 5, f"Active client created.")
    return active_client
    
async def create_active_client():  
    active_client_name = config_handler.get_active_client_name()
    global client_path
    client_path = f"setup/clients/{active_client_name}"
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
    return active_client

async def load_all_plugins(client : discord.Client):
    plugin_path = f"{client_path}/plugins"
    p.print_status("info", 4, f"Loading all bot Plugins")
    module_dict = await modules.get_modules_by_type("[E]", plugin_path)
    
    for key in module_dict.keys():
      for module in module_dict[key]:
        module = module[:-3]
        path = f"{plugin_path.replace('/','.')}.{key}.{module}"
        await client.load_extension(path)
