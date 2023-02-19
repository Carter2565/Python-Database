#-----------------------------------------------------------------------#
#                         --- Python Database ---
#
# Contributors: @Carter2565#5594, 
# This is the current database for PTSO-Exchange.
# This project can be used as a template for any python database.
#
#-----------------------------------------------------------------------#

from settings import settings 
from database import database
import threading
import requests
import time 
import json


data = {"operation":"set","request":"profile","asset":None,"login":"2565tube@gmail.com","pwd":"098f6bcd4621d373cade4e832627b4f6","fname":None,"lname":None,"username":"Carter2565","data":"{\"fname\":\"Carter\",\"lname\":\"Blair\",\"owned\":[0,1,2,3,4,5],\"created\":[0,1,2,3,4,5],\"servertags\":[\"Site Owner\"],\"usertags\":[\"CDS\",\"Test\"],\"about\":\"This is Carter's about page\",\"pfp\":\"Carter2565.pfp.gif\"}"}
num_threads = 5000


def read_log():
	# read the log file and add the elapsed times to a list
	with open('request_log.txt', "r") as log_file:
		elapsed_times = [float(line.strip()) for line in log_file]
		lines = len(log_file.readlines())

	with open(r"request_log.txt", 'r') as fp:
		x = len(fp.readlines())
		print('Total lines:', x)

	# calculate the average elapsed time
	avg_time = sum(elapsed_times) / len(elapsed_times)
	# print(lines)
	print(f"Average time elapsed: {avg_time}")

def request():
	try:
		start_time = time.time()
		# response = requests.post(f"http://{settings.server.ip}:{settings.server.port}", json = json.loads(data))
		response = requests.post(f"http://{settings.server.ip}:{settings.server.port}", json = data)
		response = response.json()
		end_time = time.time()
		elapsed_time = end_time - start_time
		print(f"Thread {threading.current_thread().name}")
		with open("request_log.txt", "a") as log_file:
			log_file.write(f"{elapsed_time}\n")
	except:
		pass

for i in range(num_threads):
	thread = threading.Thread(target=request)
	thread.start()

time.sleep(0.125 * (num_threads/10))
read_log()

  
  
