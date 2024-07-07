import socket
import queue
import struct
import threading
import struct

MAJOR = 0
MINOR = 0
PATCH = 1

#q = queue.Queue()

def worker():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 1104))
    sock.listen(5)
    while True:
        print("Waiting for a new socket!")
        conn, _ = sock.accept()

        # Initialization Phase
        conn.send(struct.pack("bbb", MAJOR, MINOR, PATCH))

        # Communication Phase
        cmd = conn.recv(1)
        while cmd:
            print(f"{cmd.decode()} Command Executed!")
            cmd = conn.recv(1)

        print("Socket closed!")
    
#thread = threading.Thread(target=worker, daemon=True).start()

worker()
