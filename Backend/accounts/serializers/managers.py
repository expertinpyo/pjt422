# system import
from rest_framework import serializers
# models import
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

class ManagerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('pk', 'username', 'name', 'belong', 'phone', 'rfid_num', 'campus', 'position')
        fields = '__all__'

class ManagerCreateSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'name', 'belong', 'rfid_num', 'phone', 'position', 'password')
    
    def create(self, validated_data):
        user = super(ManagerCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        print(user.password)
        return user

# 회원 정보 수정
class ManagerUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'name', 'phone',)


class ManagerAllUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'belong', 'phone', 'rfid_num', 'position', 'username', 'password', 'is_superuser', )  # password..?