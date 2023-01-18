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
    userdata = database.getUserdata() # gets userdata from file
    try:
      user = userdata[email] #  Gets user by email.
    except KeyError:
      return(400)
    if (not(pwd == user["pwd"])):
      user = None
      return(401)
    return(202)

class database(login):
  def getUserdata():
    with open(f"{settings.launchDir}database/userdata.json", "r") as f:
      userdata = json.loads(f.read())
      return(userdata) 

  def getProfiledata():
    with open(f"{settings.launchDir}database/profiledata.json", "r") as f:
      profiledata = json.loads(f.read())
      return(profiledata)

  def getAsset():
    with open(f"{settings.launchDir}database/assets/assets.json", 'r') as f:
      assets = json.loads(f.read())
      return(assets)


  def request(self, request): # 
    try:
      data = json.loads(request)
      opperation = data['opperation']
    except:
      opperation = None
    
    if(opperation == 'user'): # A userdata/email request
      if(login.login(data) == 202):
        email = data["login"]
        userdata = database.getUserdata()
        user = userdata[email]
        return(json.dumps(user))
      else:
        return(json.dumps(login.login(data)))

    elif(opperation == 'profile'): # A profile/username request
      userdata = database.getProfiledata()
      if('username' in userdata):
        username = data['username']
        profiledata = userdata[username]
        return(profiledata)
      except KeyError:
        return(400)


    elif(opperation == 'assets'): # A asset request
      pass

    else:
      return(400)


