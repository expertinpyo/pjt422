from rest_framework import serializers
from ..models import Student

class StudentListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ('campus',)
        

class StudentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('student_num', 'name', 'belong', 'rfid_num',)