from lzma import CHECK_CRC32, CHECK_CRC64, CHECK_SHA256
from django.http import QueryDict
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

# rest framework 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status, exceptions
from rest_framework.response import Response


# models
from .models import Campus, Student, Building, Floor, Trashbin

# serializers
from .serializers.campus import CampusListSerializer, CampusSerializer, CampusManagerSerializer, CampusStudentSerializer
from .serializers.building import BuildingFloorSerializer, BuildingSerializer
from .serializers.floor import FloorSerializer, FloorTrashbinSerializer
from .serializers.student import StudentListSerializer
from .serializers.trashbin import TrashbinCreateSerializer, TrashbinListSerializer, TrashbinSerializer, TrashbinNotificationSerializer, TrashbinTypeSerializer


import requests
import logging

logger = logging.getLogger('trash_event')


# 캠퍼스 / 빌딩 / 층  / 쓰레가통 열람 권한 : 모든 이용자
# 관리자 / 학생 정보 열람 권한 : authenticated 유저 (JR + SR + MR 관리자))

# 캠퍼스 / 빌딩 / 층 / 관리자 / 학생 추가, 삭제, 수정 권한 : admin (MR 관리자)
# 쓰레기통 추가, 삭제, 수정 권한 : authenticated (SR + MR 관리자)

@api_view(['GET', 'POST'])
def test(request, rfid, trashbin_pk):
    trashbin = get_object_or_404(Trashbin, pk=trashbin_pk)
    floor = trashbin.floor
    building = floor.building
    campus = building.campus

    logger.error(f'{campus.name} {building.name} {floor.name} {trashbin.token} {trashbin.trash_type} {rfid} {trashbin.amount}')
    

    return Response(status=status.HTTP_200_OK)


# 전체 캠퍼스 조회 및 추가
@api_view(['GET', 'POST'])
def campuses(request):

    def get_campus():
        campuses = Campus.objects.all()
        serializer = CampusListSerializer(campuses, many=True)
        return Response(serializer.data)
    
    
    def create_campus():
        serializer = CampusListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method == 'GET':
        return get_campus()
    elif request.method == 'POST':
        if request.user.is_superuser:
            return create_campus()
        raise exceptions.AuthenticationFailed('No Authorization to perform this task')


# 특정 캠퍼스의 전체 건물 조회 및 추가 / 해당 캠퍼스 수정 및 삭제
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def campus(request, campus_pk):
    campus = get_object_or_404(Campus, pk=campus_pk)
    
    def get_buildings():
        serializer = CampusSerializer(campus)
        return Response(serializer.data)

    def create_building():
        serializer = BuildingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(campus=campus)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update_campus():
        serializer = CampusListSerializer(instance=campus, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete_campus():
        campus.delete()
        campuses = Campus.objects.all()
        serializer = CampusListSerializer(campuses, many=True)
        return Response(serializer.data)

    if request.method == 'GET':
        return get_buildings()
    else:
        if request.user.is_superuser:
            if request.method == 'POST':
                return create_building()
            elif request.method == 'PUT':
                return update_campus()
            elif request.method == 'DELETE':
                return delete_campus()
        raise exceptions.AuthenticationFailed('No Authorization to perform this task')


# 특정 건물의 전체 층 조회 및 층 추가 / 해당 건물 수정 및 삭제
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def building(request, building_pk):
    building = get_object_or_404(Building, pk=building_pk)
    campus = get_object_or_404(Campus, pk=building.campus.pk)
            
    def get_floors():
        serializer = BuildingFloorSerializer(building)
        return Response(serializer.data)

    def create_floor():
        serializer = FloorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(building=building)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update_building():
        serializer = BuildingSerializer(instance=building, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data) 

    def delete_building():
        building.delete()
        serializer = CampusSerializer(campus)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return get_floors()
    else:
        if request.user.is_superuser:
            if request.method == 'POST':
                return create_floor()
            elif request.method == 'PUT':
                return update_building()
            elif request.method == 'DELETE':
                return delete_building()
        raise exceptions.AuthenticationFailed('No Authorization to perform this task')
    
    
# 해당 계단 정보 + 모든 쓰레기통 조회, 쓰레기통 추가 / 해당 층 수정 및 삭제
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def floor(request, floor_pk):
    floor = get_object_or_404(Floor, pk=floor_pk)
    building = get_object_or_404(Building, pk=floor.building.pk)

    def get_trashbins():
        serializer = FloorTrashbinSerializer(floor)
        return Response(serializer.data)

    def create_trashbin():
        serializer = TrashbinCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(floor=floor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update_floor():
        serializer = FloorSerializer(instance=floor, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    def delete_floor():
        floor.delete()
        serializer = BuildingFloorSerializer(building)
        return Response(serializer.data)

    if request.method == 'GET':
        return get_trashbins()
    else:
        if request.user.is_superuser:
            if request.method == 'POST':
                return create_trashbin()
            elif request.method == 'PUT':
                return update_floor()
            elif request.method == 'DELETE':
                return delete_floor()
        raise exceptions.AuthenticationFailed('No Authorization to perform this task')


# 해당 쓰레기통 조회 / 수정 / 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def trashbin(request, trashbin_pk):  
    trashbin = get_object_or_404(Trashbin, pk=trashbin_pk)
    floor = get_object_or_404(Floor, pk=trashbin.floor.pk)
    
    # 쓰레기통 상세 조회
    def get_trashbin():
        serializer = TrashbinSerializer(trashbin)
        return Response(serializer.data)
    
    def update_trashbin():
        serializer = TrashbinSerializer(instance=trashbin, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete_trashbin():
        trashbin.delete()
        serializer = FloorTrashbinSerializer(floor)
        return Response(serializer.data)

    if request.method == 'GET':
        return get_trashbin()
    else:
        if request.user.is_superuser:
            if request.method == 'PUT':
                return update_trashbin()
            elif request.method == 'DELETE':
                return delete_trashbin()
        raise exceptions.AuthenticationFailed('No Authorization to perform this task')


@api_view(['GET',])
@permission_classes([IsAuthenticated])
def trashbin_check(request):
    trashbins = Trashbin.objects.exclude(status__iexact='SAF').filter(floor__building__campus__pk=request.user.pk)
    serializer = TrashbinListSerializer(trashbins, many=True)
    return Response(serializer.data)


# 특정 캠퍼스의 전체 관리자 조회 및 추가
@api_view(['GET',])
@permission_classes([IsAdminUser])
def managers(request, campus_pk):
    campus = get_object_or_404(Campus, pk=campus_pk)

    def get_managers():
        serializer = CampusManagerSerializer(campus)
        return Response(serializer.data)

    if request.method == 'GET' and request.user.campus.pk == campus_pk:
        return get_managers()
    raise exceptions.AuthenticationFailed('No Authorization to perform this task')


# 특정 캠퍼스의 전체 학생 조회 및 추가
@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def students(request, campus_pk):
    campus = get_object_or_404(Campus, pk=campus_pk)
    
    def get_students():
        serializer = CampusStudentSerializer(campus)
        return Response(serializer.data)

    def create_student():
        serializer = CampusStudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(campus=campus)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.user.campus.pk == campus_pk:
        if request.method == 'GET':
            return get_students()
        elif request.method == 'POST':
            return create_student()
    raise exceptions.AuthenticationFailed('No Authorization to perform this task')


# 학생 정보 수정 및 삭제
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def student_detail(request, campus_pk, student_pk):
    student = get_object_or_404(Student, pk=student_pk)
    campus = get_object_or_404(Campus, pk=campus_pk)
    
    def update_student():
        serializer = StudentListSerializer(instance=student, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete_student():  
        student.delete()
        serializer = CampusStudentSerializer(campus)
        return Response(serializer.data)
    
    if request.user.campus.pk == campus_pk:
        if request.method == 'PUT':
            return update_student()
        elif request.method == 'DELETE':
            return delete_student()
    raise exceptions.AuthenticationFailed('No Authorization to perform this task')
        

# @api_view(['GET'])
# def trashbin_status(request):
#     trashbins = Trashbin.objects.filter(Q(status='CAU') | Q(status='WAR'))
#     serializer = TrashbinSerializer(trashbins, many=True)
#     return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def notification(request):
    campus = request.user.campus
    trashbins = Trashbin.objects.filter(floor__building__campus__pk=campus.pk, amount__gte=0.4)
    serializer = TrashbinNotificationSerializer(trashbins, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# def check_all(request, rfid):
#     User = get_user_model()
#     try:
#         user = Student.objects.get(rfid_num = rfid)
#         data = {
#             'who': '등록된 사용자입니다.'
#         }
#     except Student.DoesNotExist: 
#         user = User.objects.filter(rfid_num=rfid)
#         if len(user) >= 1:
#             data = {
#                 'who': '관리자입니다.'
#             }
#         else:
#             data = {
#                 'who': '미등록된 사용자입니다.'
#             }
#     finally:
#         return Response(data)


# @api_view(['GET'])
# def trashbin_type(request, token):
#     trashbin = get_object_or_404(Trashbin, token=token)
#     serializer = TrashbinTypeSerializer(trashbin)
#     return Response(serializer.data)






    






# # 층 삭제, 수정 (수정의 경우 지도가 바뀔 수도 있으므로)
# @api_view(['GET', 'DELETE', 'PUT'])
# def floor(request, floor_pk):
#     floor = get_object_or_404(Floor, pk=floor_pk)
    
#     def get_trashbins():    
#         serializer = FloorSerializer(floor)
#         return Response(serializer.data)

#     def update_floor():
#         serializer = FloorSerializer(instance=floor, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
    
#     def delete_floor():
#         floor.delete()
        
#         return Response(data, status=status.HTTP_204_NO_CONTENT)

#     if request.method == 'GET':
#         return get_trashbins()
#     elif request.method == 'PUT':
#         return update_floor()
#     elif request.method == 'GET':
#         return delete_floor()


# @api_view(['GET', 'POST'])
# def floor_trashbins(request, floor_pk):  
#     floor = get_object_or_404(Floor, pk=floor_pk)
#     if request.method == 'GET':
#         serializer = FloorTrashbinSerializer(floor)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = TrashbinCreateSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(floor=floor)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', "DELETE"])
# def trashbin_detail(request, floor_pk, trashbin_pk):  
#     trashbin = get_object_or_404(Trashbin, pk=trashbin_pk)
#     floor = get_object_or_404(Floor, pk=floor_pk)
#     # 쓰레기통 상세 조회
#     if request.method == 'GET':
#         serializer = TrashbinSerializer(trashbin)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = TrashbinSerializer(instance=trashbin, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#     elif request.method == 'DELETE':
#         trashbin.delete()
#         # 삭제 후 전체 쓰레기통 조회
#         trashbins = floor.trashbin.all()
#         serializer = TrashbinListSerializer(trashbins, many=True)
#         return Response(serializer.data)

