import socket
import struct
from typing import Any, final, Type
from abc import ABC, abstractmethod

class BasePacketHandler(ABC):
    @staticmethod
    @abstractmethod
    def _identifier():
        pass

    def __init__(self, data_class: Type[Any]):
        self.__data = None
        self.__data_class = data_class
    
    def handle_socket(self, sock: socket.socket) -> Any:
        payload_size = struct.unpack("I", sock.recv(4))[0]
        raw_data = sock.recv(payload_size)
        return self.__data_class.GetRootAs(raw_data)

    @final
    def receive(self, sock: socket.socket) -> None:
        self.handle_socket(sock)