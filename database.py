import json
import base64
import settings

class response:
  def __init__(self, json):
    self.request = json
    self.response = database.request(self.request)
    print(response)
  def error(self, code):
    self.response = code 
    # 400 Request error
    # 401 Unauthorized
    # 204 No content to be sent
  # response = None
class login:
  def __init__(self):
    return

class database(login):
  def __init__(self, data):
    self.json = json.loads(data) 
  
  def request(self): # 
    try:
      opperation = self.json['opperation']
    except:
      opperation = None
    
    if(opperation == 'user'): # A userdata/email request
      pass

    elif(opperation == 'profile'): # A profile/username request
      pass

    elif(opperation == 'assets'): # A asset request
      pass

    else:
      response.error(response,400)


def getData(file):
  with open(f"database/{file}].json", "r") as f:
    data = json.dumps(f.read())
    return(data) 

# def getProfiledata():
#   with open("database/profiledata.json", "r") as f:
#     data = f.read()
#     profiledata = json.dumps(data)
#     return(profiledata)

def getAsset():
  with open("python/database/assets/assets.json", 'r') as f:
    x = f.read()
    assets = json.dumps(x)
    return(assets)
