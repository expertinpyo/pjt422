# class형 view를 만들기 위해 View import
from re import L
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.views import APIView

from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


from .models import *

from .serializers.date import *

import pandas as pd
import json

import matplotlib.pyplot as plt
import numpy as np

from django.db.models import Sum

# Create your views here.
class TestView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, dates):
        
        year, month, date = dates[:4], dates[4:6], dates[6:]
        if BuildingDate.objects.filter(year__exact=year, month__exact=month, date__exact=date):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if FloorDate.objects.filter(year__exact=year, month__exact=month, date__exact=date):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if TrashbinDate.objects.filter(year__exact=year, month__exact=month, date__exact=date):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
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
        # 같은 날 같은시간 이므로 month와 year는 통일시켜서 집어넣는 것도 하나의 방법임.
        # 다만 num을 활용해야 하므로 다시 생각해보자


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
        return Response(status=status.HTTP_200_OK)



        # return Response(status=status.HTTP_400_BAD_REQUEST)


# get 요청
# 전체 쓰레기통 대상 => 시간대별 조회 통계
# 한 빌딩의 쓰레기통 시간대별 조회 통계
# 한 층의 쓰레기통 시간대별 조회 통계
# 위에것 not 시간대별 but 쓰레기통 종류별 통계

# # 빌딩 일일 데이터 조회
# class GetGraph(APIView):
    
#     def graph(self):
        

class BuildingDailyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, building_pk, dates):
        year, month, date = dates[:4], dates[4:6], dates[6:]
        building = get_object_or_404(BuildingDate, building_pk=building_pk, year=year, month=month, date=date)
        serializer = BuildingDateSerializer(building)
        return Response(serializer.data)


class FloorDailyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, floor_pk, dates):
        year, month, date = dates[:4], dates[4:6], dates[6:]
        floor = get_object_or_404(FloorDate, floor_pk=floor_pk, year=year, month=month, date=date)
        serializer = FloorDateSerializer(floor)
        return Response(serializer.data)
        

class TrashbinDailyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, token, dates):
        year, month, date = dates[:4], dates[4:6], dates[6:]
        trashbin = get_object_or_404(TrashbinDate, token=token, year=year, month=month, date=date)
        serializer = TrashbinDateSerializer(trashbin)
        return Response(serializer.data)


class BuildingMonthlyView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, building_pk, months):
        year, month = months[:4], months[4:]
        print(year, month)
        building = get_list_or_404(BuildingDate, building_pk=building_pk, building_month__num__exact=month, building_month__year__num__exact=year)
        serializer = BuildingDateSerializer(building, many=True)
        return Response(serializer.data)

class BuildingYearView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, building_pk, year):
        building = get_list_or_404(BuildingDate, building_pk=building_pk, building_month__year__num__exact=year)
        serializer = BuildingDateSerializer(building, many=True)
        return Response(serializer.data)

class PandasTestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, floor_pk, months):
        year, month = months[:4], months[4:6]
        df = pd.DataFrame.from_records(FloorDate.objects.filter(floor_pk=floor_pk, year=year, month=month).values())
        new_df = df.groupby(['year', 'month']).sum().reset_index()
        new_df.building_pk = df.loc[0, 'building_pk'] 
        new_df.floor_pk = floor_pk 
        print(new_df)
        return Response(status=status.HTTP_200_OK)
        # return Response(serializer.data)