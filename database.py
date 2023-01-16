import json
import base64
import settings

class response:
  def __init__(self, json):
    self.request = json
    db = database()
    print(self.request)
    self.response = db.request(str(self.request))
    print(self.response)

    # 400 Request error
    # 401 Unauthorized
    # 204 No content to be sent

class login:
  def login(data):
    email = data["login"] # gets the email
    pwd = data["pwd"] # gets the password 
    userdata = json.loads(database.getUserdata()) # gets userdata from file
    try:
      user = userdata[email] #  Gets user by email.
    except:
      return('401')
    if (not(pwd == user["pwd"])):
      user = None
      return(401)
    return(200)

class database(login):
  def getUserdata():
    with open(f"database/userdata.json", "r") as f:
      userdata = json.loads(f.read())
      return(userdata) 

  def getProfiledata():
    with open("database/profiledata.json", "r") as f:
      profiledata = json.loads(f.read())
      return(profiledata)

  def getAsset():
    with open("python/database/assets/assets.json", 'r') as f:
      assets = json.loads(f.read())
      return(assets)

  def request(request = None): # 
    try:
      data = json.loads(request)
      opperation = data['opperation']
    except:
      opperation = None
    
    if(opperation == 'user'): # A userdata/email request
      if(login.login(data) == 200):
        email = data["login"]
        userdata = database.getUserdata()
        user = userdata[email]
        return(user)
      else:
        return(json.dumps(401))

    elif(opperation == 'profile'): # A profile/username request
      pass

    elif(opperation == 'assets'): # A asset request
      pass

    else:
      return(400)


