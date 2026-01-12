import socket
import time
from protocol import pack_full

HOST = "127.0.0.1"
PORT = 9999

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    seq = 0
    value = 0.0

    print("[Sender] Sending sequence + timestamp + value")

    while True:
        timestamp = time.time()
        packet = pack_full(seq, timestamp, value)

        sock.sendto(packet, (HOST, PORT))
        print(f"[Sender] seq={seq} value={value}")

        seq += 1
        value += 0.5
        time.sleep(1)

if __name__ == "__main__":
    main()
