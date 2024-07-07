import logging
from math import gcd
from typing import Tuple, override
from utils.exception.packet_handler_execution_exception import PacketHandlerExecutionException
from utils.flatb.DRSA import DRSA
from utils.base_packet_handler import BasePacketHandler

class RsaPacketHandler(BasePacketHandler):
    def __init__(self):
        super().__init__(DRSA)

    @override
    def _identifier():
        return 0x0002
    
    def generate_rsa_object(self, p: int, q: int) -> Tuple[int, int, int]:
        e = 65537
        n = p * q
        phi = (p - 1) * (q - 1)
        if gcd(e, phi) != 1:
            raise PacketHandlerExecutionException("GCD of e and phi isnt equal to one! ")
        d = pow(e, -1, phi)
        return (e, n, d,)
    
    @override
    def execute(self):
        (e, n, d,) = self.generate_rsa_object(self._data.P(), self._data.Q())  # type: ignore
        logging.info(f"{{e: {e}, n: {n}, d: {d}}}")
    