from dataclasses import dataclass
import pickle
import struct
import asyncio
from dotenv import load_dotenv
from os import getenv
import pymysql
import pymysql.cursors

import logging
from datetime import date

# 오늘 날짜 확인
year = str(date.today().year)
month = str(date.today().month) if len(str(date.today().month)) == 2 else '0' + str(date.today().month)
day = str(date.today().day) if len(str(date.today().day)) == 2 else '0' + str(date.today().day)
tday = year + month + day
# 로그 데이터를 위한 변수 선언
logger = logging.getLogger()
# Level INFO로 설정
logger.setLevel(logging.INFO)
# 로그데이터 형식
formatter = logging.Formatter('%(asctime)s %(messages)s')
# 오늘날짜.log로 저장
file_handler = logging.FileHandler(f'{tday}.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


load_dotenv()

# DB 연결
def dbconnect():

    conn = pymysql.connect (
        host = getenv("MYSQL_HOST"), user = getenv("MYSQL_USER"), password= getenv("MYSQL_ROOT_PASSWORD"),
        db=getenv("MYSQL_DATABASE"), port =int(getenv("MYSQL_PORT")),  charset="utf8", cursorclass=pymysql.cursors.DictCursor
    )
    print(conn)
    return conn



# #rf00000001

# 학생이면 학생 아이디 할당 (학생 아이디가 student_pk인지, 학번(student_num)인지)
# rfid_num으로 신원 확인
def check_rfid(conn, rfid):
    cur = conn.cursor()
    sql = 'SELECT * FROM campus_student WHERE rfid_num = %s'
    cur.execute(sql,[rfid])
    result = cur.fetchone()  # fetchone()은 한줄씩 읽어오는 것 / fetchall()은 한번에 읽어오는 것
    print(result)
    if result != None:  # 학생이라는 뜻
        user = {'id': result['student_num'], 'is_manager': False}
    else:
        sql = 'SELECT *  FROM accounts_user WHERE rfid_num = %s'
        cur.execute(sql,[rfid])
        result = cur.fetchone()
        if result != None:
            user = {'id': result['student_num'], 'is_manager': True}
        else:
            user = {'id': None, 'is_manager': True}
    print(user)
    return {'user': user}
            
    
# # 최종 상태를 클라이언트로부터 받은 다음 그걸 DB에 업데이트
def update_data(conn, token, amount):
    cur = conn.cursor()
    sql = 'UPDATE campus_trashbin SET amount = %s WHERE token = %s'
    cur.execute(sql, (amount, token)) 
    #conn.commit()
    # db에 amount 업데이트 한 후에 status도 업데이트해줘야 함
    sql2 = 'UPDATE campus_trashbin SET status = CASE WHEN amount >= 0.7 THEN "WAR" WHEN amount >= 0.3 THEN "CAU" ELSE "SAF" END WHERE token = %s'
    cur.execute(sql2, (token))

    sql3 = 'SELECT tr.token, tr.trash_type, tr.group_id, gr.floor_id, fl.building_id FROM campus_trashbin AS tr INNER JOIN campus_group AS gr ON tr.group_id = gr.id INNER JOIN campus_floor AS fl ON gr.floor_id = fl.id WHERE tr.token = %s' 
    cur.execute(sql3, (token))
    result = cur.fetchone()
    trash_type = result['trash_type']
    group_id = result['group_id']
    floor_id = result['floor_id']
    building_id = result['building_id']
    logger.info(f'{building_id} {floor_id} {group_id} {token} {trash_type}')

    conn.commit()  # 데이터베이스 정보에 변동을 주는 내용이므로 commit() 필수


# 2. (타이머) client에 trashbin_type 넘기기 
def get_type(conn, token):
    cur = conn.cursor()
    sql = 'SELECT trash_type FROM campus_trashbin WHERE token = %s'
    cur.execute(sql, (token))
    result = cur.fetchone()  
    
    return(result['trash_type'])


# 관리자면 cleanrecord에 추가하기 => 관리자가 비울때만 (즉, 최종에서 amount == 0이 될때)
def add_discard_user(conn, trashbin_id, user_id):
    cur = conn.cursor()
    sql = 'INSERT INTO campus_cleanrecord (updated_at, trashbin_id, user_id) VALUES(now(), %s, %s)'
    cur.execute(sql, (trashbin_id, user_id))
    conn.commit()


# 4. 여러개의 client에 데이터를 넘기기 위해 세트를 찾아야 함 
# query... client_id -> 세트[client_id] 리스트 client_id_list
def find_set(conn, token):
    client_list = []
    cur = conn.cursor()
    sql = 'SELECT token FROM campus_trashbin WHERE group_id = (SELECT group_id FROM campus_trashbin WHERE token = %s)'
    cur.execute(sql, (token))
    result = cur.fetchall()  # [{'token': '1B21'}, {'token': '1B22'}, {'token': '1B23'}]
    print(result)  
    for i in range(len(result)):
        client_list.append(result[i]['token'])
    print(client_list)
    return client_list     # ['1B21', '1B22', '1B23']
    

# 해당 쓰레기통의 현재 양 조회
def get_amount(conn, token):
    cur = conn.cursor()
    sql = 'SELECT amount FROM campus_trashbin WHERE token = %s'
    cur.execute(sql, (token))
    result = cur.fetchone()
    print(result)
    return result['amount']

# def main():
#     conn = dbconnect()
#     print('연결완료')
#     get_amount(conn, '1B21')
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

conn = dbconnect()

clients = []  # 현재 서버랑 통신중인 모든 쓰레기통


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
    global conn 
    data = await read_data(reader)  
    if data is None:  # 전원 연결이 안되었을 때
        writer.close()
        return

    if data["type"] != "init":
        writer.close()
        return

    client_id = data["id"]
    # 중복체크
    for client in clients:
        if client.id == client_id:
            print(f"trashbin id ({client_id}) already exists")
            writer.close()
            return

    # query... data["amount"] 업데이트  => 부팅시 받은 amount를 update 
    if get_amount(conn, client_id) != data["amount"]:
        update_data(conn, client_id, data["amount"])

    clients.append(Client(client_id, writer))
    print(f"connection open {client_id}")

    try:
        while True:
            data = await read_data(reader)
            if data is None:
                break

            print(f"{client_id} wrote: {data}")


            # 3. (rfid 태그 + 문열기 요청) / 4. 문열기 응답
            if data["type"] == "door_open":
                # query... rfid check
                user = check_rfid(conn, data["rfid"])
                is_rfid_ok = True
                if user["id"] == None:  
                    is_rfid_ok = False
                
                if is_rfid_ok:
                    # query... client_id -> 세트[client_id] 리스트 client_id_list
                    client_id_list = find_set(conn, client_id)
                    #client_id_list = [client_id, ]
                    for client in clients:
                        data = {
                            "type": "door_open",
                            "user": user
                        }
                        if client.id in client_id_list:
                            await write_data(client.writer, data)

            # 5. 문닫기 요청 / 6. 문닫기 응답
            if data["type"] == "door_close":
                client_id_list = find_set(conn, client_id)
                for client in clients:
                    data = {
                        "type": "door_close",
                    }
                    if client.id in client_id_list:
                        await write_data(client.writer, data)
            
            # 7. 최종 상태 보내기
            if data["type"] == "stat":
                update_data(conn, client_id, data["amount"])
                if get_amount(conn, client_id) == 0 and data["user"]["is_manager"]:
                    add_discard_user(conn, client_id, data["user"]["user_id"])
    

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
    global conn
    trashbin_type = get_type(conn, client.id)
    data = {"type": "stat", "trashbin_type": trashbin_type}
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
    conn.close()


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