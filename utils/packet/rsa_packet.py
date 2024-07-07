from functools import cached_property
from typing import override
import flatbuffers
from utils.flatb import DRSA
from utils.base_packet import BasePacket

class RSAPacket(BasePacket):
    def __init__(self, p: int, q: int):
        super().__init__(0x0002)
        self.__p = p
        self.__q = q

    @cached_property
    @override
    def _raw_data(self):
        builder = flatbuffers.Builder(0)

        DRSA.Start(builder)
        DRSA.DRSAAddP(builder, self.__p)
        DRSA.DRSAAddQ(builder, self.__q)
        pq = DRSA.End(builder)

        builder.Finish(pq)
        return builder.Output()
