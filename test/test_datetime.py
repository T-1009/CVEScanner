import datetime

Green = '\033[92m'
Blue = '\033[94m'
Grey = '\033[0m'
Red = '\033[31m'
White = '\33[97m'
Yellow = '\33[93m'

def log_info(message):
    current_time = datetime.datetime.now().strftime("[%H:%M:%S]")
    print("{}{} {}INFO - {}{}".format(Yellow, current_time, Green, message, Grey))


log_info("generate poc tasks...")
log_info("total tasks: 78")
log_info("begin poc scan...  (threads: 78)")

log_info("done with 18.599050998687744s")
