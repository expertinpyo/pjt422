# system import
from rest_framework import serializers
# models import
from ..models import *
from django.contrib.auth import get_user_model

class BuildingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ('pk', 'name', 'description', 'campus')

class BuildingFloorSerializer(serializers.ModelSerializer):
    
    class FloorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Floor
            fields = ('pk', 'name', 'map_path', 'width', 'height')
    
    floor = FloorSerializer(many=True, read_only=True)
    floors_count = serializers.IntegerField(source='floor.count', read_only=True)
    
    class Meta:
        model = Building
        fields = ('pk', 'name', 'description', 'floor', 'floors_count',)


class BuildingTrashBinSerializer(serializers.ModelSerializer):
    
    class TrashBinSerializer(serializers.ModelSerializer):
        class Meta:
            model = Trashbin
            exclude = ('created_at', 'updated_at', 'discarded_users')
    
    trashbin = TrashBinSerializer(many=True, read_only=True)

    class Meta:
        model = Building
        fields = ('pk', 'name', 'description', 'trashbin')
        