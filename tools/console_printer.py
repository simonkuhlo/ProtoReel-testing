if __name__ == "__main__":
    import sys
    import asyncio
    sys.path.append(".") 
from res import config_handler
import termcolor


async def print_status(status : str = "info", level : int = 5, message : str = None):
    config = config_handler.get_config("term_formatting")
    log_level = int(config["log_level"])
    if level < log_level:
        return
    config = config["status_codes"]
    current_status = config[status]
    
    message_head_color = current_status["color"]
    message_head_config = f'pre_{config["pre"]}'
    message_head_text = f"[{current_status[message_head_config]}]"
    message_head_colored = termcolor.colored(message_head_text, message_head_color)
    
    finished_message = f"{message_head_colored} {message}"
    print(finished_message)



if __name__ == "__main__":
    asyncio.run(print_status("info", 1,"Hallo Leute"))