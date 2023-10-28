if __name__ == "__main__":
    import sys
    import asyncio
    sys.path.append(".") 
from tools import config_handler
import termcolor


def print_status(status : str = "info", level : int = 5, message : str = None):
    config = config_handler.get_config("term_formatting")
    log_level = int(config["log_level"])
    if level < log_level:
        return
    current_status = config["status_codes"][status]
    
    message_head_color = current_status["color"]
    message_head_config = f'pre_{config["status_pre"]}'
    message_head_text = f"[{current_status[message_head_config]}]"
    message_head_colored = termcolor.colored(message_head_text, message_head_color)
    
    finished_message = f"\n{message_head_colored} {message}\n"
    print(finished_message)



if __name__ == "__main__":
    asyncio.run(print_status("info", 1,"Hallo Leute"))