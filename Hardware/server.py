from dataclasses import dataclass
import pickle
import struct
import asyncio
from dotenv import load_dotenv
from os import getenv
import pymysql
import pymysql.cursors

load_dotenv()

# DB 연결
def dbconnect():

    conn = pymysql.connect (
        host = getenv("MYSQL_HOST"), user = getenv("MYSQL_USER"), password= getenv("MYSQL_ROOT_PASSWORD"),
        db=getenv("MYSQL_DATABASE"), port =int(getenv("MYSQL_PORT")),  charset="utf8", cursorclass=pymysql.cursors.DictCursor
    )
    return conn



# #rf00000001

# # 수정 필요 => 학생이면 학생 아이디 할당 (질문이 필요해보임)
# # rfid_num으로 신원 확인
# def search_data(conn, rfid):
#     cur = conn.cursor()
#     sql = 'SELECT * FROM campus_student WHERE rfid_num = %s'
#     cur.execute(sql,[rfid])
#     result = cur.fetchone()  # fetchone()은 한줄씩 읽어오는 것 / fetchall()은 한번에 읽어오는 것
#     print(result)
#     if result != None:  # 학생이라는 뜻
#         who = 'student'
#     else:
#         sql = 'SELECT *  FROM accounts_user WHERE rfid_num = %s'
#         cur.execute(sql,[rfid])
#         result = cur.fetchone()
#         if result != None:
#             who = 'manager'
#         else:
#             who = 'unauthorized'
#     return {'who': who}
            
    
# # 최종 상태를 클라이언트로부터 받은 다음 그걸 DB에 업데이트
# def update_data(conn, token, amount):
#     cur = conn.cursor()
#     sql = 'UPDATE campus_trashbin SET amount = %s WHERE token = %s'
#     cur.execute(sql, (amount, token)) 
#     conn.commit()  # 데이터베이스 정보에 변동을 주는 내용이므로 commit() 필수


# # 2. (타이머) client에 trashbin_type 넘기기 
# def get_type(conn, token):
#     cur = conn.cursor()
#     sql = 'SELECT trash_type FROM campus_trashbin WHERE token = %s'
#     cur.execute(sql, (token))
#     result = cur.fetchone()  # token이 unique하므로
#     print(result['trash_type'])

# 4. 여러개의 client에 데이터를 넘기기 위해 세트를 찾아야 함 => backend 모델 수정한 후에 
# query... client_id -> 세트[client_id] 리스트 client_id_list


# def main():
#     conn = dbconnect()
#     print('연결완료')
#     get_type(conn, '1B2GER1')
#     conn.close()
#     print('연결해제')

# if __name__=="__main__":
#     main()

HOST, PORT = "0.0.0.0", 9999
# MYSQL_DATABASE = getenv("MYSQL_DATABASE")
# MYSQL_USER = getenv("MYSQL_USER")
# MYSQL_ROOT_PASSWORD = getenv("MYSQL_ROOT_PASSWORD")
# MYSQL_HOST = getenv("MYSQL_HOST")
# MYSQL_PORT = getenv("MYSQL_PORT")
SCHEDULE_INTERVAL = 10

clients = []


@dataclass
class Client:
    id: str
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
        writer.close()
        return

    if data["type"] != "init":
        writer.close()
        return

    client_id = data["id"]
    for client in clients:
        if client.id == client_id:
            print(f"trashbin id ({client_id}) already exists")
            writer.close()
            return

    # query... data["amount"] 업데이트

    clients.append(Client(client_id, writer))
    print(f"connection open {client_id}")

    try:
        while True:
            data = await read_data(reader)
            if data is None:
                break

            print(f"{client_id} wrote: {data}")

            if data["type"] == "door_open":
                # query... rfid check
                is_rfid_ok = True
                if is_rfid_ok:
                    # query... client_id -> 세트[client_id] 리스트 client_id_list
                    client_id_list = [client_id, ]
                    for client in clients:
                        data = {
                            "type": "door_open",
                            "user": {
                                "id": "",
                                "is_manager": False
                            }
                        }
                        if client.id in client_id_list:
                            await write_data(client.writer, data)
    except ConnectionResetError:
        pass
    finally:
        client_idx = -1
        for idx, client in enumerate(clients):
            if client.id == client_id:
                client_idx = idx

        del clients[client_idx]
        print(f"connection closed {client_id}")


async def schedule_coroutine(client):
    # query... client.id -> trashbin_type
    data = {"type": "stat", "trashbin_type": "data"}
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
















# # rfid_num으로 권한 확인하기 
# def search_data(conn, rfid):
#     cur = conn.cursor()
#     sql = 'SELECT count(rfid_num) as count FROM campus_student WHERE rfid_num = %s'
#     cur.execute(sql,[rfid])
#     result = cur.fetchone()  # fetchone()은 한줄씩 읽어오는 것 / fetchall()은 한번에 읽어오는 것
#     print(result)
#     if result['count'] == 1:  # 학생이라는 뜻
#         return {'who': 'student'}
#     else:
#         sql = 'SELECT COUNT(rfid_num) as count FROM accounts_user WHERE rfid_num = %s'
#         cur.execute(sql,[rfid])
#         result = cur.fetchone()
#         if result['count'] == 1:
#             return {'who': 'manager'}
#         else:
#             return {'who': 'unauthorized'}