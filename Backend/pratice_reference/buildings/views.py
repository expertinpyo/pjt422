from django.shortcuts import render
from .models import *
from .serializers.building import BuildingSerializer
from .serializers.floor import FloorSerializer
from .serializers.trashbin import TrashbinSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

# 전체 빌딩 조회
@api_view(['GET',])
def buildings(request):
    all_buildings = Building.objects.all()
    serializer = BuildingSerializer(all_buildings, many=True)
    return Response(serializer.data)

# 특정 빌딩의 모든 층 조회
@api_view(['GET'])
def floors(request, b_num):
    all_floors = Building.objects.filter(name__icontains=b_num)
    serializer = FloorSerializer(all_floors, many=True)
    return Response(serializer.data)

# 특정 층의 모든 쓰레기통 조회
@api_view(['GET'])
def bins(request, b_num, f_num):
    pass