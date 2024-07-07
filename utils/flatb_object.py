from typing import Protocol


class HasGetRootAs(Protocol):
    @classmethod
    def GetRootAs(cls, buf: bytes, offset: int) -> 'HasGetRootAs':
        ...