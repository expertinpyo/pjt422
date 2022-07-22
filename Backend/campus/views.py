from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers.campus import CampusListSerializer, CampusSerializer, CampusManagerSerializer, CampusStudentSerializer
from .models import Campus, Student, Building, Floor
from .serializers.floor import FloorSerializer
from .serializers.student import StudentListSerializer
# Create your views here.

@api_view(['GET'])
def campuses(request):
    campuses = Campus.objects.all()
    serializer = CampusListSerializer(campuses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def campus(request, campus_pk):
    campus = get_object_or_404(Campus, pk=campus_pk)
    serializer = CampusSerializer(campus)
    return Response(serializer.data)

@api_view(['GET'])
def campus_manager(request, campus_pk):
    campus = get_object_or_404(Campus, pk=campus_pk)
    serializer = CampusManagerSerializer(campus)
    return Response(serializer.data)

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
        data = {
            'delete': f'{student_pk}번 학생이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


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
def floor_UD(request, campus_pk, building_pk, floor_pk):
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


@api_view(['GET'])
def floor_trashbins(request):
    pass