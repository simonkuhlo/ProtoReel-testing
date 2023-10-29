import os
from tools import console_printer as p


async def get_modules_by_type(module_type : str, path : str):
    p.print_status("info", 4, f"Getting all modules in {p.lowlighted(path)} with type {p.highlighted(module_type)}")
    module_dict = {}
    dir_list = os.listdir(f"{path}")
    for dirname in dir_list:
        if os.path.isdir(f"{path}/{dirname}"):
            if dirname.startswith(("[!]", "__")):
                p.print_status("info", 4, f"Ignoring {p.lowlighted(dirname)} becasue of prefix")
                continue
            things_list = []
            for thing in os.listdir(f"{path}/{dirname}"):
                if thing.startswith(module_type):
                    things_list.append(thing)
            module_dict[dirname] = things_list
    p.print_status(f"success", 5, f"Got all Modules: {p.lowlighted(module_dict)}")
    return(module_dict)