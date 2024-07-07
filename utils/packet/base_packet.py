import socket
import struct
from typing import final
from abc import ABC, abstractmethod

class BasePacket(ABC):
    def __init__(self, identifier: int):
        self.identifier = identifier

    @property
    @abstractmethod
    def _raw_data(self) -> bytes:
        pass
    
    def handle_socket(self, sock: socket.socket) -> None:
        sock.sendall(self._raw_data)

    @final
    def send(self, sock: socket.socket) -> None:
        sock.sendall(struct.pack("I", len(self._raw_data)))
        self.handle_socket(sock)