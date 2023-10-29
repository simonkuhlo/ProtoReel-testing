import os

async def get_modules_by_type(module_type : str, path : str):
  module_dict = {}
  dir_list = os.listdir(f"{path}")
  for dirname in dir_list:
    if os.path.isdir(os.path.join(os.path.abspath("./plugins"), dirname)):
        if dirname.startswith(("!", "__")):
          continue
        things_list = []
        for thing in os.listdir(f"./plugins/{dirname}"):
          if thing.startswith(module_type):
            things_list.append(thing)
        module_dict[dirname] = things_list
  return(module_dict)