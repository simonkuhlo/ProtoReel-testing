import json

def get_active_client_name():
        with open("res/config.json", "r") as json_file:
                config = json.load(json_file)
                active_client_name = config["used_client"]
                return(active_client_name)