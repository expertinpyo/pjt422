# 초기값 세팅
from dotenv import load_dotenv
from os import getenv
import socket
import pickle
import struct
from time import sleep

load_dotenv()
HOST, PORT = getenv("HOST", "localhost"), int(getenv("PORT", "9999"))


class MySocket(socket.socket):
    def __init__(self, *args, **kwargs):
        super(MySocket, self).__init__(*args, **kwargs)

    def send_data(self, data):
        packet = pickle.dumps(data)
        length = struct.pack("!I", len(packet))
        packet = length + packet
        self.sendall(packet)

    def recv_data(self):
        buf = self.recv(4)
        if len(buf) == 0:
            return None

        length = struct.unpack("!I", buf)[0]

        buf = self.recv(length)
        if len(buf) == 0:
            return None

        return pickle.loads(buf)


sock = MySocket(socket.AF_INET, socket.SOCK_STREAM)


def main():
    count = 1

    while True:
        # Connect to server and send data
        data = {"name": "client", "detail": "hello world", "count": count}
        sock.send_data(data)
        count += 1

        received = sock.recv_data()
        if received is None:
            break

        print(f"Sent:     {data}")
        print(f"Received: {received}")

        sleep(3)


if __name__ == "__main__":
    try:
        sock.connect((HOST, PORT))
        main()
    except Exception as e:
        print(e)
    finally:
        sock.close()
