import imp
settings, config = imp.load_source('settings')
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
      responce = requests.get(request)
    