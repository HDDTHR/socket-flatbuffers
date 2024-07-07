import socket
import struct
from typing import Any, final, Type, Optional
from abc import ABC, abstractmethod

from utils.packet_registrar import PacketRegistrar

class BasePacketHandler(ABC):
    def __init__(self, identifier: int, data_class: Type[Any]):
        self.__data = None
        self.__data_class = data_class
        PacketRegistrar.register_packet(identifier, self.__class__)

    @property
    @abstractmethod
    def data(self) -> Optional[Any]:
        return self.__data
    
    def handle_socket(self, sock: socket.socket) -> None:
        payload_size = struct.unpack("I", sock.recv(4))[0]
        raw_data = sock.recv(payload_size)
        self.__data_class.GetRootAs(raw_data)

    @final
    def receive(self, sock: socket.socket) -> None:
        self.handle_socket(sock)