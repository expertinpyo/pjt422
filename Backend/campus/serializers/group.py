from rest_framework import serializers
from ..models import *


class GroupSerializer(serializers.ModelSerializer):

    class TrashbinSerializer(serializers.ModelSerializer):

        class Meta:
            model = Trashbin
            exclude = ('created_at', 'updated_at')
    
    trashbin = TrashbinSerializer(many=True, read_only=True)
    
    class Meta:
        model = Group
        fields = '__all__'

class GroupCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name',)
    
