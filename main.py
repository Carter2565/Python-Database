from server.py import webserver
import json

parser = argparse.ArgumentParser()
parser.add_argument('-interface', action='store_true', help='Enables UI')
args = parser.parse_args()

class database:
  def __init__(self, data):
    self.json = json.dumps(data) 

class userdata(database):
  def __init__(self, data, function):
    super().__init__(data)()

if(args.interface):
  interface.start()