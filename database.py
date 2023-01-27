import json
import base64
from settings import settings

class response:
  def __init__(self, json):
    self.request = json
    db = database()
    # print(self.request)
    self.response = db.request(str(self.request))
    # print(self.response)

    # 400 Request error
    # 401 Unauthorized
    # 204 No content to be sent

class login:
  def login(data):
    try:
      email = data["login"] # gets the email
      pwd = data["pwd"] # gets the password 
    except KeyError:
      return(400)
    userdata = database.get.Userdata() # gets userdata from file
    try:
      user = userdata[email] #  Gets user by email.
    except KeyError:
      return(400)
    if (not(pwd == user["pwd"])):
      user = None
      return(401)
    return(202)

class database(login):
  class get:
    def Userdata():
      with open(f"{settings.file.dir}database/userdata.json", "r") as f:
        userdata = json.loads(f.read())
        return(userdata) 

    def Profiledata():
      with open(f"{settings.file.dir}database/profiledata.json", "r") as f:
        profiledata = json.loads(f.read())
        return(profiledata)

    def Asset():
      with open(f"{settings.file.dir}database/assets/assets.json", 'r') as f:
        assets = json.loads(f.read())
        return(assets)

    def Object():
      with open(f"{settings.file.dir}database/objectdata.json", "r") as f:
        objectdata = json.loads(f.read())
        return(objectdata) 
  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  class set:
    pass

  def request(self, request): # 
    try:
      data = json.loads(request)
      operation = data['operation']
    except:
      operation = None
    
    if(operation == 'get'):

      if(request == 'user'): # A userdata/email request
        if(login.login(data) == 202):
          email = data["login"]
          userdata = database.get.Userdata()
          user = userdata[email]
          return(json.dumps(user))
        else:
          return(json.dumps(login.login(data)))

      elif(request == 'profile'): # A profile/username request
        userdata = database.get.Profiledata()
        if(data['username'] in userdata):
          username = data['username']
          profiledata = userdata[username]
          return(json.dumps(profiledata))
        else:
          return(400)

      elif(request == 'asset'): # A asset request
        assets = database.get.Asset()
        if(data['asset'] in assets):
          asset = data['asset']
          return(json.dumps(asset))
        else:
          return(400)

      elif(request == 'object'): # A object request. This is miscellaneous things ex: public goals or featured items etc
        objectdata = database.get.Object()
        return(json.dumps(objectdata))

      else:
        return(400)

    elif(operation == 'set'):
      pass

    else:
      return(400)
