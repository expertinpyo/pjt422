# class형 view를 만들기 위해 View import
from rest_framework.views import APIView

from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from django.shortcuts import get_list_or_404, get_object_or_404


from .models import *

from .serializers.date import *
from .serializers.week import *
from .serializers.month import *
from .serializers.year import *

import pandas as pd
import json

import matplotlib.pyplot as plt
import numpy as np

from django.db.models import Sum

from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create your views here.

# 빌딩 일간 데이터 조회
class BuildingDailyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, building_pk, dates):
        year, month, date = dates[:4], dates[4:6], dates[6:]
        building = get_object_or_404(BuildingDate, building_pk=building_pk, year=year, month=month, date=date)
        serializer = BuildingDateSerializer(building)
        return Response(serializer.data)

# 빌딩 주간 데이터 조회
class BuildingWeeklyView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, building_pk, dates):
        year, month, date = dates[:4], dates[4:6], dates[6:] 
        str_date = datetime.strptime(year + '-' + month + '-' + date, '%Y-%m-%d')
        model_ids = []
        for i in range(7):
            datetime_result = str(str_date - relativedelta(days=i))
            qry = BuildingDate.objects.get(building_pk=building_pk, year=datetime_result[:4], month=datetime_result[5:7], date=datetime_result[8:10])
            model_ids.append(qry.pk)
        df = pd.DataFrame.from_records(BuildingDate.objects.filter(pk__in=model_ids).values())
        new_df = df.groupby(['building_pk']).sum().reset_index()
        building = new_df.to_dict(orient='records')[0]
        serializer = BuildingWeekSerializer(building) 
        return Response(serializer.data)

# 빌딩 월간 데이터 조회
class BuildingMonthlyView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, building_pk, months):
        year, month = months[:4], months[4:6]
        df = pd.DataFrame.from_records(BuildingDate.objects.filter(building_pk=building_pk, year=year, month=month).values())
        new_df = df.groupby(['year', 'month', 'building_pk']).sum().reset_index()
        building = new_df.to_dict(orient='records')[0]
        serializer = BuildingMonthSerializer(building) 
        return Response(serializer.data)

# 빌딩 연간 데이터 조회
class BuildingYearView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, building_pk, year):
        df = pd.DataFrame.from_records(BuildingDate.objects.filter(building_pk=building_pk, year=year).values())
        new_df = df.groupby(['year', 'building_pk']).sum().reset_index()
        building = new_df.to_dict(orient='records')[0]
        serializer = BuildingYearSerializer(building) 
        return Response(serializer.data)

# 층 일간 데이터 조회
class FloorDailyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, floor_pk, dates):
        year, month, date = dates[:4], dates[4:6], dates[6:]
        floor = get_object_or_404(FloorDate, floor_pk=floor_pk, year=year, month=month, date=date)
        serializer = FloorDateSerializer(floor)
        return Response(serializer.data)

# 층 주간 데이터 조회
class FloorWeeklyView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, floor_pk, dates):
        year, month, date = dates[:4], dates[4:6], dates[6:] 
        str_date = datetime.strptime(year + '-' + month + '-' + date, '%Y-%m-%d')
        model_ids = []
        for i in range(7):
            datetime_result = str(str_date - relativedelta(days=i))
            qry = FloorDate.objects.get(floor_pk=floor_pk, year=datetime_result[:4], month=datetime_result[5:7], date=datetime_result[8:10])
            model_ids.append(qry.pk)
        df = pd.DataFrame.from_records(FloorDate.objects.filter(pk__in=model_ids).values())
        new_df = df.groupby(['floor_pk']).sum().reset_index()
        floor = new_df.to_dict(orient='records')[0]
        serializer = FloorWeekSerializer(floor) 
        return Response(serializer.data)

# 층 월간 데이터 조회 
class FloorMonthlyView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, floor_pk, months):
        year, month = months[:4], months[4:6]
        df = pd.DataFrame.from_records(BuildingDate.objects.filter(floor_pk=floor_pk, year=year, month=month).values())
        new_df = df.groupby(['year', 'month', 'building_pk', 'floor_pk']).sum().reset_index()
        floor = new_df.to_dict(orient='records')[0]
        serializer = FloorMonthSerializer(floor) 
        return Response(serializer.data)

# 층 연간 데이터 조회 
class FloorYearView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, floor_pk, year):
        df = pd.DataFrame.from_records(BuildingDate.objects.filter(floor_pk=floor_pk, year=year).values())
        new_df = df.groupby(['year', 'building_pk', 'floor_pk']).sum().reset_index()
        floor = new_df.to_dict(orient='records')[0]
        serializer = FloorYearSerializer(floor) 
        return Response(serializer.data)


# 쓰레기통 일간 데이터 조회
class TrashbinDailyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, token, dates):
        year, month, date = dates[:4], dates[4:6], dates[6:]
        trashbin = get_object_or_404(TrashbinDate, token=token, year=year, month=month, date=date)
        serializer = TrashbinDateSerializer(trashbin)
        return Response(serializer.data)

# 쓰레기통 주간 데이터 조회
class TrashbinWeeklyView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, token, dates):
        year, month, date = dates[:4], dates[4:6], dates[6:] 
        str_date = datetime.strptime(year + '-' + month + '-' + date, '%Y-%m-%d')
        model_ids = []
        for i in range(7):
            datetime_result = str(str_date - relativedelta(days=i))
            qry = TrashbinDate.objects.get(token=token, year=datetime_result[:4], month=datetime_result[5:7], date=datetime_result[8:10])
            model_ids.append(qry.pk)
        df = pd.DataFrame.from_records(TrashbinDate.objects.filter(pk__in=model_ids).values())
        new_df = df.groupby(['token']).sum().reset_index()
        trashbin = new_df.to_dict(orient='records')[0]
        serializer = TrashbinWeekSerializer(trashbin) 
        return Response(serializer.data)

# 쓰레기통 월간 데이터 조회
class TrashbinMonthlyView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, token, months):
        year, month = months[:4], months[4:6]
        df = pd.DataFrame.from_records(TrashbinDate.objects.filter(token=token, year=year, month=month).values())
        new_df = df.groupby(['year', 'month', 'building_pk', 'floor_pk', 'token']).sum().reset_index()
        print(new_df)
        trashbin = new_df.to_dict(orient='records')[0]
        serializer = TrashbinMonthSerializer(trashbin) 
        return Response(serializer.data)

# 쓰레기통 연간 데이터 조회
class TrashbinYearView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, token, year):
        df = pd.DataFrame.from_records(TrashbinDate.objects.filter(token=token, year=year).values())
        new_df = df.groupby(['year', 'building_pk', 'floor_pk', 'token']).sum().reset_index()
        trashbin = new_df.to_dict(orient='records')[0]
        serializer = TrashbinYearSerializer(trashbin) 
        return Response(serializer.data)
