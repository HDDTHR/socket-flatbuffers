from typing import override
import flatbuffers
from utils.flatb import DMessage
from utils.packet.base_packet import BasePacket

class MessagePacket(BasePacket):
    def __init__(self, text: str):
        super().__init__(0x01)
        self.__text = text

    @override
    def _raw_data(self):
        builder = flatbuffers.Builder(0)
        DMessage.Start(builder)
        DMessage.DMessageAddText(builder, builder.CreateString(self.__text))
        DMessage.End(builder)
        builder.Finish(builder)
        return 
