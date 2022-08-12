from dataclasses import dataclass
import pickle
import struct
import asyncio
from dotenv import load_dotenv
from os import getenv

load_dotenv()
HOST, PORT = "0.0.0.0", "9999"
MYSQL_DATABASE = getenv("MYSQL_DATABASE")
MYSQL_USER = getenv("MYSQL_USER")
MYSQL_ROOT_PASSWORD = getenv("MYSQL_ROOT_PASSWORD")
MYSQL_HOST = getenv("MYSQL_HOST")
MYSQL_PORT = getenv("MYSQL_PORT")
SCHEDULE_INTERVAL = 10

clients = []


@dataclass
class Client:
    trashbin_id: str
    writer: asyncio.StreamWriter


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


async def handle(reader, writer):
    data = await read_data(reader)
    if data is None:
        return

    trashbin_id = data["id"]
    for client in clients:
        if client.trashbin_id == trashbin_id:
            print(f"trashbin id ({trashbin_id}) already exists")
            writer.close()
            return

    clients.append(Client(trashbin_id, writer))
    print(f"connection open {trashbin_id}")

    try:
        while True:
            data = await read_data(reader)
            if data is None:
                break

            # mariadb call

            print(f"{trashbin_id} wrote: {data}")
            if data["type"] == "rfid_tag":
                await write_data(
                    writer,
                    {
                        "type": "rfid_auth",
                        "user_type": "manager",
                        "user_id": "0987654321",
                    },
                )
            else:
                await write_data(writer, data)
    except ConnectionResetError:
        pass
    finally:
        client_idx = -1
        for idx, client in enumerate(clients):
            if client.trashbin_id == trashbin_id:
                client_idx = idx

        del clients[client_idx]
        print(f"connection closed {trashbin_id}")


async def schedule_coroutine(client):
    data = {"type": "stat", "detail": client.trashbin_id}
    await write_data(client.writer, data)


async def schedule():
    while True:
        tasks = (schedule_coroutine(client) for client in clients)
        await asyncio.gather(*tasks)
        await asyncio.sleep(SCHEDULE_INTERVAL)


async def main():
    server = await asyncio.start_server(handle, HOST, PORT)
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    await asyncio.gather(server.serve_forever(), schedule())


if __name__ == "__main__":
    asyncio.run(main())
