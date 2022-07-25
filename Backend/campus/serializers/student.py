from rest_framework import serializers
from ..models import Student

# 학생 전체 조회
class StudentListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        exclude = ('created_at', 'updated_at', )
        read_only = ('campus',)
