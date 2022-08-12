from .models import *
from .serializers.date import * 

import pandas as pd
from datetime import date, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from django_apscheduler.jobstores import register_events, DjangoJobStore
import logging


# ytd = date.today() - timedelta(days=1)
# dates = ytd.strftime('%Y%m%d')

dates = '20220505'
def start():
    global dates
    
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
    register_events(scheduler)
    
    @scheduler.scheduled_job('cron', minute='*/1', name='daily_data')
    def daily_data():
        year, month, date = dates[:4], dates[4:6], dates[6:]
        
        if BuildingDate.objects.filter(date=date, month=month, year=year):
            return
        
        if FloorDate.objects.filter(date=date, month=month, year=year):
            return
        
        if TrashbinDate.objects.filter(date=date, month=month, year=year):
            return

        with open (f'log_dummy/{dates}', encoding='UTF8') as f:
            records = [line.rstrip().split(' ') for line in f]
        columns = ['date', 'time', 'building', 'building_pk', 'floor', 'floor_pk', 'token', 'trash_type', 'rfid', 'amount']
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
        new_df.drop(columns=['time', 'rfid', 'amount', 'hour', 'floor', 'building'], inplace=True)
        new_df = new_df.astype({'floor_pk':'int', 'building_pk':'int'})
        
        trashbin = new_df.copy()
        trashbin_dict = trashbin.to_dict(orient='records')

        building = new_df.groupby(['year', 'month', 'date', 'building_pk']).sum().drop(columns='floor_pk').reset_index()
        building_dict = building.to_dict(orient='records')

        floor = new_df.groupby(['year', 'month', 'date', 'building_pk','floor_pk']).sum().reset_index()
        floor_dict = floor.to_dict(orient='records')

        
        for dic in building_dict:
            serializer = BuildingDateSerializer(data=dic)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

        for dic in floor_dict:
            serializer = FloorDateSerializer(data=dic)
            if serializer.is_valid(raise_exception=True):
                serializer.save()


        for dic in trashbin_dict:            
            serializer = TrashbinDateSerializer(data=dic)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
    
    dates = str(int(dates) + 1)
    scheduler.start()


def weekly_data():
    pass

def monthly_data():
    pass

def yearly_data():
    pass