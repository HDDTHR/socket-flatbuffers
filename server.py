import socket
import struct
import struct
import logging

from utils.constants import MAJOR, MINOR, PATCH
from utils.exception.packet_handler_not_known_exception import PacketHandlerNotKnownException
from utils.packet_handler_registrar import PacketHandlerRegistrar

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler()
    ]
)

def main():
    PacketHandlerRegistrar.init()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 1104))
    sock.listen(5)
    while True:
        print("Waiting for a new connection!")
        conn, _ = sock.accept()

        try:
            # Initialization Phase
            conn.send(struct.pack("bbb", MAJOR, MINOR, PATCH))

            # Communication Phase
            while True:
                data = conn.recv(4)
                if not data:
                    break

                id = struct.unpack("I", data)[0]
                try:
                    packet_handler = PacketHandlerRegistrar.handle_packet(id)
                    packet_handler.handle_socket(conn)
                    packet_handler.execute()
                except PacketHandlerNotKnownException as e:
                    logging.warning(f"Identifier {id} not found in the PacketRegistrar, disconnecting client..")
                    break  # Exit the loop to wait for a new connection
        except Exception as e:
            logging.error(f"An error occurred: {e}")
        finally:
            conn.close()
            logging.info("Socket reset!")

if __name__ == "__main__":  
    main()
