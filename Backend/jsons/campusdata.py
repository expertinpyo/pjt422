import random
import json
import datetime


campus = []
floors = []
buildings = []
trashbins = []
students = []

floor_url = "https://www.cnuh.co.kr/images/pcrc/sub01/sub01_0603_img01.jpg"
belong = ["공학", "간호학", "자연과학", "경영학", "경제학", "어문학", "체육학"]
camp_name = ["서울대학교", "연세대학교"]
building = ["공학관", "어학관", "경영대학관", "체육관", "중앙도서관"]
floor = ["B1","B2", "1", "2", "3", "4"]
trash_type = ['GER', 'PET', 'CAN', 'GLA', 'PPR']
# 캠퍼스
created_at = datetime.datetime.now()
updated_at = datetime.datetime.now()
cnt_campus = cnt_building = cnt_floor = cnt_trashbin = 1
for i in range(1, 3):
    fields1 = {
        'name': camp_name[i-1],
        'description' : f"이 곳은 {camp_name[i-1]}입니다.",
        'created_at': created_at,
        'updated_at': updated_at
    }   
    data = {
        'pk' : cnt_campus,
        'model': 'campus.campus',
        'fields': fields1
    }
    campus.append(data)
    
    #빌딩
    for j in range(1, len(building)+1):
        fields2 = {
            'name': building[j-1],
            'description': f'이 곳은 {building[j-1]} 건물 입니다.',
            'campus': cnt_campus,
            'created_at': created_at,
            'updated_at': updated_at
        }
        data2 = {
            'pk': cnt_building,
            'model': 'campus.building',
            'fields': fields2
        }
        buildings.append(data2)

        for k in range(1, len(floor)+1):
            fields3 = {
                'name' : floor[k-1],
                'map_path' : floor_url,
                'width' : 650,
                'height': 450,
                'trashbin_size': 20,
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

            for a in range(1, len(trash_type)+1):
                fields4 = {
                    'token': str(i)+str(j)+floor[k-1]+trash_type[a-1]+str(cnt_trashbin),
                    'amount': random.random(),
                    'location_x': random.randrange(0, 650),
                    'location_y': random.randrange(0, 450),
                    'floor': cnt_floor,
                    'created_at': created_at,
                    'updated_at': updated_at
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
    cnt_campus += 1

last_name = ["김", "이", "박", "최", "정", "홍", "장", "왕", "윤", "안"]
first_name = ["민준", "서준", "도윤", "예준", "시우", "하준", "주원", "지호", "준우", "지후", "민성", "서연",
"서윤", "지우", "서현", "하은", "하윤", "민서", "지유", "윤서", "지민", "채원", "수아", "지아", "지윤", "은서", "다은"
]
building = ["공학", "간호학", "자연과학", "경영학", "경제학", "어문학", "체육학"]
for i in range(1, 5*10**3+1):
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
        'campus': random.randrange(1, 3)
    }
    data = {
        'pk': student['pk'],
        'model': 'campus.student',
        'fields': fields
    }
    students.append(data)

with open('campus.json', 'w', encoding='utf-8') as json_file:
    json.dump(campus, json_file, ensure_ascii=False, default=str)

with open('buildings.json', 'w', encoding='utf-8') as json_file:
    json.dump(buildings, json_file, ensure_ascii=False, default=str)

with open('floors.json', 'w', encoding='utf-8') as json_file:
    json.dump(floors, json_file, ensure_ascii=False, default=str)

with open('trashbins.json', 'w', encoding='utf-8') as json_file:
    json.dump(trashbins, json_file, ensure_ascii=False, default=str)

with open('students.json', 'w', encoding='utf-8') as json_file:
    json.dump(students, json_file, ensure_ascii=False, default=str)