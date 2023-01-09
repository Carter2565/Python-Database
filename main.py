import argparse
from server import webserver
from settings import settings as config, settings
from database import database
from interface import interface

parser = argparse.ArgumentParser()
parser.add_argument('-interface', action='store_true', help='Enables UI')
args = parser.parse_args()
 
database = webserver(config.ip, config.port)
database.start()

if(args.interface):
  interface.start()