#-----------------------------------------------------------------------#
#                         --- Python Database ---
#
# Contributors: @Carter2565#5594, 
# This is the current database for PTSO-Exchange.
# This project can be used as a template for any python database.
#
#-----------------------------------------------------------------------#

from settings import settings 
from database import database
import requests
from time import sleep
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-interface', action='store_true', help='Enables UI')
args = parser.parse_args()

def interface():
  sleep(1)
  while(True):
    request = input("Enter json: ")
    print('')
    if(request == 'exit()'):
      exit(200)


    response = requests.post(f"http://{settings.server.ip}:{settings.server.port}", json = json.loads(request))
    response = response.json()
    # print(f'-{error}-')

    # --------------------------------------- use isinstance ----------------------------------------
    try:
      error = int(response)
    except TypeError:
      error = None
    finally:
      if (error in settings.error.codes):
        print(f'\n {error} -- {settings.error.codes[error]} \n')
      else:
        print('\n' + str(response) + '\n')   
  

if(args.interface):
  interface()