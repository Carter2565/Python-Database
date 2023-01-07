import json
from main import settings, response

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
