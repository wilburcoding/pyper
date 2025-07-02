# testing client side stuff
import socket

import json 
HOST = "127.0.0.1" 
PORT = 56726 

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#sent test message every second just for some testing (for now)
import time
while True:
  time.sleep(1)
  s.sendall(json.dumps({"jj": "test"}).encode())
  data = s.recv(1024)
  print(f"Received {data!r}")
  
