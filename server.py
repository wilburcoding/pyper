import socket
import threading
import json
import threading
import time
HOST = "127.0.0.1"
PORT = 56726 
game = {}
conns = []
def handle_client(conn, addr):
    print(f"Connected by {addr}")
    with conn:
        conns.append(conn)
        while True:
            data = conn.recv(1024)  
            if not data:
                break
            print(f"Received from {addr}: {data.decode()}")
            jdat = json.loads(data.decode())
            payload = []
            conn.sendall(json.dumps({"res": data.decode()}).encode()) 
            print(f"Sent to {addr}: {data.decode()}")
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
    while True:
        print("This is printed every second")
        time.sleep(1)


threading.Thread(target=manage, daemon=True).start()

start_server()
