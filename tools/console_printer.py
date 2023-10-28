if __name__ == "tools/console_printer":
    from res import config_handler

if __name__ == "__main__":
    import sys
    sys.path.append(".") 
    from res import config_handler

config = config_handler.get_config("term_formatting")
print(config)