import socket
import threading
import json
import threading
import time
import random
leaderboard = {}
wlist = []
with open('words.txt', 'r') as file:
    for line in file:
        processed_line = line.strip()
        if (len(processed_line) > 2 and "'" not in processed_line):
            wlist.append(processed_line)
HOST = "127.0.0.1"
PORT = 56726 
game = {"state":"wait", "results":{}, "words":"","countdown":0}
conns = []
countdown = 15
def handle_client(conn, addr):
    global leaderboard
    print(f"Connected by {addr}")
    with conn:
        while True:
            data = conn.recv(1024)  
            if not data:
                break
            print(f"Received from {addr}: {data.decode()}")
            jdat = json.loads(data.decode())
            payload = {}

            if (jdat["type"] == "join" and (game["state"] == "wait" or game["state"] == "countdown")):
              conns.append(conn)
              pass
            elif (jdat["type"] == "res"):
                # game result
                jdat["speed"] = int(jdat["speed"])
                game["results"][jdat["id"]] = {"speed":jdat["speed"], "name":jdat["name"]}
                if (jdat["name"] in list(leaderboard.keys())):
                    if (jdat["speed"] > leaderboard[jdat["name"]]):
                        leaderboard[jdat["name"]] = jdat["speed"]
                else:
                    leaderboard[jdat["name"]] = jdat["speed"]
                pass
            elif (jdat["type"] == "leaderboard"):
                sorted_l = sorted(
                    leaderboard.items(), key=lambda item: item[1], reverse=True)
                sorted_l_dict = dict(sorted_l)
                #get only first 5 items
                leaderboard = dict(list(sorted_l_dict.items())[:5])
                conn.sendall(json.dumps({"leaderboard":leaderboard,"state":"l"}).encode())
            else:
                conn.sendall(json.dumps({"state":"ongoing"}).encode())
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

def manage():
    # will do game managing stuff while this is running
    global countdown, game, conns
    while True:
        if (game["state"] == "wait"):
            # waiting for players
            if (len(conns) > 0):
                print("Starting game!")
                game["state"] = "countdown"
            countdown = 15
            ranwords = [random.choice(wlist)
                        for i in range(10)]
            game["words"] = " ".join(ranwords)
            game["results"] = {}
            pass
        elif (game["state"] == "countdown"):
            if (countdown == 0):
                game["state"] = "play"
                countdown = 60
                print("Starting game with " + str(len(conns))  + " players")
            else:
              countdown-=1
        elif (game["state"] == "play"):
            if (countdown == 0 or len(list(game["results"].keys())) == len(conns) or len(conns) == 0):
                print("Game over with results: " + str(game["results"]))
                game["state"] = "results"
                countdown = 5
            else:
              if (countdown % 15 == 0):
                  print("Countdown: " + str(countdown))
              countdown-=1
        elif (game["state"] == "results"):
            if (countdown == 0):
                game["state"] = "wait"
                conns = []
            else:
                countdown-=1
        game["countdown"] = countdown
        for conn in conns[:]: 
          try:
              conn.sendall(json.dumps(game).encode())
          except Exception as e:
              print(e)
              conns.remove(conn)
        time.sleep(1)

threading.Thread(target=manage, daemon=True).start()

start_server()