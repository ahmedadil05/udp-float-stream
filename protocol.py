import struct

import struct

# V2: Sequence number + float
SEQ_FLOAT_FORMAT = "!If"  # uint32 + float32
SEQ_FLOAT_SIZE = struct.calcsize(SEQ_FLOAT_FORMAT)

def pack_seq_float(seq: int, value: float) -> bytes:
    """Sequence + float packing (8 bytes)"""
    return struct.pack(SEQ_FLOAT_FORMAT, seq, value)

def unpack_seq_float(data: bytes):
    """Extract sequence and float"""
    if len(data) != SEQ_FLOAT_SIZE:
        raise ValueError(f"Invalid packet size: expected {SEQ_FLOAT_SIZE}, got {len(data)}")
    return struct.unpack(SEQ_FLOAT_FORMAT, data)