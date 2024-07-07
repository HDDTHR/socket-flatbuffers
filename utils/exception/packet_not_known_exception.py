class PacketNotKnownException(Exception):
    def __init__(self):
        super().__init__("Packet not found in PacketRegistrar!")