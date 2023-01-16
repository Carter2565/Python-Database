from settings import settings 
from database import database
import requests
import var_dump
import json

while(True):
  request = input("Enter json: ")
  if(request == 'exit()'):
    exit(200)

  try:
    response = requests.post(f"http://{settings.server.ip}:{settings.server.port}", json = request)
    print('\n' + str(response.json()) + '\n')
  except:
    print('\n Response error \n')