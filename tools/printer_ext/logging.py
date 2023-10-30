import datetime
from tools.printer_ext import get_configs

class Logfile_writer():
    def __init__(self):
        self.configs = get_configs.Config_handler()
        self.client_name = self.configs.config["used_client" ]
        self.logfile = self.create_logfile()
        
    def create_logfile(self, log_type = "auto"):
        with open(f"logs/session-{str(datetime.datetime.now()).replace(':','')}.log","w") as logfile:
            logfile.write(f'Log created.\n')
            logfile.write(f'Time: {datetime.datetime.now()}\n')
            logfile.write(f'Client: {self.client_name}\n')
            logfile.write(f'Log-type: {log_type}\n')
            logfile.write(f'\n-------------------------------------------------\n')
        return(logfile.name)
    
    def log(self, message : str, status_code : str, time : str, call_source):
        clean_text = self.clean_message(message)
        log_message = f"\n[{status_code}] at [{time}] from [{call_source}]:\n{clean_text}\n---"
        with open(self.logfile, "a+") as log_file:
            log_file.write(f"{log_message}")
        
    def clean_message(self, message):
        clean_text = message.replace('[1m[94m','')
        clean_text = clean_text.replace('[0m', '')
        clean_text = clean_text.replace('[1m[30m', '')
        return(clean_text)