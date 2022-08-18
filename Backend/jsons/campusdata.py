import random
import json
import datetime


floors = []
buildings = []
trashbins = []
students = []
groups = []

floor_url = "https://www.cnuh.co.kr/images/pcrc/sub01/sub01_0603_img01.jpg"
belong = ["공학", "간호학", "자연과학", "경영학", "경제학", "어문학", "체육학"]
building = ["공학관", "어학관", "경영대학관", "체육관", "중앙도서관"]
floor = ["B2","B1", "1", "2", "3", "4", "5", "6", "7"]
trash_type = ['GER', 'PET', 'CAN', 'GLA', 'PPR']

created_at = datetime.datetime.now()
updated_at = datetime.datetime.now()
cnt_building = cnt_floor = cnt_group = cnt_trashbin = 1

group_str = 'A'
group_num = '1'
group_name = group_str + group_num

for j in range(1, len(building)+1):
    fields2 = {
        'name': building[j-1],
        'description': f'이 곳은 {building[j-1]} 건물 입니다.',
        'created_at': created_at,
        'updated_at': updated_at
    }
    data2 = {
        'pk': cnt_building,
        'model': 'campus.building',
        'fields': fields2
    }
    buildings.append(data2)
    orders = -1
    floor_number = random.randint(3, len(floor))
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
        num_group = random.randint(3, 8)
        for i in range(1, num_group+1):
            fields5 = {
                'name': floor[k-1]+group_name,
                'floor': cnt_floor,
                'created_at': created_at,
                'updated_at': updated_at
            }
            location_x = random.randrange(30, 600)
            location_y = random.randrange(30, 400)
            ver_hor = random.random()
            group_num = str(int(group_num) + 1)
            group_name = group_str + group_num
            data5 = {
                'pk': cnt_group,
                'model': 'campus.group',
                'fields': fields5
            }
            groups.append(data5)
            for asd in range(3):
                if ver_hor >= 0.5:
                    location_x += (asd * 20)
                else:
                    location_y += (asd * 20)
                fields4 = {
                    'token': str(j)+floor[k-1]+str(cnt_trashbin),
                    'trash_type' : trash_type[random.randint(0, 4)],
                    'amount': random.random(),
                    'location_x': location_x,
                    'location_y': location_y,
                    'created_at': created_at,
                    'updated_at': updated_at,
                    'group': cnt_group
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
            cnt_group += 1
        group_str = chr(ord(group_str) + 1)
        group_num = '1'
        group_name = group_str + group_num
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

with open('groups.json', 'w', encoding='utf-8') as json_file:
    json.dump(groups, json_file, ensure_ascii=False, default=str)

with open('trashbins.json', 'w', encoding='utf-8') as json_file:
    json.dump(trashbins, json_file, ensure_ascii=False, default=str)

with open('students.json', 'w', encoding='utf-8') as json_file:
    json.dump(students, json_file, ensure_ascii=False, default=str)