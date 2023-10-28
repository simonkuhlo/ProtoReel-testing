import dotenv
import asyncio
import os


async def get_token(client:str) -> str:
        
    token = os.getenv(f"TOKEN-{client}")

    if token is None:
        print("\n[!] No Token. Add / Update the Token for this Client using [2]update_token.\n")
        
    return(token)


async def add_token(client:str, token:str):
    dotenv.set_key(dotenv_path=".env", key_to_set=f"TOKEN-{client}", value_to_set=f"{token}")


async def main():
    
    is_env = dotenv.load_dotenv()
    
    if not is_env:
        print("\n[!] No .env File. Create the .env-file using the [3]create_env.\n")
    
    action = input("What do you want to do?\n\n[1] get_token\n[2] update_token\n[3] create_env\n\n-> ")
    
    match action:
        case "1":
            client_name = input("Client name?\n->")
            token = await get_token(client_name)
            print(f"{client_name}'s Token: {token}.")

        case "2":
            client_name = input("Client name?\n->")
            token = input("Token?\n->")
            await add_token(client_name, token)
            print(f"\nAdded the following Token for client {client_name}: {token}")
            
        case "3":
            print(f"WIP")
  
        case _:
            print(f"[{action}] is not a valid action.")
    await continue_or_exit()
    

async def continue_or_exit():
    next_task = input("\nDo another Task? [y/n]\n-> ")
    if next_task == "y":
        await main()
    else:
        exit()

if __name__ == "__main__":
    asyncio.run(main())