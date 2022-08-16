from lzma import CHECK_CRC32, CHECK_CRC64, CHECK_SHA256
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

# rest framework 
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

# models
from .models import CleanRecord, Student, Building, Floor, Trashbin, Group

# serializers
from .serializers.building import BuildingFloorSerializer, BuildingSerializer
from .serializers.floor import FloorSerializer, FloorTrashbinSerializer
from .serializers.student import StudentCreateSerializer, StudentListSerializer
from .serializers.trashbin import CleanRecordSerializer, TrashbinCreateSerializer,TrashbinSerializer, TrashbinNotificationSerializer
from .serializers.group import GroupSerializer

# import socketserver
# import pickle
# import struct



# 빌딩 / 층  / 쓰레가통 열람 권한 : 모든 이용자
# 관리자 / 학생 정보 열람 권한 : authenticated 유저 (JR + SR + MR 관리자))

# 빌딩 / 층 / 관리자 / 학생 추가, 삭제, 수정 권한 : admin (MR 관리자)
# 쓰레기통 추가, 삭제, 수정 권한 : authenticated (SR + MR 관리자)


# 모든 빌딩 관리
class BuildingAllView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        buildings = Building.objects.all()
        serializer = BuildingSerializer(buildings, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_superuser:
            print(request.data)
            serializer = BuildingSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        raise exceptions.AuthenticationFailed('You do not have permission to perform this action.')


# 특정 빌딩 관리
class BuildingView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, building_pk):
        building = get_object_or_404(Building, pk=building_pk)
        serializer = BuildingFloorSerializer(building)
        return Response(serializer.data)

    def post(self, request, building_pk):
        building = get_object_or_404(Building, pk=building_pk)
        serializer = FloorSerializer(data=request.data)
        if request.user.is_superuser:
            if serializer.is_valid(raise_exception=True):
                serializer.save(building=building)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        raise exceptions.AuthenticationFailed('You do not have permission to perform this action.')

    def put(self, request, building_pk):
        building = get_object_or_404(Building, pk=building_pk)
        serializer = BuildingSerializer(instance=building, data=request.data)
        if request.user.is_superuser:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        raise exceptions.AuthenticationFailed('You do not have permission to perform this action.')

    def delete(self, request, building_pk):
        if request.user.is_superuser:
            building = get_object_or_404(Building, pk=building_pk)
            building.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise exceptions.AuthenticationFailed('You do not have permission to perform this action.')


# 특정 층 관리
class FloorView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, floor_pk):
        floor = get_object_or_404(Floor, pk=floor_pk)
        serializer = FloorTrashbinSerializer(floor)
        return Response(serializer.data)
    
    def post(self, request, floor_pk):
        floor = get_object_or_404(Floor, pk=floor_pk)
        serializer = GroupSerializer(data=request.data)
        if request.user.is_superuser:
            if serializer.is_valid(raise_exception=True):
                serializer.save(floor=floor)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        raise exceptions.AuthenticationFailed('You do not have permission to perform this action.')

    def put(self, request, floor_pk):
        floor = get_object_or_404(Floor, pk=floor_pk)
        serializer = FloorTrashbinSerializer(instance=floor, data=request.data)
        if request.user.is_superuser:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        raise exceptions.AuthenticationFailed('You do not have permission to perform this action.')

    def delete(self, request, floor_pk):
        if request.user.is_superuser:
            floor = get_object_or_404(floor, pk=floor_pk)
            floor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise exceptions.AuthenticationFailed('You do not have permission to perform this action.')


# 특정 쓰레기통 그룹 관리
class GroupView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, group_pk):
        group = get_object_or_404(Group, pk=group_pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)
    
    def post(self, request, group_pk):
        group = get_object_or_404(Group, pk=group_pk)
        serializer = TrashbinCreateSerializer(data=request.data)
        if request.user.is_superuser:
            if serializer.is_valid(raise_exception=True):
                serializer.save(group=group)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        raise exceptions.AuthenticationFailed('You do not have permission to perform this action.')

    def put(self, request, group_pk):
        group = get_object_or_404(Group, pk=group_pk)
        serializer = GroupSerializer(instance=group, data=request.data)
        if request.user.is_superuser:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        raise exceptions.AuthenticationFailed('You do not have permission to perform this action.')

    def delete(self, request, group_pk):
        if request.user.is_superuser:
            group = get_object_or_404(group, pk=group_pk)
            group.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise exceptions.AuthenticationFailed('You do not have permission to perform this action.')


# 특정 쓰레기통 관리
class TrashbinView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, trashbin_pk):
        trashbin = get_object_or_404(Trashbin, pk=trashbin_pk)
        print(trashbin.trash_type)
        serializer = TrashbinSerializer(trashbin)
        return Response(serializer.data)
    
    def put(self, request, trashbin_pk):
        trashbin = get_object_or_404(Trashbin, pk=trashbin_pk)
        serializer = TrashbinSerializer(instance=trashbin, data=request.data)
        if request.user.position != "JR":
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        raise exceptions.AuthenticationFailed('You do not have permission to perform this action.')

    def delete(self, request, trashbin_pk):
        if request.user.position != "JR":
            trashbin = get_object_or_404(trashbin, pk=trashbin_pk)
            trashbin.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise exceptions.AuthenticationFailed('You do not have permission to perform this action.')


# 전체 학생 조회 및 추가
class StudentAllView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentListSerializer(students, many=True)
        return Response(serializer.data)

    def post(Self, request):
        serializer = StudentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


# 학생 정보 수정 및 삭제 
class StudentView(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, student_pk):
        student = get_object_or_404(Student, pk=student_pk)
        serializer = StudentListSerializer(instance=student, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, student_pk):
        student = get_object_or_404(Student, pk=student_pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 알림 요청
class NotificationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        trashbins = Trashbin.objects.filter(amount__gte=0.4)
        serializer = TrashbinNotificationSerializer(trashbins, many=True)
        return Response(serializer.data)


class RecordView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        records = get_list_or_404(CleanRecord)
        serializer = CleanRecordSerializer(records, many=True)
        return Response(serializer.data)

