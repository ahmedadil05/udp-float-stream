import socket
from protocol import unpack_float, SIZE

HOST = "127.0.0.1"
PORT = 9999

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))

    print(f"[Receiver] Listening on {HOST}:{PORT}")

    while True:
        data, addr = sock.recvfrom(SIZE)
        value = unpack_float(data)
        print(f"[Receiver] {value} from {addr}")

if __name__ == "__main__":
    main()
