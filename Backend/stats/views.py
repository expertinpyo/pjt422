# class형 view를 만들기 위해 View import
from rest_framework.views import APIView

from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


from .models import *

from .serializers.date import DailyDataSerializer
from .serializers.trashbin import TrashbinDataSerializer

import pandas as pd

# Create your views here.
class TestView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, dates):
        pass


    def post(self, request, dates):
        if not Date.objects.filter(date__iexact=dates):
            date = {'date':dates}
            serializer_date = DailyDataSerializer(data=date)
            if serializer_date.is_valid(raise_exception=True):
                serializer_date.save()
                with open (f'log_dummy/{dates}', encoding='UTF8') as f:
                    records = [line.rstrip().split(' ') for line in f]
                columns = ['date', 'time', 'building', 'floor', 'token', 'trash_type', 'rfid', 'amount']
                df = pd.DataFrame(records, columns=columns)
                df["hour"] = df["time"].str[:2]
                right_data = df.drop_duplicates(subset=['token'])
                left_data = df.groupby(['token', 'hour']).date.count().unstack(fill_value=0)        
                left_data.reset_index(inplace=True)
                left_data.index.name = 'pk'
                labels = ['token', 'hour_00','hour_01','hour_02','hour_03','hour_04','hour_05','hour_06','hour_07','hour_08','hour_09','hour_10','hour_11','hour_12','hour_13','hour_14','hour_15','hour_16','hour_17','hour_18','hour_19','hour_20','hour_21','hour_22','hour_23']
                left_data.columns = labels
                left_data['total'] = left_data.sum(numeric_only=True, axis=1)
                new_df = left_data.merge(right_data, on='token')
                new_df.drop(columns=['time', 'rfid', 'amount', 'hour'], inplace=True)
                new_df.token.astype('str')
                new_df.date.astype('str')

                jss = new_df.to_json(orient='records', force_ascii=False)
                
                for js in jss:
                    serializer = TrashbinDataSerializer(data=js, many=True)
                    if serializer.is_valid(raise_exception=True):
                        print("여기까지도 옴 2")
                        serializer.save()
                return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

                
                
        

class DailyView(APIView):
    pass


class MonthlyView(APIView):
    pass


class YearView(APIView):
    pass
