# system import
from rest_framework import serializers
# models import
from ..models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class CampusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = ('pk', 'name', 'description')

class CampusSerializer(serializers.ModelSerializer):
    
    class BuildingListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Building
            fields = ('pk', 'name', 'description')
    
    building = BuildingListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Campus
        fields = ('pk', 'name', 'description', 'building')

class CampusManagerSerializer(serializers.ModelSerializer):
    
    class ManagerListSerializers(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'name', 'belong', 'phone', 'rfid_num', 'position')
    
    manager = ManagerListSerializers(many=True, read_only=True)
    
    class Meta:
        model = Campus
        fields = ('pk', 'name', 'description', 'manager')

class CampusStudentSerializer(serializers.ModelSerializer):

    class StudentListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Student
            fields = ('pk', 'student_num', 'name', 'belong', 'rfid_num')
        
    student = StudentListSerializer(many=True, read_only=True)

    class Meta:
        model = Campus
        fields = ('pk', 'name', 'description', 'student')


