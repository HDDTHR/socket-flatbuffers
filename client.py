import socket
import logging
import struct

from utils.packet.message_packet import MessagePacket

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler()
    ]
)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 1104))

    # Receive version
    version_data = sock.recv(3)
    print(struct.unpack("bbb", version_data))

    packets = [MessagePacket("Hello, world!")]

    for packet in packets:
        packet.send(sock)

    sock.close()

if __name__ == "__main__":
    main()