if __name__ == "__main__":
    import sys
    sys.path.append(".") 
from tools import config_handler
import termcolor

""""
USAGE: 
from tools import console_printer as p
p.print_status("info", 5, f"Hallo")
"""

def print_status(status : str = "info", level : int = 5, message : str = None):
    config = config_handler.get_config("term_formatting")
    log_level = int(config["log_level"])
    if level < log_level:
        return
    current_status = config_handler.get_adv_config("term_formatting_status_codes")[status]
    
    message_head_color = current_status["color"]
    message_head_config = f'pre_{config["status_pre"]}'
    message_head_text = f"[{current_status[message_head_config]}]"
    message_head_colored = termcolor.colored(message_head_text, message_head_color)
    log_level_text = " "
    if config["show_log_level"]:
        log_level_text = f"[{log_level}] => "
        log_level_colored = termcolor.colored(log_level_text, "grey")
        
    finished_message = f"{message_head_colored}{log_level_colored}{message}\n"
    print(finished_message)



if __name__ == "__main__":
    print_status("info", 1,"Hallo Leute")