from django.shortcuts import get_object_or_404, get_list_or_404
from django.urls import is_valid_path
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers.campus import CampusListSerializer, CampusSerializer, CampusManagerSerializer, CampusStudentSerializer

from .models import Campus, Student, Building, Floor, Trashbin
from .serializers.floor import FloorSerializer, FloorTrashbinSerializer
from .serializers.student import StudentListSerializer
from .serializers.building import BuildingFloorSerializer, BuildingTrashBinSerializer


from .serializers.trashbin import TrashbinCreateSerializer, TrashbinListSerializer, TrashbinSerializer

from .models import Campus, Student, Building, Floor
from .serializers.floor import FloorSerializer
from .serializers.student import StudentListSerializer
from .serializers.building import BuildingFloorSerializer, BuildingListSerializer, BuildingTrashBinSerializer


from .models import Campus, Building

from accounts.views import campus_managers

# Create your views here.

# 캠퍼스 / 빌딩 / 층  / 쓰레가통 열람 권한 : 모든 이용자
# 관리자 / 학생 정보 열람 권한 : authenticated 유저 (JR + SR + MR 관리자))

# 캠퍼스 / 빌딩 / 층 / 관리자 / 학생 추가, 삭제, 수정 권한 : admin (MR 관리자)
# 쓰레기통 추가, 삭제, 수정 권한 : authenticated (SR + MR 관리자)

# 전체 캠퍼스 조회 및 추가
@api_view(['GET', 'POST'])
def campuses(request):
    
    def get_campus():
        campuses = Campus.objects.all()
        serializer = CampusListSerializer(campuses, many=True)
        return Response(serializer.data)
    
    def create_campus():
        serializer = CampusListSerializer(data=request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method == 'GET':
        return get_campus()
    elif request.method == 'POST':
        return create_campus()


# 특정 캠퍼스의 전체 건물 조회 및 추가 / 해당 캠퍼스 수정 및 삭제
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def campus(request, campus_pk):
    campus = get_object_or_404(Campus, pk=campus_pk)
    
    def get_buildings():
        serializer = CampusSerializer(campus)
        return Response(serializer.data)

    def create_building():
        serializer = BuildingListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update_campus():
        serializer = CampusListSerializer(instance=campus, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete_campus():
        campus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return get_buildings()
    elif request.method == 'POST':
        return create_building()
    elif request.method == 'PUT':
        return update_campus()
    elif request.method == 'DELETE':
        return delete_campus()


# 특정 건물의 전체 층 조회 및 층 추가 / 해당 건물 수정 및 삭제
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def building(request, building_pk):
    building = get_object_or_404(Building, pk=building_pk)
        
    def get_floors():
        serializer = BuildingFloorSerializer(building)
        return Response(serializer.data)

    def create_floor():
        pass

    def update_building():
        serializer = BuildingListSerializer(instance=building, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete_building():
        building.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return get_floors()
    elif request.method == 'POST':
        return create_floor()
    elif request.method == 'PUT':
        return update_building()
    elif request.method == 'DELETE':
        return delete_building()
    


# 특정 캠퍼스의 전체 관리자 조회 및 추가
@api_view(['GET' 'POST'])
def campus_manager(request, campus_pk):
    campus = get_object_or_404(Campus, pk=campus_pk)
    
    def get_managers(campus_pk):
        serializer = CampusManagerSerializer(campus)
        return Response(serializer.data)

    if request.method == 'GET':
        return get_managers(campus_pk)
    elif request.method == 'POST':
        return campus_managers(request, campus_pk)


# 특정 캠퍼스의 전체 학생 조회
@api_view(['GET'])
def campus_student(request, campus_pk):
    campus = get_object_or_404(Campus, pk=campus_pk)
    serializer = CampusStudentSerializer(campus)
    return Response(serializer.data)



# 학생 추가
@api_view(['POST'])
def students(request, campus_pk):
    campus = get_object_or_404(Campus, pk=campus_pk)
    serializer = StudentListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(campus=campus)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 학생 정보 수정 및 삭제
@api_view(['PUT', 'DELETE'])
def student_detail(request, campus_pk, student_pk):
    student = get_object_or_404(Student, pk=student_pk)
    campus = get_object_or_404(Campus, pk=campus_pk)
    if request.method == 'PUT':
        serializer = StudentListSerializer(instance=student, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        student.delete()
        students = campus.student.all()
        serializer = StudentListSerializer(students, many=True)
        return Response(serializer.data)



# 층 추가
@api_view(['POST'])
def floor_create(request, campus_pk, building_pk):
    serializer = FloorSerializer(data=request.data)
    building = get_object_or_404(Building, pk=building_pk)
    if serializer.is_valid(raise_exception=True):
        serializer.save(building=building)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# 층 삭제, 수정 (수정의 경우 지도가 바뀔 수도 있으므로)
@api_view(['GET', 'DELETE', 'PUT'])
def floor_detail(request, campus_pk, building_pk, floor_pk):
    floor = get_object_or_404(Floor, pk=floor_pk)
    if request.method == 'GET':
        serializer = FloorSerializer(floor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FloorSerializer(instance=floor, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        floor.delete()
        data = {
            'delete': f'{building_pk}번 건물의 {floor_pk}번 층이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)




# 특정 건물의 전체 층 조회
@api_view(['GET'])
def building(request, building_pk):
    building = get_object_or_404(Building, pk=building_pk)
    serializer = BuildingFloorSerializer(building)
    return Response(serializer.data)




@api_view(['GET', 'POST'])
def floor_trashbins(request, floor_pk):  
    floor = get_object_or_404(Floor, pk=floor_pk)
    if request.method == 'GET':
        serializer = FloorTrashbinSerializer(floor)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TrashbinCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(floor=floor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', "DELETE"])
def trashbin_detail(request, floor_pk, trashbin_pk):  
    trashbin = get_object_or_404(Trashbin, pk=trashbin_pk)
    floor = get_object_or_404(Floor, pk=floor_pk)
    # 쓰레기통 상세 조회
    if request.method == 'GET':
        serializer = TrashbinSerializer(trashbin)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TrashbinSerializer(instance=trashbin, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        trashbin.delete()
        # 삭제 후 전체 쓰레기통 조회
        trashbins = floor.trashbin.all()
        serializer = TrashbinListSerializer(trashbins, many=True)
        return Response(serializer.data)

