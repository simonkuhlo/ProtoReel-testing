import json
import os

class Config_handler():
    def __init__(self):
        self.config = self.get_config()
        self.config_override_file = f'setup/clients/{self.config["used_client"]}/config_overrides.json'
        self.config = self.config_overrides(self.config_override_file, self.config)
        self.format_config = self.config["term_formatting"]
        self.adv_config = self.get_adv_config()
        self.statuses = self.adv_config["term_formatting_status_codes"]
        self.log_level = int(self.format_config["log_level"])
        
    def get_config(self):
        with open("res/config.json", "r") as json_file:
            config = json.load(json_file)
        return(config)
    
    def get_adv_config(self):
        with open("res/adv_config.json", "r") as json_file:
            adv_config = json.load(json_file)
        return(adv_config)
    
    def config_overrides(self, override_path, config):
        if os.path.exists(override_path):
            with open(override_path, "r") as json_file: 
                    overrides = json.load(json_file)
                    config_overrides = overrides["config_overrides"]
            config.update(config_overrides)
        return(config)