# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatb

import flatbuffers
from flatbuffers.compat import import_numpy
from typing import Any
from typing import Optional
np = import_numpy()

class DMessage(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset: int = 0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = DMessage()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsDMessage(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # DMessage
    def Init(self, buf: bytes, pos: int):
        self._tab = flatbuffers.table.Table(buf, pos)

    # DMessage
    def Text(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def DMessageStart(builder: flatbuffers.Builder):
    builder.StartObject(1)

def Start(builder: flatbuffers.Builder):
    DMessageStart(builder)

def DMessageAddText(builder: flatbuffers.Builder, text: int):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(text), 0)

def AddText(builder: flatbuffers.Builder, text: int):
    DMessageAddText(builder, text)

def DMessageEnd(builder: flatbuffers.Builder) -> int:
    return builder.EndObject()

def End(builder: flatbuffers.Builder) -> int:
    return DMessageEnd(builder)
