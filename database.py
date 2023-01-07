import json

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
    self.json = json.loads(data) 
  
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


def getUser(data):
  f = open(settings.launchDir + "database/userdata.json")
  x = f.read()
  email = data["login"]
  pwd = data["pwd"]
  userdata = json.loads(x)
  try:
    user = userdata[email] #  Gets user by email.
  except:
    return('User does not exist')
 # print(user["pwd"])
  if (not(pwd == user["pwd"])):
    user = None
    # print("123456789"+pwd+"pwd")
    return('User credentials dont match')
    # raise Exception('User credentials dont match')
  return(user)

def getProfile(username):
  with open("database/profiledata.json", "r") as f:
    data = f.read()
  userdata = jsonFormatter.loads(data)
  if username in userdata:
    return userdata[username]
  else:
    return "User does not exist"




def content():
      def featured():
        parameters=json["parameters"]
        asset = parameters["asset"]
        asset = getAssets(asset)
        return(jsonFormatter.dumps(asset))

      def profile():
        parameters=json["parameters"]
        asset = parameters["asset"]
        if(asset != None):
          print(asset)
          user = getProfile(asset)
        else:
          user = getUser(json)
          print(user)
        return(jsonFormatter.dumps(user))

      def image():
        parameters=json["parameters"]
        asset = parameters["asset"]
        username = parameters["item"]
        try:
          userdata = getProfile(username)
          image = asset+"/"+userdata[asset]
        except:
          image = asset+'/default.png'
        item = parameters["item"]
        image = f'python/database/assets/userdata/{image}'
        with open(image, 'rb') as f:
          image_data = f.read()
#        print(image_data)
        base64_image = base64.b64encode(image_data).decode()
        return(str(base64_image))

      def tags():
        tags = getUserdata(json,'tags')
#        print(tags)
        return(jsonFormatter.dumps(tags))
