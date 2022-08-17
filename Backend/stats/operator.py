from .models import *
from .serializers.date import * 

import pandas as pd
from datetime import date, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
import logging


ytd = date.today() - timedelta(days=1)
dates = ytd.strftime('%Y%m%d')
# dates = '20220501'
logger = logging.getLogger('trash_event')

def start():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(daily_data, 'interval', seconds=5)
    scheduler.add_job(daily_data, 'cron', hour=1)
    scheduler.start()


def daily_data():
    global dates
    year, month, date = dates[:4], dates[4:6], dates[6:]
    
    if BuildingDate.objects.filter(date=date, month=month, year=year):
        return
    
    if FloorDate.objects.filter(date=date, month=month, year=year):
        return

    if TrashbinDate.objects.filter(date=date, month=month, year=year):
        return
    # {building_id} {floor_id} {group_id} {token} {trash_type}'
    with open (f'log_dummy/{dates}.log', encoding='UTF8') as f:
        records = [line.rstrip().split(' ') for line in f]
    columns = ['date', 'time', 'building_pk', 'floor_pk', 'token', 'trash_type']
    df = pd.DataFrame(records, columns=columns)
    
    df['year'] = df.date.str[:4]
    df['month'] = df.date.str[4:6]
    df.date = df.date.str[6:]

    df['hour'] = df['time'].str[:2]
    right_data = df.drop_duplicates(subset=['token'])
    left_data = df.groupby(['token', 'hour']).date.count().unstack(fill_value=0)        
    left_data.reset_index(inplace=True)
    labels = ['token', 'hour_00','hour_01','hour_02','hour_03','hour_04','hour_05','hour_06','hour_07','hour_08','hour_09','hour_10','hour_11','hour_12','hour_13','hour_14','hour_15','hour_16','hour_17','hour_18','hour_19','hour_20','hour_21','hour_22','hour_23']
    left_data.columns = labels
    left_data['total'] = left_data.sum(numeric_only=True, axis=1)


    new_df = left_data.merge(right_data, on='token')
    new_df.drop(columns=['time', 'hour'], inplace=True)
    new_df = new_df.astype({'floor_pk':'int', 'building_pk':'int'})
    types = new_df.drop(columns = ['hour_00','hour_01','hour_02','hour_03','hour_04','hour_05','hour_06','hour_07','hour_08','hour_09','hour_10','hour_11','hour_12','hour_13','hour_14','hour_15','hour_16','hour_17','hour_18','hour_19','hour_20','hour_21','hour_22','hour_23'])


    trashbin= new_df.groupby(['year','month','date','building_pk', 'floor_pk', 'token', 'trash_type']).sum().reset_index()
    trashbin_dict = trashbin.to_dict(orient='records')

    floor_type = types.groupby(['year','month','date','building_pk', 'floor_pk','trash_type']).total.sum().unstack(fill_value=0)
    floor_type.reset_index(inplace=True)
    floor_type.drop(columns = ['year', 'month', 'date', 'building_pk'], inplace=True)
    floor = new_df.groupby(['year','month','date','building_pk', 'floor_pk']).sum().reset_index()
    floor = floor.merge(floor_type, on='floor_pk')
    floor_dict = floor.to_dict(orient='records')

    building_type = types.groupby(['year','month','date','building_pk','trash_type']).total.sum().unstack(fill_value=0)
    building_type.reset_index(inplace=True)
    building_type.drop(columns = ['year', 'month', 'date'], inplace=True)
    building = new_df.groupby(['year','month','date','building_pk']).sum().reset_index()
    building = building.merge(building_type, on='building_pk')        
    building_dict = building.to_dict(orient='records')


    for dic in building_dict:
        serializer = BuildingDateSerializer(data=dic)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    logger.info(f'{dates} : building daily data save completely')

    for dic in floor_dict:
        serializer = FloorDateSerializer(data=dic)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    logger.info(f'{dates} : floor daily data save completely')


    for dic in trashbin_dict:            
        serializer = TrashbinDateSerializer(data=dic)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    logger.info(f'{dates} : trashbin daily data save completely')
    
    

    # if dates[4:6] == '06':
    #     if int(dates[6:]) == 30:
    #         dates = '20220701'
    #     else: 
    #         dates = str(int(dates) + 1)
    # elif dates[4:6] == '08':
    #     if int(dates[6:]) > 14:
    #         dates = '20220501'
    #     else:
    #         dates = str(int(dates) + 1)
    # else:
    #     if int(dates[6:]) == 31:
    #         dates = dates[:5] + str(int(dates[4:6])+1) + '01'
    #     else:
    #         dates = str(int(dates) + 1)
