import logging
from typing import override
from utils.flatb.DMessage import DMessage
from utils.base_packet_handler import BasePacketHandler

class MessagePacketHandler(BasePacketHandler):
    def __init__(self):
        super().__init__(DMessage)

    @override
    def _identifier():
        return 0x0001
    
    @override
    def execute(self):
        logging.info(f"Message - {self._data.Text()}") # type: ignore *pain in the ass to add type*