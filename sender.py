import socket
import time
from protocol import pack_float, SIZE

HOST = "127.0.0.1"
PORT = 9999

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    value = 0.0
    print("[Sender] Sending float values...")

    while True:
        data = pack_float(value)
        sock.sendto(data, (HOST, PORT))
        print(f"[Sender] Sent {value}")
        value += 0.5
        time.sleep(1)

if __name__ == "__main__":
    main()
