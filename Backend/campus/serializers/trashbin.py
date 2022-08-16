from rest_framework import serializers
from ..models import Building, Floor, Student, Trashbin, Group, CleanRecord
from django.contrib.auth import get_user_model

# 해당 층에 쓰레기통 추가
class TrashbinCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trashbin
        exclude = ('group', 'discard_users', )


# 쓰레기통 상세 조회
class TrashbinSerializer(serializers.ModelSerializer):
    # discard_users를 조회하기 위한 관리자 정보
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            excludes = ('created_at', 'updated_at',)

    discard_users = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Trashbin
        fields = '__all__'


class TrashbinNotificationSerializer(serializers.ModelSerializer):
    
    class GroupSerializer(serializers.ModelSerializer):

        class FloorSerializer(serializers.ModelSerializer):
            
            class BuildingSerializer(serializers.ModelSerializer):

                class Meta:
                    model = Building
                    fields = ('pk', 'name',)
                
            building = BuildingSerializer(read_only=True)

            class Meta:
                model = Floor
                fields = ('pk', 'name', 'building')
        
        floor = FloorSerializer(read_only=True)

        class Meta:
            model = Group
            fields = ('pk', 'name', 'floor')
    
    group = GroupSerializer(read_only=True)

    class Meta:
        model = Trashbin
        fields = '__all__'



# 비움 이력 조회
class CleanRecordSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username', 'rfid_num', 'name', 'phone', 'position', )
    
    user = UserSerializer(read_only=True)
    
    class TrashbinSerializer(serializers.ModelSerializer):
        
        class GroupSerializer(serializers.ModelSerializer):

            class FloorSerializer(serializers.ModelSerializer):
                
                class BuildingSerializer(serializers.ModelSerializer):

                    class Meta:
                        model = Building
                        fields = ('pk', 'name',)
                    
                building = BuildingSerializer(read_only=True)

                class Meta:
                    model = Floor
                    fields = ('pk', 'name', 'building',)
            
            floor = FloorSerializer(read_only=True)

            class Meta:
                model = Group
                fields = ('pk', 'name', 'floor',)
        
        group = GroupSerializer(read_only=True)

        class Meta:
            model = Trashbin
            fields = ('trash_type', 'token', 'group', )
    
    trashbin = TrashbinSerializer(read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = CleanRecord
        fields = '__all__'



# class CleanRecordSerializer(serializers.ModelSerializer):
    
#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = get_user_model()
#             fields = ('pk', 'username', 'rfid_num', 'name', 'phone', 'position', )

#     user = UserSerializer(read_only=True)  

#     trashbin = TrashbinNotificationSerializer(read_only=True)

#     class Meta:
#         model = CleanRecord
#         fields = '__all__'