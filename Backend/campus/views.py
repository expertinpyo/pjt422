from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers.campus import CampusListSerializer, CampusSerializer, CampusManagerSerializer, CampusStudentSerializer
from .serializers.building import BuildingFloorSerializer, BuildingTrashBinSerializer
from .models import Campus, Building
# Create your views here.

# 전체 캠퍼스 조회
@api_view(['GET'])
def campuses(request):
    campuses = Campus.objects.all()
    serializer = CampusListSerializer(campuses, many=True)
    return Response(serializer.data)

# 특정 캠퍼스의 전체 건물 조회
@api_view(['GET'])
def campus(request, campus_pk):
    campus = get_object_or_404(Campus, pk=campus_pk)
    serializer = CampusSerializer(campus)
    return Response(serializer.data)

# 특정 캠퍼스의 전체 관리자 조회
@api_view(['GET' 'POST'])
def campus_manager(request, campus_pk):
    campus = get_object_or_404(Campus, pk=campus_pk)
    def get_managers(campus_pk):
        serializer = CampusManagerSerializer(campus)
        return Response(serializer.data)

        
    if request.method == 'GET':
        return get_managers(campus_pk)
    elif request.method == 'POST':
        pass    # 아직 post는 구현 안됨. 굳이 여기서 코드를 작성할 필요는 없어보임. accounts의 view에 함수 만들고 그 것 호출 여부도 괜찮아보임

# 특정 캠퍼스의 전체 학생 조회
@api_view(['GET'])
def campus_student(request, campus_pk):
    campus = get_object_or_404(Campus, pk=campus_pk)
    serializer = CampusStudentSerializer(campus)
    return Response(serializer.data)

# 특정 건물의 전체 층 조회
@api_view(['GET'])
def building(request, building_pk):
    building = get_object_or_404(Building, pk=building_pk)
    serializer = BuildingFloorSerializer(building)
    return Response(serializer.data)