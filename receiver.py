import socket
import time
from protocol import unpack_full, FULL_SIZE

HOST = "0.0.0.0"
PORT = 9999

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))

    expected_seq = 0

    print("[Receiver] Listening for packets...")

    while True:
        data, addr = sock.recvfrom(1024)

        # Defensive check
        if len(data) != FULL_SIZE:
            print(f"[Receiver] Bad packet size from {addr}")
            continue

        seq, sent_time, value = unpack_full(data)
        now = time.time()
        latency_ms = (now - sent_time) * 1000

        # Packet loss detection
        if seq != expected_seq:
            print(f"[Receiver] LOSS: expected {expected_seq}, got {seq}")

        expected_seq = seq + 1

        print(
            f"[Receiver] seq={seq} "
            f"value={value} "
            f"latency={latency_ms:.2f} ms"
        )

if __name__ == "__main__":
    main()
