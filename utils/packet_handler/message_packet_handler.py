from socket import socket
from utils.flatb.DMessage import DMessage
from utils.packet_handler.base_packet_handler import BasePacketHandler


class MessagePacketHandler(BasePacketHandler):
    def __init__(self):
        super().__init__(0x01, DMessage)
    