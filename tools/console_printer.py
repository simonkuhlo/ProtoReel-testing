if __name__ == "__main__":
    import sys
    sys.path.append(".") 
    
from tools import config_handler
import termcolor
import datetime
import inspect 
import json
import os

""""
USAGE:  
from tools import console_printer as p
p.print_status("info", 5, f"Hallo")

"""

class Printer():
    def __init__(self):
        self.config = config_handler.get_config("term_formatting", print_log = False)
        print(self.config)
        self.log_level = int(self.config["log_level"])
        self.statuses = config_handler.get_adv_config("term_formatting_status_codes", print_log = False)

    def print_status(self, status : str = "info", level : int = 5, message : str = None):
        if level > self.log_level:
            return
        current_status = self.statuses[status]
        message_head_color = current_status["color"]
        message_head_config = f'pre_{self.config["status_pre"]}'
        message_head_text = f"[{current_status[message_head_config]}]"
        message_head_colored = termcolor.colored(message_head_text, message_head_color)
        
        log_level_colored = ""
        datetime_colored = ""
        calling_module_colored = ""
        
        if self.config["show_log_level"]:
            log_level_text = f"[{level}] "
            log_level_colored = termcolor.colored(log_level_text, "grey")
        
        if self.config["show_time"]:
            current_time = datetime.datetime.now()
            datetime_text = f"[{current_time}]"
            datetime_colored = termcolor.colored(datetime_text, "grey")
        
        if self.config["show_calling_module"]:
            from_stack = inspect.stack()[1]
            module = inspect.getmodule(from_stack[0])
            module_name = module.__name__
            calling_module_text = f"Called by [{module_name}]"
            calling_module_colored = termcolor.colored(calling_module_text, "grey")
        
        finished_message = f"{message_head_colored}{log_level_colored}{datetime_colored}=> {message}\n{calling_module_colored}\n"
        print(finished_message)
        
        #if self.config["write_logs"]:
            #logging.log()

    def highlighted(text : str):
        highlighted_text = termcolor.colored(text, "light_blue", attrs = ["bold"])
        return(highlighted_text)

    def lowlighted(self, text : str):
        highlighted_text = termcolor.colored(text, "grey", attrs = ["bold"])
        return(highlighted_text)


class Config_handler():
    def __init__(self):
        self.config = self.get_config()
        config_override_file = f'setup/clients/{self.config["used_client"]}/config_overrides.json'
        self.config = self.config_overrides(config_override_file, self.config)
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
        
current_config = Config_handler()              

        
if __name__ == "__main__":
    #print(SPrinter.highlighted("Hallo"))
    #SPrinter.print_status("info", 1,"Hallo Leute")
    print("test")