# 초기값 세팅
from dotenv import load_dotenv
from os import getenv
import pickle
import struct
import asyncio

load_dotenv()
HOST, PORT = getenv("HOST", "localhost"), int(getenv("PORT", "9999"))

status = {
    "id": "",
    "trashbin_type": "",
    "rfid": {
        "id": "",
        "is_tagged": False
    },
    "user": {
        "id": "",
        "is_manager": False
    },
    "door": {
        "is_top_open": False,
        "is_bottom_open": False
    },
    "trash_amount": 0,
}


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


async def socket_listener(reader, writer):
    while True:
        data = await read_data(reader)
        if data is None:
            exit(0)

        if data["type"] == "stat":
            status["trashbin_type"] = data["trashbin_type"]

        if data["type"] == "door_open" and not status["door"]["is_top_open"]:
            # open_top_door()
            status["user"] = data["user"]
            status["door"]["is_top_open"] = True

        if data["type"] == "door_close" and status["door"]["is_top_open"]:
            # close_top_door()
            status["door"]["is_top_open"] = False
            # if status["door"]["is_bottom_open"]:
            #   close_bottom_door()
            #   status["door"]["is_bottom_open"] = False

            await write_data(writer, {
                "type": "stat",
                "amount": status["trash_amount"]
            })

        print(f"Received: {data}")


async def device_loop(writer):
    while True:
        # ...some logic

        # if rfid tagged
        rfid = "123456789"

        await write_data(writer, {
            "type": "door_open",
            "rfid": rfid,
        })

        status["rfid"]["id"]= rfid
        status["rfid"]["is_tagged"] = True


        await asyncio.sleep(0.1)


async def main():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    await write_data(writer, {"id": "1234", "type": "init"})
    data = await read_data(reader)
    if data is None:
        return
    if data["type"] != "init":
        return

    status["trashbin_type"] = data["trashbin_type"]

    await asyncio.gather(
        device_loop(writer), socket_listener(reader, writer)
    )


if __name__ == "__main__":
    asyncio.run(main())
