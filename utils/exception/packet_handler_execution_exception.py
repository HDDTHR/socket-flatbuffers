class PacketHandlerExecutionException(Exception):
    def __init__(self, message: str = "Execution error!"):
        super().__init__(message)