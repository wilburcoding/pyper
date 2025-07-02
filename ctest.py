# testing client side stuff
import socket

import json 
HOST = "127.0.0.1" 
PORT = 56726 
import random
import uuid
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#sent test message every second just for some testing (for now)
import time
s.sendall(json.dumps({"type": "join"}).encode())
while True:
  data = s.recv(1024)
  print(f"Received {data!r}")
  dat = json.loads(data.decode())
  if (dat["state"] == "play" and dat["countdown"] == 55):
    s.sendall(json.dumps({"type": "res", "id": str(uuid.uuid4()), "name":"Guest" + str(random.randint(1,1000)), "speed":str(random.randint(1,10))}).encode())
  