# 초기값 세팅
from dotenv import load_dotenv
from os import getenv
import pickle
import struct
import asyncio
from time import time

from lib.helper import (
    set_gpio_for_front_door,
    set_gpio_for_capacity_check,
    set_display_lcd,
    get_deviceID,
    display_lcd,
    unlock_front_door,
    lock_front_door,
    the_last_action,
    current_capacity_rate,
    pass_auth,
    fail_auth,
    getuserID,
    is_btn_pressed,
)

load_dotenv()
HOST, PORT = getenv("HOST", "localhost"), int(getenv("PORT", "9999"))

OPEN_TIMEOUT = 30

pwm = set_gpio_for_front_door()
set_gpio_for_capacity_check()
lcd = set_display_lcd()

status = {
    "id": get_deviceID(),
    "trashbin_type": "",
    "rfid": {"id": "", "last_tagged_time": time()},
    "user": {},
    "door": {"is_slide_open": False, "is_front_unlock": False, "open_time": time()},
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
        print(data)
        if data is None:
            # 연결 끊어짐
            exit(0)

        if data["type"] == "stat":
            status["trashbin_type"] = data["trashbin_type"]

        if data["type"] == "door_open" and not status["door"]["is_slide_open"]:
            await pass_auth()
            status["user"] = data["user"]
            status["door"]["is_slide_open"] = True
            status["door"]["open_time"] = time()
            
        if data["type"] == "fail_auth" and not status["door"]["is_slide_open"]:
            await fail_auth()

        if data["type"] == "front_unlock" and not status["door"]["is_front_unlock"]:
            await unlock_front_door(pwm)
            status["door"]["is_front_unlock"] = True

        if data["type"] == "door_close" and status["door"]["is_slide_open"]:
            if status["door"]["is_front_unlock"]:
                await lock_front_door(pwm)
                status["door"]["is_front_unlock"] = False
            await the_last_action()
            status["door"]["is_slide_open"] = False
            status["trash_amount"] = await current_capacity_rate()

            await write_data(
                writer,
                {
                    "type": "stat",
                    "amount": status["trash_amount"],
                    "user": status["user"],
                },
            )

        # print(f"Received: {data}")


async def device_loop(writer):
    while True:
        # 슬라이드가 열려있고
        # 앞쪽문이 잠겨있고
        # OPEN_TIMEOUT 시간만큼 경과했을 때
        # -> 서버에 문 닫기 신호를 보냄
        if (
            status["door"]["is_slide_open"]
            and not status["door"]["is_front_unlock"]
            and (time() - status["door"]["open_time"]) >= OPEN_TIMEOUT
        ):
            await write_data(
                writer,
                {"type": "door_close"},
            )

        # 버튼이 눌렸고
        # 슬라이드가 열려있고
        # 앞쪽문이 잠겨있을 때
        # -> 앞쪽 문 열기 신호를 보냄
        if (
            is_btn_pressed()
            and status["door"]["is_slide_open"]
            and not status["door"]["is_front_unlock"]
        ):
            await write_data(
                writer,
                {"type": "front_unlock", "user": status["user"]},
            )

        # 버튼이 눌렸고
        # 앞쪽문이 열려있을 때
        # -> 문 닫기 신호를 보냄
        if is_btn_pressed() and status["door"]["is_front_unlock"]:
            await write_data(
                writer,
                {"type": "door_close"},
            )

        # 슬라이드가 닫혀있고
        # rfid 값이 존재하고
        # (이전 값이랑 다름 or 태그한지 1초 이상 경과)했을 때
        # -> 서버에 rfid와 함께 문 열기 신호를 보냄
        rfid = getuserID()
        if (
            not status["door"]["is_slide_open"]
            and rfid
            and (
                rfid != status["rfid"]["id"]
                or (time() - status["rfid"]["last_tagged_time"]) >= 1
            )
        ):
            await write_data(
                writer,
                {
                    "type": "door_open",
                    "rfid": rfid,
                },
            )
        if rfid:
            status["rfid"]["id"] = rfid
            status["rfid"]["last_tagged_time"] = time()

        await asyncio.sleep(0.1)


async def main():
    status["trash_amount"] = await current_capacity_rate()
    reader, writer = await asyncio.open_connection(HOST, PORT)
    await write_data(
        writer, {"type": "init", "id": status["id"], "amount": status["trash_amount"]}
    )
    data = await read_data(reader)
    if data is None:
        return
    if data["type"] != "init":
        return

    status["trashbin_type"] = data["trashbin_type"]
    await display_lcd(lcd, status["trashbin_type"])

    await asyncio.gather(device_loop(writer), socket_listener(reader, writer))


if __name__ == "__main__":
    asyncio.run(main())
