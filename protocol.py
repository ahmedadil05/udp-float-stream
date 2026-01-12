import struct

# V3: Sequence + timestamp + float
FULL_FORMAT = "!Idf"  # uint32 + double + float32
FULL_SIZE = struct.calcsize(FULL_FORMAT)

def pack_full(seq: int, timestamp: float, value: float) -> bytes:
    """Full packet with timing (16 bytes)"""
    return struct.pack(FULL_FORMAT, seq, timestamp, value)

def unpack_full(data: bytes):
    """Extract seq, timestamp, and value"""
    if len(data) != FULL_SIZE:
        raise ValueError(f"Invalid packet size: expected {FULL_SIZE}, got {len(data)}")
    return struct.unpack(FULL_FORMAT, data)