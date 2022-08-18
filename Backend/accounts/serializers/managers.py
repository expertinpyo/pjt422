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

# 회원정보 생성 => password hashing
class ManagerCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('pk', 'username', 'password', 'name', 'belong', 'phone', 'rfid_num', 'position')
        extra_kwargs= {
            'password' : {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        if instance.position == "MR":
            instance.is_superuser = True
            instance.is_staff = True
        instance.save()
        return instance
    
    
        

# 회원 정보 수정
class ManagerUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'name', 'phone',)


class ManagerAllUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'belong', 'phone', 'rfid_num', 'position', 'password', 'is_superuser', )  # password..?


class ManagerMasterUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'password', 'name', 'belong', 'phone', 'rfid_num', 'position')
        extra_kwargs= {
            'password' : {'write_only': True}
        }
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        
        if password is not None:
            instance.set_password(password)
        if instance.position == "MR":
            instance.is_superuser = True
            instance.is_staff = True
        else:
            instance.is_superuser = instance.is_staff = False

        instance.save()
        return instance

class ManagerNormalUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields =  ('password', 'phone', )
        extra_kwargs= {
            'password' : {'write_only': True}
        }
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        
        if password is not None:
            instance.set_password(password)
            
        instance.save()
        return instance