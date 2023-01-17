from settings import settings 
from database import database
import requests

while(True):
  request = input("Enter json: ")
  print('')
  if(request == 'exit()'):
    exit(200)


  response = requests.post(f"http://{settings.server.ip}:{settings.server.port}", json = request)
  error = str(response.json())
  # print(f'-{error}-')
  statuscode = False
  for code in settings.error.codes:
    # print(f'{error}--{code}')
    if(error == str(code)):
      statuscode = True
      print(f'\n {code} -- {settings.error.codes[code]} \n')
  if(not statuscode):
    print('\n' + str(response.json()) + '\n')   
 