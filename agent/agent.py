import psutil
import time
from requests import post
from datetime import datetime
import socket

register = {}


while True:
    processes = psutil.process_iter(['name', 'pid', 'ppid'])
    hostname = socket.gethostname()

    register["hostname"] = hostname 
    register["timestamp"] = str(datetime.now())
    register["processes"] = [p.info for p in processes]
    post("http://127.0.0.1:8000/events", json= register)
    time.sleep(5)
    print("ok")




