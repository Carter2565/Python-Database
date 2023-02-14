#-----------------------------------------------------------------------#
#                         --- Python Database ---
#
# Contributors: @Carter2565#5594, 
# This is the current database for PTSO-Exchange.
# This project can be used as a template for any python database.
#
#-----------------------------------------------------------------------#

from http.server import BaseHTTPRequestHandler, HTTPServer
from database import response as server
import http.cookies
import hashlib
import time
import json

def hash_string(string):
  return hashlib.md5(string.encode()).hexdigest()

class Server(BaseHTTPRequestHandler):
  # def do_GET(self):
  #   self.send_response(200)
  #   self.send_header("Content-type", "text/json")
  #   self.end_headers()

    # content = response((self.path)[7:])
    # self.wfile.write(bytes(content, "utf-8"))

    # try:
    #   print(json.loads(str(self.path)[7:]))
    # except json.decoder.JSONDecodeError:
    #   print('400 - No json data')

  def do_OPTIONS(self):
    self.send_response(200)
    self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    self.send_header("Access-Control-Allow-Origin", "*")
    self.send_header("Access-Control-Allow-Headers", "Content-Type")
    self.end_headers()

  def do_GET(self):
    cookie = http.cookies.SimpleCookie(self.headers.get("Cookie"))
    if "token" in cookie:
      token = cookie["token"].value
      asset = self.path.split("/")[1]
      assetid = asset.split(".")[0]
      request_data = {"operation":"get", "request": "assets", "asset":assetid}
      response = server(request_data).response
      if response["public"] == 1 or hash_string(token + assetid) == response["token"]:
        self.send_response(200)
        self.send_header("Content-Type", "application/octet-stream")
        self.end_headers()
        with open(asset, "rb") as f:
            self.wfile.write(f.read())
        return
    self.send_response(401)
    self.send_header("Content-Type", "text/plain")
    self.end_headers()
    self.wfile.write("Unauthorized".encode("utf-8"))

  def do_POST(self):
    # from database import response as server
    content_length = int(self.headers['Content-Length'])
    body = self.rfile.read(content_length).decode('utf-8')
    # json_data = json.loads(str(body))
    json_data = body
    print(body)
    # print(json_data)
    # print(json_data)
    # response(json_data)
    response = server(json_data).response

    # print(response)
    try:
      error = int(response)
      self.send_response(error)
    except:
      self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.send_header("Access-Control-Allow-Origin", "*")
    self.end_headers()
    # print(str(message)+'-----------')
    self.wfile.write(bytes(str(response), "utf8"))
    # self._send_response(res.response)
    print(f'\n{response} \n')

class webserver:
  def __init__(self, ip, port):
    self.hostName = ip
    self.serverPort = port
  
  def start(self):
    server = HTTPServer((self.hostName, self.serverPort), Server)
    print("[Python API] -- Server started http://%s:%s" % (self.hostName, self.serverPort) + '\n')

    try:
      server.serve_forever()
    except KeyboardInterrupt:
      pass

    server.server_close()
    print("[Python] -- Server stopped.")