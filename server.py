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
from settings import settings
import http.cookies
import hashlib
import time
import json
import cgi
import os

def hash_string(string):
  return hashlib.md5(string.encode()).hexdigest()

class Server(BaseHTTPRequestHandler):
  def do_OPTIONS(self):
    self.send_response(200)
    self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    self.send_header("Access-Control-Allow-Origin", "*")
    self.send_header("Access-Control-Allow-Headers", "Content-Type")
    self.end_headers()

  def do_GET(self):
    cookie = http.cookies.SimpleCookie(self.headers.get("Cookie"))
    token = cookie.get("token", "")
    asset = self.path.split("/")[1]
    assetid = asset.split(".")[0]

    if assetid.isdigit():
        request_data = {"operation": "get", "request": "asset", "asset": assetid}
        response = json.loads(server(json.dumps(request_data)).response)

        if response != 400:
            if response["public"] == 1 or hash_string(token + assetid) == response["token"]:
                self.send_response(200)
                self.send_header("Content-Type", "application/octet-stream")
                self.end_headers()
                print(asset)
                with open(os.path.join(settings.file.dir, "database", "assets", asset), "rb") as f:
                    self.wfile.write(f.read())
                return
            else:
                self.send_response(401)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write("Unauthorized".encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Not Found".encode("utf-8"))
    else:
        if os.path.isfile(os.path.join(settings.file.dir, "database", "assets", asset)):
            self.send_response(200)
            self.send_header("Content-Type", "application/octet-stream")
            self.end_headers()
            print(asset)
            with open(os.path.join(settings.file.dir, "database", "assets", asset), "rb") as f:
                self.wfile.write(f.read())
            return
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Not Found".encode("utf-8"))



  def do_POST(self):
    content_type = self.headers.get('Content-Type')

    if content_type.startswith('multipart/form-data'):
      # Handle file upload
      form = cgi.FieldStorage(
        fp=self.rfile,
        headers=self.headers,
        environ={'REQUEST_METHOD': 'POST'}
      )

      # Get uploaded file
      uploaded_file = form['file'].file
      filename, extension = os.path.splitext(form['file'].filename)

      if(os.path.isfile(os.path.join(settings.file.UPLOAD_PATH,f'{filename}{extension}'))):
        x = 0
        while(os.path.isfile(os.path.join(settings.file.UPLOAD_PATH,f'{filename}{x}{extension}'))):
          x += 1
        file = f'{filename}{x}{extension}'
      else:
        file = f'{filename}{extension}'

      # Save uploaded file to disk
      with open(os.path.join(settings.file.UPLOAD_PATH, file), 'wb') as f:
        f.write(uploaded_file.read())

      # Send response
      self.send_response(200)
      self.send_header('Content-type', 'text/plain')
      self.end_headers()
      self.wfile.write('File uploaded successfully'.encode('utf-8'))
    else:
      # Handle regular POST request
      content_length = int(self.headers['Content-Length'])
      body = self.rfile.read(content_length).decode('utf-8')
      json_data = body
      print(body)

      response = server(json_data).response

      try:
        error = int(response)
        self.send_response(error)
      except:
        self.send_response(200)

      self.send_header('Content-type', 'application/json')
      self.send_header("Access-Control-Allow-Origin", "*")
      self.end_headers()

      self.wfile.write(bytes(str(response), "utf8"))
      print(f'\n{response} \n')


  # def do_POST(self):
  #     content_length = int(self.headers['Content-Length'])
  #     body = self.rfile.read(content_length).decode('utf-8')
  #     json_data = body
  #     print(body)

  #     response = server(json_data).response

  #     try:
  #         error = int(response)
  #         self.send_response(error)
  #     except:
  #         self.send_response(200)

  #     self.send_header('Content-type', 'application/json')
  #     self.send_header("Access-Control-Allow-Origin", "*")
  #     self.end_headers()

  #     self.wfile.write(bytes(str(response), "utf8"))
  #     print(f'\n{response} \n')


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