if __name__ == "__main__":
    import sys
    sys.path.append(".")
    
import os
import dotenv

from tools import config_handler 
from tools import console_printer as p



def get_token(client:str) -> str:
        
    token = os.getenv(f"TOKEN-{client}")

    if token is None:
        p.print_status("error", 1, "No Token. Add / Update the Token for this Client using [2]update_token.")
        
    return(token)


def add_token(client:str, token:str):
    dotenv.set_key(dotenv_path=".env", key_to_set=f"TOKEN-{client}", value_to_set=f"{token}")


def main():
    load_env()
    
    action = input("What do you want to do?\n\n[1] get_token\n[2] update_token\n[3] create_env\n\n-> ")
    
    match action:
        case "1":
            client_name = input("Client name?\n->")
            token = get_token(client_name)
            p.print_status("info", 1, f"{client_name}'s Token: {token}.")

        case "2":
            client_name = input("Client name?\n->")
            token = input("Token?\n->")
            add_token(client_name, token)
            p.print_status("error", 2,f"\nAdded the following Token for client {client_name}: {token}")
            
        case "3":
            p.print_status("warning", 2,("WIP"))
  
        case _:
            p.print_status("error", 1, f"[{action}] is not a valid action.")
            
    continue_or_exit()
    
def load_env():
    is_env = dotenv.load_dotenv()
    
    if not is_env:
        p.print_status("error", 1,"\n[!] No .env File. Create the .env-file using the [3]create_env.\n")

def continue_or_exit():
    next_task = input("Do another Task? [y/n]\n-> ")
    if next_task == "y":
        main()
    else:
        exit()
        
def get_active_client_token():
    load_env()
    active_client_name = config_handler.get_active_client_name()
    active_client_token = get_token(active_client_name)
    
    return(active_client_token)

if __name__ == "__main__":
    main()