if __name__ == "__main__":
    import sys
    sys.path.append(".") 
    
import termcolor
import datetime
import inspect

from tools.printer_ext import get_configs
from tools.printer_ext import logging


""""
USAGE:  
from tools import console_printer as p
p.print_status("info", 5, f"Hallo")

"""

class Printer():
    def __init__(self):
        self.config_handler = get_configs.Config_handler()
        self.logging = logging.Logfile_writer()
        self.config = self.config_handler.config
        self.config = self.config_handler.format_config
        self.log_level = self.config_handler.log_level
        self.statuses = self.config_handler.statuses

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

        current_time = datetime.datetime.now()
        if self.config["show_time"]:
            datetime_text = f"[{current_time}]"
            datetime_colored = termcolor.colored(datetime_text, "grey")
            
        from_stack = inspect.stack()[1]
        module = inspect.getmodule(from_stack[0])
        module_name = module.__name__
        if self.config["show_calling_module"]:
            calling_module_text = f"Called by [{module_name}]"
            calling_module_colored = termcolor.colored(calling_module_text, "grey")
        
        finished_message = f"{message_head_colored}{log_level_colored}{datetime_colored}=> {message}\n{calling_module_colored}\n"
        print(finished_message)
        
        if self.config["write_logs"]:
            
            self.logging.log(message = message, status_code = status, time = current_time, call_source = module_name)

    def highlighted(self, text : str):
        highlighted_text = termcolor.colored(text, "light_blue", attrs = ["bold"])
        return(highlighted_text)

    def lowlighted(self, text : str):
        highlighted_text = termcolor.colored(text, "grey", attrs = ["bold"])
        return(highlighted_text)
        
SP = Printer()              

        
if __name__ == "__main__":
    print(SP.highlighted(text="Hallo"))
    SP.print_status("info", 1,"Hallo Leute")