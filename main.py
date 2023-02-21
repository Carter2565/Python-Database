#-----------------------------------------------------------------------#
#                         --- Python Database ---
#
# Contributors: @Carter2565#5594, 
# This is the current database for PTSO-Exchange.
# This project can be used as a template for any python database.
#
#-----------------------------------------------------------------------#

import os
import updater
import argparse
import threading
from server import webserver
from interface import interface
from settings import settings as config, settings

parser = argparse.ArgumentParser()
parser.add_argument('-interface', action='store_true', help='Enables UI')
args = parser.parse_args()
 
database = webserver(config.server.ip, config.server.port)

# def interface():
#   os.system('python interface.py')

updater.update()

if(args.interface or config.interface.interface):
  threading.Thread(target=interface, args=[]).start()  
  
threading.Thread(target=database.start(), args=[]).start()  