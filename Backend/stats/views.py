# class형 view를 만들기 위해 View import
from re import L
from rest_framework.views import APIView

from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


from .models import *

from .serializers.date import *

import pandas as pd
import json

# Create your views here.
class TestView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, dates):
        
        # if BuildingDate.objects.
        year  = dates[:4]
        month = dates[4:6]
        day = dates[6:]
        month_pk = Month.objects.filter(num__exact=month, year__num=year)[0]
        year_pk = Year.objects.filter(num__exact=year)[0]

        
        if BuildingDate.objects.filter(num__exact=day, building_month__exact=month_pk, building_month__year__exact=year_pk):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if FloorDate.objects.filter(num__exact=day, floor_month__exact=month_pk, floor_month__year__exact=year_pk):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if TrashbinDate.objects.filter(num__exact=day, trashbin_month__exact=month_pk, trashbin_month__year__exact=year_pk):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        with open (f'log_dummy/{dates}', encoding='UTF8') as f:
            records = [line.rstrip().split(' ') for line in f]
        columns = ['date', 'time', 'building', 'building_pk', 'floor', 'floor_pk', 'token', 'trash_type', 'rfid', 'amount']
        df = pd.DataFrame(records, columns=columns)
        df["hour"] = df["time"].str[:2]
        right_data = df.drop_duplicates(subset=['token'])
        left_data = df.groupby(['token', 'hour']).date.count().unstack(fill_value=0)        
        left_data.reset_index(inplace=True)
        labels = ['token', 'hour_00','hour_01','hour_02','hour_03','hour_04','hour_05','hour_06','hour_07','hour_08','hour_09','hour_10','hour_11','hour_12','hour_13','hour_14','hour_15','hour_16','hour_17','hour_18','hour_19','hour_20','hour_21','hour_22','hour_23']
        left_data.columns = labels
        left_data['total'] = left_data.sum(numeric_only=True, axis=1)
        # 같은 날 같은시간 이므로 month와 year는 통일시켜서 집어넣는 것도 하나의 방법임.
        # 다만 num을 활용해야 하므로 다시 생각해보자
        


        new_df = left_data.merge(right_data, on='token')
              
        new_df.drop(columns=['date', 'time', 'rfid', 'amount', 'hour', 'floor', 'building'], inplace=True)
        new_df = new_df.astype({'floor_pk':'int', 'building_pk':'int'})
        
        trashbin = new_df.copy()
        trashbin['year'] = year
        trashbin['month'] = month
        trashbin['num'] = day
        trashbin_dict = trashbin.to_dict(orient='records')

        building = new_df.groupby(['building_pk']).sum().drop(columns='floor_pk').reset_index()
        building['year'] = year
        building['month'] = month
        building['num'] = day
        building_dict = building.to_dict(orient='records')

        floor = new_df.groupby(['building_pk','floor_pk']).sum().reset_index()
        floor['year'] = year
        floor['month'] = month
        floor['num'] = day
        floor_dict = floor.to_dict(orient='records')
            
        
        
        for dic in building_dict:
            dic['building_month'] = month_pk.pk
            serializer = BuildingDateSerializer(data=dic)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

        for dic in floor_dict:
            dic['floor_month'] = month_pk.pk
            serializer = FloorDateSerializer(data=dic)
            if serializer.is_valid(raise_exception=True):
                serializer.save()


        for dic in trashbin_dict:            
            dic['trashbin_month'] = month_pk.pk
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

# 날짜별 전체 조회
class DailyView(APIView):
    
    def get(self, request, dates):
        pass



class MonthlyView(APIView):
    pass


class YearView(APIView):
    pass
