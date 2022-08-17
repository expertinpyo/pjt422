import random
import json
import datetime

floors = []
buildings = []
trashbins = []
students = []
groups = []

floor_url = "https://www.cnuh.co.kr/images/pcrc/sub01/sub01_0603_img01.jpg"
belong = ["기숙사", "평생교육관", "자연과학", "경영학", "경제학", "어문학", "체육학"]
building = ["평생교육관", "기숙사", "어학관", "체육관", "중앙도서관"]
floor = ["B1", "1", "2", "3", "4"]
trash_type = ['GER', 'PET', 'CAN', 'GLA', 'PPR']

locations = [[(500, 275, 0), (207, 123, 0),(1020, 350, 1)], [(657, 280, 1), (190, 125, 0), (910, 120, 1)], [(600, 255, 0), (280, 392, 0), (1090, 230, 1)], [(120, 245, 0), (575, 320, 1), (1016, 160, 1)]]

created_at = datetime.datetime.now()
updated_at = datetime.datetime.now()
cnt_building = 2
cnt_floor = 5
cnt_trashbin = 37
py = [
'https://www.kyungnam.ac.kr/sites/cce/images/temp_1617330335815100.jpg',
'https://www.kyungnam.ac.kr/sites/cce/images/temp_1617338550917100.jpg',
'https://www.kyungnam.ac.kr/sites/cce/images/temp_1617330103119100.jpg',
'https://www.kyungnam.ac.kr/sites/cce/images/temp_1617338867376100.jpg'
]

field_1 = {
    'name': building[0],
    'description' : f'이 곳은 {building[0]} 입니다.',
    'created_at' : created_at,
    'updated_at' : updated_at
}

data_1 = {
    'pk' : 1,
    'model' : 'campus.building',
    'fields' : field_1
}
cnt_bin = 1
buildings.append(data_1)
for i in range(4):
    fields_2 = {
            'name' : floor[i],
            'map_path' : py[i],
            'width' : 1334,
            'height': 574,
            'trashbin_size': 20,
            'order': i,    # 층 순서
            'building' : 1,
            'created_at': created_at,
            'updated_at': updated_at
        }
    data_2 = {
        'pk': i+1,
        'model': 'campus.floor',
        'fields': fields_2
    }
    floors.append(data_2)
    gr = 0
    for j in range(3):
        type_list = []
        for k in range(3):
            if i == 1:
                if j == 0:
                    if not k:
                        token = '10000000186490f2'
                    elif k == 1:
                        token = '1000000089ff6e7a'
                    else:
                        token = '10000000tokenasd'
            else:
                token = '10000000token' + 'i' + 'j' + str(random.randint(1, 9))
            
            location_x = locations[i][j][0]
            location_y = locations[i][j][1]
            
            if locations[i][j][2]:
                location_y += k * 20
            else:
                location_x += k * 20
            while True:
                    n = random.randint(0, 4)
                    if not n in type_list:
                        type_list.append(n)
                        break
            fields_3 = {
                        'token': token,
                        'trash_type' : trash_type[n],
                        'amount': random.random(),
                        'location_x': location_x,
                        'location_y': location_y,
                        'group' : str(j),
                        'created_at': created_at,
                        'updated_at': updated_at,
                        'floor': i+1,
                    }
            if fields_3['amount'] >= 0.7:
                fields_3['status'] = 'WAR'
            elif fields_3['amount'] >= 0.4:
                fields_3['status'] = 'CAU'
            else:
                fields_3['status'] = 'SAF'
            data_3 = {
                    'pk': cnt_bin,
                    'model': 'campus.trashbin',
                    'fields': fields_3
                    }
            trashbins.append(data_3)
            cnt_bin += 1


for j in range(1, len(building)):
    fields2 = {
        'name': building[j],
        'description': f'이 곳은 {building[j]} 건물 입니다.',
        'created_at': created_at,
        'updated_at': updated_at
    }
    data2 = {
        'pk': cnt_building,
        'model': 'campus.building',
        'fields': fields2
    }
    buildings.append(data2)
    orders = 0
    floor_number = random.randint(2, len(floor))
    for k in range(1, floor_number):
        fields3 = {
            'name' : floor[k-1],
            'map_path' : floor_url,
            'width' : 650,
            'height': 450,
            'trashbin_size': 20,
            'order': orders,    # 층 순서
            'building' : cnt_building,
            'created_at': created_at,
            'updated_at': updated_at

        }
        data3 = {
            'pk': cnt_floor,
            'model': 'campus.floor',
            'fields': fields3
        }
        floors.append(data3)
        orders += 1        
        for gr in range(3):
            location_x = random.randrange(30, 600)
            location_y = random.randrange(30, 400)
            ver_hor = random.random()
            type_list = []
            for asd in range(3):
                if ver_hor >= 0.5:
                    location_x += 20
                else:
                    location_y += 20
                while True:
                    n = random.randint(0, 4)
                    if not n in type_list:
                        type_list.append(n)
                        break
                fields4 = {
                    'token': str(j)+floor[k-1]+str(cnt_trashbin),
                    'trash_type' : trash_type[n],
                    'amount': 0,
                    'location_x': location_x,
                    'location_y': location_y,
                    'created_at': created_at,
                    'updated_at': updated_at,
                    'group': str(gr),
                    'floor' : cnt_floor
                }
                if fields4['amount'] >= 0.7:
                    fields4['status'] = 'WAR'
                elif fields4['amount'] >= 0.4:
                    fields4['status'] = 'CAU'
                else:
                    fields4['status'] = 'SAF' 
                data4 = {
                    'pk' : cnt_trashbin,
                    'model': 'campus.trashbin',
                    'fields': fields4
                }
                trashbins.append(data4)
                cnt_trashbin += 1
        cnt_floor += 1
    cnt_building += 1


last_name = ["김", "이", "박", "최", "정", "홍", "장", "왕", "윤", "안"]
first_name = ["민준", "서준", "도윤", "예준", "시우", "하준", "주원", "지호", "준우", "지후", "민성", "서연",
"서윤", "지우", "서현", "하은", "하윤", "민서", "지유", "윤서", "지민", "채원", "수아", "지아", "지윤", "은서", "다은"
]

for i in range(1, 101):
    student = {}
    student["pk"] = i
    student["student_num"] = "0" * (10-len(str(i))) + str(i)
    student["name"] = last_name[random.randrange(len(last_name))] +  first_name[random.randrange(len(first_name))]
    student["belong"] = building[random.randrange(len(building))]
    student["rfid_num"] = "rf" + "0" * 3 + "0" * (5-len(str(i))) + str(i)
    fields = {
        'student_num': student['student_num'],
        'name': student['name'],
        'belong': student['belong'],
        'rfid_num': student['rfid_num'],
        'created_at': created_at,
        'updated_at': updated_at,
    }
    data = {
        'pk': student['pk'],
        'model': 'campus.student',
        'fields': fields
    }
    students.append(data)


with open('buildings.json', 'w', encoding='utf-8') as json_file:
    json.dump(buildings, json_file, ensure_ascii=False, default=str)

with open('floors.json', 'w', encoding='utf-8') as json_file:
    json.dump(floors, json_file, ensure_ascii=False, default=str)

with open('trashbins.json', 'w', encoding='utf-8') as json_file:
    json.dump(trashbins, json_file, ensure_ascii=False, default=str)

with open('students.json', 'w', encoding='utf-8') as json_file:
    json.dump(students, json_file, ensure_ascii=False, default=str)