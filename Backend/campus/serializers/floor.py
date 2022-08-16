from rest_framework import serializers
from ..models import Floor, Trashbin, Group


class FloorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Floor
        fields = ('name', 'map_path', 'width', 'height', 'trashbin_size', 'order')
        


class FloorGroupSerializer(serializers.ModelSerializer):
    # 층 내 쓰레기통 그룹 조회
    class GroupListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Group
            exclude = ('floor',)


    group = GroupListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Floor
        fields = ('pk', 'name', 'map_path', 'width', 'height', 'trashbin_size','group', 'building', 'order')
        
