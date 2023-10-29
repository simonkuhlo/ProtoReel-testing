import json
from tools import console_printer as p

def get_active_client_name():
        p.print_status("info", 4, f"Getting config: active client name")
        with open("res/config.json", "r") as json_file:
                config = json.load(json_file)
                active_client_name = config["used_client"]
                p.print_status("info", 5, f"Got config: client name -> {active_client_name}")
                return(active_client_name)
        
def get_config(key : str, print_log : bool = True):
        if print_log:
                p.print_status("info", 4, f"Getting config: {key}")
        with open("res/config.json", "r") as json_file:
                whole_config = json.load(json_file)
                config_value = whole_config[key]
                if print_log:
                        p.print_status("info", 5, f"Got config: {key} -> {config_value}")
                return(config_value)

def get_adv_config(key : str, print_log : bool = True):
        if print_log:
                p.print_status("info", 4, f"Getting advanced config: {key}")
        with open("res/adv_config.json", "r") as json_file:
                whole_config = json.load(json_file)
                config_value = whole_config[key]
                if print_log:
                        p.print_status("info", 5, f"Got advanced config: {key} -> {config_value}")
                return(config_value)