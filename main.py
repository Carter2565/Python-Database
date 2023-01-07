from server.py import webserver
from settings.config import settings as settings, config
import json

parser = argparse.ArgumentParser()
parser.add_argument('-interface', action='store_true', help='Enables UI')
args = parser.parse_args()

class response:
  response = None
  def __init__(self, json):
    self.request = json
    database(self.request)
    return(response)
  def error(code):
    response = code 
    # 400 Request error
    # 204 No content to be sent

class content(response):
  def __init__(self, functionn):
    self.function = function

class login:
  def __init__(self):
    return

class database(login, content):
  def __init__(self, data):
    self.json = json.dumps(data) 
  
  try:
    opperation = self.json[opperation]
  except:
    opperation = None
  
  if(opperation = 'content'):
     for function in settings.functions:
      if(function = self.json[function]):
        pass
      else:
        response.error(204)
  elif(opperation = 'login'):

  else:
    response.error(400)

 if(args.interface):
  interface.start()
else:
  database = webserver(config.ip, config.port)
  database.start()