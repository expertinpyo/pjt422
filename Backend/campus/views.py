from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers.campus import CampusListSerializer, CampusSerializer, CampusManagerSerializer, CampusStudentSerializer
from .models import Campus

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