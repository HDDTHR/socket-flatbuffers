from functools import cached_property
from typing import override
import flatbuffers
from utils.flatb import DMessage
from utils.base_packet import BasePacket

class MessagePacket(BasePacket):
    def __init__(self, text: str):
        super().__init__(0x0001)
        self.__text = text

    @cached_property
    @override
    def _raw_data(self):
        builder = flatbuffers.Builder(0)
        text = builder.CreateString(self.__text)

        DMessage.Start(builder)
        DMessage.DMessageAddText(builder, text)
        message = DMessage.End(builder)

        builder.Finish(message)
        return builder.Output()
