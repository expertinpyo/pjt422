from rest_framework import serializers
from ..models import Student

class StudentListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'
        

class StudentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('pk', 'student_num', 'name', 'belong', 'rfid_num',)