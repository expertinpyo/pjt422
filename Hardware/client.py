from dotenv import load_dotenv
from os import getenv
import pickle
import struct
import asyncio

load_dotenv()
HOST, PORT = getenv("HOST", "localhost"), getenv("PORT", "9999")


class Received:
    def __init__(self) -> None:
        self.ready = asyncio.Event()
        self.data = {}


async def write_data(writer, data):
    packet = pickle.dumps(data)
    length = struct.pack("!I", len(packet))
    packet = length + packet
    writer.write(packet)
    await writer.drain()


async def read_data(reader):
    buf = await reader.read(4)
    if len(buf) == 0:
        return None

    length = struct.unpack("!I", buf)[0]

    buf = await reader.read(length)
    if len(buf) == 0:
        return None

    return pickle.loads(buf)


async def socket_listener(reader, received):
    while True:
        data = await read_data(reader)
        if data is None:
            exit(0)

        if data["type"] == "rfid_auth":
            received.data = data
            received.ready.set()

        print(f"Received: {data}")


async def device_loop(writer, received):
    while True:
        # ...some logic

        # rfid tagged

        data = {
            "id": "1234",
            "type": "rfid_tag",
            "rfid": "1234567890",
        }
        await write_data(writer, data)

        await received.ready.wait()
        data = received.data
        received.ready.clear()

        # use rfid data

        await asyncio.sleep(3)


async def main():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    await write_data(writer, {"id": "1234", "type": "init"})

    received = Received()

    await asyncio.gather(
        device_loop(writer, received), socket_listener(reader, received)
    )


if __name__ == "__main__":
    asyncio.run(main())
