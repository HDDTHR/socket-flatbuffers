import socket
import struct
from sys import version

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 1104))

# Initialization Phase
version_data = bytes()
while not version_data:
    version_data += sock.recv(3)

major, minor, patch = struct.unpack("bbb", version_data)
print(major, minor, patch)


# Communication Phase
cmds = ['A', 'B', 'C']

for cmd in cmds:
    sock.send(cmd.encode())

sock.close()