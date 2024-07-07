from socket import socket
from utils.flatb.d_message import d_message
from utils.base_packet_handler import BasePacketHandler


class MessagePacketHandler(BasePacketHandler):
    def __init__(self):
        super().__init__(0x01, d_message)
    