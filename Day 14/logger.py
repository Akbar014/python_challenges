import os 
import datetime

Base_DIR = os.path.dirname(__file__)
log_dir = os.path.join(Base_DIR, 'logs')
os.makedirs(log_dir, exist_ok=True)


def trigger_log_save():
    filename = f"{datetime.datetime.now()}.txt"
    filepath = os.path.join(log_dir, filename)
    with open(filepath, 'w+') as f:
        f.write("dfsdfsdfs")