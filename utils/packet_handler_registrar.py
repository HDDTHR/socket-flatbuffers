from __future__ import annotations
from typing import TYPE_CHECKING, Type
if TYPE_CHECKING:
    from utils.base_packet_handler import BasePacketHandler

from utils.base_packet import BasePacket
from utils.constants import ROOT_DIR
from utils.exception.packet_handler_not_known_exception import PacketHandlerNotKnownException
import os
import importlib, importlib.util
import inspect


class PacketHandlerRegistrar(object):
    __known_packets = {}

    @classmethod
    def __register_packet(cls, packet_class: Type[BasePacketHandler]):
        cls.__known_packets[packet_class._identifier()] = packet_class

    @classmethod
    def init(cls):
        directory = f'{ROOT_DIR}/packet_handler'
        for filename in os.listdir(directory):
            if filename.endswith('.py'):
                module_name = filename[:-3]
                file_path = os.path.join(directory, filename)
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                if spec:
                    module = importlib.util.module_from_spec(spec)
                    loader = spec.loader
                    if loader:
                        loader.exec_module(module)
                        for name, obj in inspect.getmembers(module, inspect.isclass):
                            if obj.__module__ == module.__name__:
                                handler: Type[BasePacketHandler] = obj
                                cls.__register_packet(handler)

    @classmethod
    def handle_packet(cls, packet_identifier) -> BasePacketHandler:
        try:
           return cls.__known_packets[packet_identifier]()
        except KeyError as e:
            raise PacketHandlerNotKnownException()

    def __init__(self):
        raise RuntimeError()