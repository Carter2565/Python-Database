from settings import settings 
from database import database
import requests
import var_dump
import json

while(True):
  request = input("Enter json:")
  if(request == 'exit()'):
    exit(200)

  print('\n'+request)

  # response = requests.post(f"http://{settings.server.ip}:{settings.server.port}", json = request)
  # print('\n\n\n'+var_dump(response.json()))
  data = {'key': 'value'}
  response = requests.post('http://localhost:8000', json=data)
  print(response.json())