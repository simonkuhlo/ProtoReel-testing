import os
from tools.console_printer import SP


async def get_modules_by_type(module_type : str, path : str):
    SP.print_status("info", 4, f"Getting all modules in {SP.lowlighted(path)} with type {SP.highlighted(module_type)}")
    module_dict = {}
    dir_list = os.listdir(f"{path}")
    for dirname in dir_list:
        if os.path.isdir(f"{path}/{dirname}"):
            if dirname.startswith(("[!]", "__")):
                SP.print_status("info", 4, f"Ignoring {SP.lowlighted(dirname)} becasue of prefix")
                continue
            things_list = []
            for thing in os.listdir(f"{path}/{dirname}"):
                if thing.startswith(module_type):
                    things_list.append(thing)
            module_dict[dirname] = things_list
    SP.print_status(f"success", 5, f"Got all Modules: {SP.lowlighted(module_dict)}")
    return(module_dict)