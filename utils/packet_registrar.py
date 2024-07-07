
from utils.exception.packet_not_known_exception import PacketNotKnownException


class PacketRegistrar(object):
    __known_packets = {}

    @classmethod
    def register_packet(cls, packet_identifier, packet_class):
        cls.__known_packets[packet_identifier] = packet_class

    @classmethod
    def handle_packet(cls, packet_identifier):
        try:
           return cls.__known_packets[packet_identifier]()
        except KeyError as e:
            raise PacketNotKnownException()

    def __init__(self):
        raise RuntimeError()