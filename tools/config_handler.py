if __name__ == "__main__":
    import sys
    sys.path.append(".") 
import json
import os
from tools.console_printer import SP

with open("res/config.json", "r") as json_file:
        config = json.load(json_file)
        
with open("res/adv_config.json", "r") as json_file:
        adv_config = json.load(json_file)

config_override_file = f'setup/clients/{config["used_client"]}/config_overrides.json'

if os.path.exists(config_override_file):
        with open(config_override_file, "r") as json_file: 
                overrides = json.load(json_file)
                config_overrides = overrides["config_overrides"]
                adv_config_overrides = overrides["adv_config_overrides"]
        config.update(config_overrides)
        adv_config.update(adv_config)
        
def get_active_client_name(print_log : bool = True):
        if print_log:
                SP.print_status("info", 4, f"Getting config: active client name")
        active_client_name = config["used_client"]
        if print_log:
                SP.print_status("success", 5, f"Got config: client name -> {SP.highlighted(active_client_name)}")
        return(active_client_name)
        
def get_config(key : str, print_log : bool = True):
        if print_log:
                SP.print_status("info", 4, f"Getting config: {SP.lowlighted(key)}")    
        config_value = config[key]
        if print_log:
                SP.print_status("success", 5, f"Got config: {SP.lowlighted(key)} -> {SP.highlighted(config_value)}")
        return(config_value)

def get_adv_config(key : str, print_log : bool = True):
        if print_log:
                SP.print_status("info", 4, f"Getting advanced config: {key}")
        config_value = adv_config[key]
        if print_log:
                SP.print_status("success", 5, f"Got advanced config: {key} -> {config_value}")
        return(config_value)