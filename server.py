#-----------------------------------------------------------------------#
#                         --- PTSO-Exchange ---
#
# Contributors: @Carter2565#5594, 
# PTSO-Exchange api webserver.
# Api.py is just the webserver Extensions.py contains all main functions
#
#-----------------------------------------------------------------------#

from http.server import BaseHTTPRequestHandler, HTTPServer
from main.py import response
import time
import json

class Server(BaseHTTPRequestHandler):
  def _set_response(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/json')
    self.end_headers()

  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-type", "text/json")
    self.end_headers()

    content = response((self.path)[7:])
    self.wfile.write(bytes(content, "utf-8"))

    try:
      print(json.loads(str(self.path)[7:]))
    except json.decoder.JSONDecodeError:
      print('400 - No json data')


class webserver:
  def __init__(self, ip, port):
    self.hostName = ip
    self.serverPort = port
  
  def stert():
    server = HTTPServer((self.hostName, self.serverPort), Server)
    print("[Python API] -- Server started http://%s:%s" % (self.hostName, self.serverPort) + '\n')

    try:
      server.serve_forever()
    except KeyboardInterrupt:
      pass

    server.server_close()
    print("[Python] -- Server stopped.")