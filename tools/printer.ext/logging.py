import datetime
from tools import config_handler

class Logfile_writer():
    def __innit__(self):
        self.logfile = self.create_logfile()
    
    def create_logfile(log_type = "auto"):
        with open(f"logs/session-{str(datetime.datetime.now()).replace(':','')}.log","w") as logfile:
            logfile.write(f'Log created.\n')
            logfile.write(f'Time: {datetime.datetime.now()}\n')
            logfile.write(f'Client: {config_handler.get_active_client_name(print_log=False)}\n')
            logfile.write(f'Log-type: {log_type}\n')
            logfile.write(f'\n-------------------------------------------------\n\n')
        return(logfile.name)
    
    def log(self, message, status_code, time, call_source):
        clean_text = self.clean_message(message)
        log_message = f"{status_code}{time}=> {clean_text}\n{call_source}\n\n"
        with open(self.logfile, "a+") as log_file:
            log_file.write(f"{log_message}")
        
    def clean_message(message):
        clean_text = message.replace('[1m[94m','')
        clean_text = clean_text.replace('[0m', '')
        
        return(clean_text)