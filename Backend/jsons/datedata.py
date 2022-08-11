import json

dates = []
year = [{
    'pk': 1,
    'model': 'stats.year',
    'fields' : {
        'num' : '2022'
    }
}]
months = []
cnt_m = 1
for month in range(5, 9):
    data_m = {
        'pk' : cnt_m,
        'model': 'stats.month',
        'fields' : {
            'num' : '0'+str(month),
            'year' : 1,
        }
    }
    months.append(data_m)
    if month == 6:
        nn = 31
    else:
        nn = 32
    for j in range(1, nn):
        day = str(j)    
        fields = {
            'num':day,
            'month': cnt_m
        }
        data = {
            'pk' : int(day),
            'model': 'stats.date',
            'fields':fields
        }
        dates.append(data)
    cnt_m += 1


with open('year.json', 'w', encoding='utf-8') as json_file:
    json.dump(year, json_file, ensure_ascii=False, default=str)


with open('month.json', 'w', encoding='utf-8') as json_file:
    json.dump(months, json_file, ensure_ascii=False, default=str)


with open('date.json', 'w', encoding='utf-8') as json_file:
    json.dump(dates, json_file, ensure_ascii=False, default=str)

