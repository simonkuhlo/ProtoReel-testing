if __name__ == "__main__":
    import sys
    import asyncio
    sys.path.append(".") 
from res import config_handler
import termcolor


async def get_status_config():
    config = config_handler.get_config("term_formatting")
    status_config = config["status_codes"]
    return(status_config)

async def print_status(status, message):
    return




if __name__ == "__main__":
    asyncio.run(get_status_config())