#-----------------------------------------------------------------------#
#                         --- Python Database ---
#
# Contributors: @Carter2565#5594, 
# This is the current database for PTSO-Exchange.
# This project can be used as a template for any python database.
#
#-----------------------------------------------------------------------#

import json
import base64
import secrets
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

def generate_token():
    return secrets.token_hex(16)

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
    def User(request):
      client = json.loads(request)
      def Userdata():
        userdata = database.get.Userdata()
        # data = json.loads(userdata)
        data = userdata
        # print(data)
        login = client['login']
        if(str(login) not in data):

          data[login] = {}
          data[login]['fname'] = client['fname']
          data[login]['lname'] = client['lname']
          data[login]['pwd'] = client['pwd']
          data[login]['owned'] = []
          data[login]['created'] = []
          data[login]['username'] = client['username']
          data[login]['token'] = secrets.token_hex(16) # Generates a token

          return(data)
        else:
          return(409)

      def Profiledata():
        # data = json.loads(get.Profiledata())
        data =database.getProfiledata()
        # print(data)
        username = client['username']
        if(str(username) not in data):

          data[username] = {}
          data[username]['fname'] = client['fname']
          data[username]['lname'] = client['lname']
          data[username]['created'] = []
          data[username]['tags'] = settings.assets.defaults.profile.tags
          data[username]['about'] = settings.assets.defaults.profile.about
          data[username]['pfp'] = settings.assets.defaults.profile.pfp

          return(data)
        else:
          return(409)

      error = 0
      try:
        response = int(str(Userdata()))
        print(response)
        if (response in settings.error.codes):
          error -= 2
      except TypeError:
        pass
      finally:
        try:
          response = int(str(Profiledata()))
          print(print(type(response)))
          if (response in settings.error.codes):
            error += 4
        except TypeError:
          pass
        finally:
          print(f'Error: {error}')
          if(error == 0):
            userdata = Userdata()
            profiledata = Profiledata()
            with open(f"{settings.file.dir}database/userdata.json", "w") as f:
              f.write(json.dumps(userdata))
            with open(f"{settings.file.dir}database/profiledata.json", "w") as f:
              f.write(json.dumps(profiledata))
            # print(f'{get.Userdata}, \n \n{get.Profiledata} \n ')
            print(f'{database.get.Userdata()}, \n \n{database.get.Profiledata()} \n ')
            return(201)
          elif(error == -2):
            # Userdata error
            print('Userdata Error')
            print(f'{Userdata()}, \n \n{Profiledata()} \n ')
            return(206)
            pass
          elif(error == 2):
            # Userdata & Profiledata error
            print('Userdata & Profiledata error')
            print(f'{Userdata()}, \n \n{Profiledata()} \n ')
            return(204)
            pass
          elif(error == 4):
            # Profiedata error
            print('Profiedata error')
            print(f'{Userdata()}, \n \n{Profiledata()} \n ')
            return(206)
            pass

  def request(self, request): # 
    try:
      data = json.loads(request)
      operation = data['operation']
      request = data['request']
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
