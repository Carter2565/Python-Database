#-----------------------------------------------------------------------#
#                         --- PTSO-Exchange ---
#
# Contributors: @Carter2565#5594, 
# PTSO-Exchange api webserver.
# Api.py is just the webserver Extensions.py contains all main functions
#
#-----------------------------------------------------------------------#

from http.server import BaseHTTPRequestHandler, HTTPServer

import time
import json

class Server(BaseHTTPRequestHandler):
  # def _set_response(self):
  #   self.send_response(200)
  #   self.send_header('Content-type', 'text/json')
  #   self.end_headers()
  def _send_response(self, message):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    # print(message+'-----------')
    self.wfile.write(bytes(message, "utf8"))

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

  def do_POST(self):
    from database import response
    content_length = int(self.headers['Content-Length'])
    body = self.rfile.read(content_length)
    json_data = json.loads(body)
    print(json_data)
    res = response(json_data).response
    self._send_response(res)

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