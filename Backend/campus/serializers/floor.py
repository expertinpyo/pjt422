from rest_framework import serializers
from ..models import Floor, Trashbin


class FloorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Floor
        fields = ('name', 'map_path', 'width', 'height', 'trashbin_size', 'order')
        


class FloorTrashbinSerializer(serializers.ModelSerializer):
    # 층 내 쓰레기통 그룹 조회
    class TrashbinListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Trashbin
            exclude = ('floor',)


    trashbin = TrashbinListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Floor
        fields = ('pk', 'name', 'map_path', 'width', 'height', 'trashbin_size','trashbin', 'building', 'order')
        
