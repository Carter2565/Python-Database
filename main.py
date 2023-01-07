import imp
import json
import argparse
from server import webserver
from interface import interface
settings, config = imp.load_source('settings')


parser = argparse.ArgumentParser()
parser.add_argument('-interface', action='store_true', help='Enables UI')
args = parser.parse_args()

class response:
  def __init__(self, json):
    self.response = None
    self.request = json
    database.request(self.request)
    return(self.response)
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
  
  def request(self):
    try:
      opperation = self.json['opperation']
    except:
      opperation = None
    
    if(opperation == 'content'): # A content request
      for function in settings.functions:
        if(function == self.json[function]):
          pass
        else:
          response.error(204)
    elif(opperation == 'login'): # A login request
      pass
    elif(opperation == 'manual'): # A request for a manualy set value
      pass
    else:
      response.error(400)

if(args.interface):
  interface.start()
else:
  database = webserver(config.ip, config.port)
  database.start()