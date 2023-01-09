import imp
import argparse
from server import webserver
from database import database
from interface import interface
settings, config = imp.load_source('settings','./')

parser = argparse.ArgumentParser()
parser.add_argument('-interface', action='store_true', help='Enables UI')
args = parser.parse_args()
 
if(args.interface):
  interface.start()

database = webserver(config.ip, config.port)
database.start()