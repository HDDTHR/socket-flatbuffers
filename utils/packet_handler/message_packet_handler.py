from typing import override
from utils.flatb.DMessage import DMessage
from utils.base_packet_handler import BasePacketHandler


class MessagePacketHandler(BasePacketHandler):
    @override
    def _identifier():
        return 0x0001

    def __init__(self):
        super().__init__(DMessage)
    