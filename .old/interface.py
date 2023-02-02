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

while(True):
  request = input("Enter json: ")
  print('')
  if(request == 'exit()'):
    exit(200)


  response = requests.post(f"http://{settings.server.ip}:{settings.server.port}", json = request)
  response = response.json()
  # print(f'-{error}-')
  try:
    error = int(response)
  except TypeError:
    error = None
  finally:
    if (error in settings.error.codes):
      print(f'\n {error} -- {settings.error.codes[error]} \n')
    else:
      print('\n' + str(response) + '\n')   
 