from settings import settings 
from database import database
import requests

class interface:
  def start():
    while(True):
      request = input("Enter json:")
      if(request == 'exit()'):
        break
      elif(request == 'exit(200)'):
        exit(200)
      request = f"{settings.ip}:{settings.port}/json='{request}'"
      print(request)
      response = requests.get(url = request)
      print('\n\n\n'+response)
    