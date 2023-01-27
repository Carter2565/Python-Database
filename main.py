import os
import threading
import argparse
from server import webserver
from settings import settings as config, settings
from database import database

parser = argparse.ArgumentParser()
parser.add_argument('-interface', action='store_true', help='Enables UI')
args = parser.parse_args()
 
database = webserver(config.server.ip, config.server.port)

def interface():
  os.system('python interface.py')

# if(args.interface):
threading.Thread(target=interface, args=[]).start()  
  
threading.Thread(target=database.start(), args=[]).start()  