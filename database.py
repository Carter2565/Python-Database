import json

def getUser(data):
  f = open("python/database/userdata.json")
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
