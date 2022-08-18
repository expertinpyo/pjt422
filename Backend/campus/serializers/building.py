# system import
from rest_framework import serializers
# models import
from ..models import *
from django.contrib.auth import get_user_model

class BuildingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ('pk', 'name', 'description',)

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ('pk', 'name', 'description')


class BuildingFloorSerializer(serializers.ModelSerializer):
    
    class FloorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Floor
            fields = ('pk', 'name', 'map_path', 'width', 'height', 'trashbin_size', 'order')
    
    floor = FloorSerializer(many=True, read_only=True)

    class Meta:
        model = Building
        fields = ('pk', 'name', 'description', 'floor',)

class BuildingTrashBinSerializer(serializers.ModelSerializer):
    
    class TrashBinSerializer(serializers.ModelSerializer):
        class Meta:
            model = Trashbin
            exclude = ('created_at', 'updated_at', 'discard_users')
    
    trashbin = TrashBinSerializer(many=True, read_only=True)

    class Meta:
        model = Building
        fields = ('pk', 'name', 'description', 'trashbin')
        