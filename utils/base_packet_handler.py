import socket
import struct
from typing import Any, Optional, TypeVar, final, Type
from abc import ABC, abstractmethod

from utils.flatb_object import HasGetRootAs

class BasePacketHandler(ABC):
    @staticmethod
    @abstractmethod
    def _identifier():
        pass

    @abstractmethod
    def execute(self):
        pass

    def __init__(self, data_class: Type['T']):
        self._data : Optional[T] = None
        self.__data_class : Type[T] = data_class
    
    def handle_socket(self, sock: socket.socket) -> Any:
        payload_size = struct.unpack("I", sock.recv(4))[0]
        raw_data = sock.recv(payload_size)
        self._data =  self.__data_class.GetRootAs(raw_data, 0)

    @final
    def receive(self, sock: socket.socket) -> None:
        self.handle_socket(sock)

T = TypeVar('T', bound=HasGetRootAs)
