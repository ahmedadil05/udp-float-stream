import struct

# Network protocol definition
# !  -> network byte order (big-endian)
# f  -> 32-bit floating point number
FORMAT = "!f"
SIZE = struct.calcsize(FORMAT)

def pack_float(value: float) -> bytes:
    """
    Convert a Python float into network-safe bytes.
    """
    return struct.pack(FORMAT, value)

def unpack_float(data: bytes) -> float:
    """
    Convert network bytes back into a Python float.
    """
    if len(data) != SIZE:
        raise ValueError(f"Invalid packet size: expected {SIZE}, got {len(data)}")
    return struct.unpack(FORMAT, data)[0]
