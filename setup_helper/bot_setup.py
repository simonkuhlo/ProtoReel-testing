import os
import imp
from tools import config_handler
from tools import console_printer as p

async def create_active_client():
    active_client_name = config_handler.get_active_client_name()
    if os.path.exists(f"setup_helper/clients/{active_client_name}"):
        file, pathname, description = imp.find_module(name="client", path=[f"setup_helper/clients/{active_client_name}"])
        client = imp.load_module("client", file, pathname, description)
    else:
        p.print_status("error", 1, f"Client [{active_client_name}] doesn't exist. Check the config at res/config.json")
        exit()
    active_client = client.Client()
    return active_client
