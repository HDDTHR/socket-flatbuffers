import socket
import logging
import struct

from utils.packet.message_packet import MessagePacket
from utils.packet.rsa_packet import RSAPacket

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
    logging.info(struct.unpack("bbb", version_data))

    packets = [
        MessagePacket("Good morning"),
        MessagePacket("Starshine,"),
        MessagePacket("the earth says"),
        MessagePacket("Hello!"),
        RSAPacket(7003995859407499,
                  7754608596439589)
    ]

    for packet in packets:
        packet.send(sock)

    sock.close()

if __name__ == "__main__":
    main()