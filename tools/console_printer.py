if __name__ == "__main__":
    import sys
    sys.path.append(".") 
from tools import config_handler
import termcolor
import datetime
import inspect 

""""
USAGE: 
from tools import console_printer as p
p.print_status("info", 5, f"Hallo")

"""

config = None
log_level = None
statuses = None
logfile = None 

def startup():
    global config
    global log_level
    global statuses
    config = config_handler.get_config("term_formatting", print_log = False)
    log_level = int(config["log_level"])
    statuses = config_handler.get_adv_config("term_formatting_status_codes", print_log = False)
    if config["write_logs"]:
        global logfile
        logfile = create_logfile("Gernal-Purpose")


def print_status(status : str = "info", level : int = 5, message : str = None):
    if not config:
        startup()
    if level > log_level:
        return
    current_status = statuses[status]
    message_head_color = current_status["color"]
    message_head_config = f'pre_{config["status_pre"]}'
    message_head_text = f"[{current_status[message_head_config]}]"
    message_head_colored = termcolor.colored(message_head_text, message_head_color)
    
    log_level_colored = ""
    datetime_colored = ""
    calling_module_colored = ""
    
    if config["show_log_level"]:
        log_level_text = f"[{level}] "
        log_level_colored = termcolor.colored(log_level_text, "grey")
    
    if config["show_time"]:
        current_time = datetime.datetime.now()
        datetime_text = f"[{current_time}]"
        datetime_colored = termcolor.colored(datetime_text, "grey")
    
    if config["show_calling_module"]:
        from_stack = inspect.stack()[1]
        module = inspect.getmodule(from_stack[0])
        module_name = module.__name__
        calling_module_text = f"Called by [{module_name}]"
        calling_module_colored = termcolor.colored(calling_module_text, "grey")
    
    finished_message = f"{message_head_colored}{log_level_colored}{datetime_colored}=> {message}\n{calling_module_colored}\n"
    #bad but idk
    clean_text = message.replace('[1m[94m','').replace('[0m', '')
    log_message = f"{message_head_text}{log_level_text}{datetime.datetime.now()}=> {clean_text}\n{calling_module_text}\n\n"
    print(finished_message)
    
    global logfile
    if logfile:
        with open(str(logfile.name),"a+") as logfile:
            logfile.write(f'{log_message}')

def highlighted(text : str):
    highlighted_text = termcolor.colored(text, "light_blue", attrs = ["bold"])
    return(highlighted_text)

def lowlighted(text : str):
    highlighted_text = termcolor.colored(text, "grey", attrs = ["bold"])
    return(highlighted_text)

def create_logfile(log_type):
    #print_status("info", 4,"Creating Logfile")
    with open(f"logs/session-{str(datetime.datetime.now()).replace(':','')}.log","w") as logfile:
        logfile.write(f'Log created.\n')
        logfile.write(f'Time: {datetime.datetime.now()}\n')
        logfile.write(f'Client: {config_handler.get_active_client_name()}\n')
        logfile.write(f'Log-type: {log_type}\n')
        logfile.write(f'\n-------------------------------------------------\n\n')
        print_status("success", 5, f"Logfile created!")
    return(logfile)
        
        
if __name__ == "__main__":
    print(highlighted("Hallo"))
    print_status("info", 1,"Hallo Leute")