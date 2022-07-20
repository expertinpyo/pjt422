from rest_framework import serializers
from ..models import *

class FloorSerializer(serializers.ModelSerializer):
    
    
    class TrashbinSerializer(serializers.ModelSerializer):
        class Meta:
            model = Trashbin
            fields = '__all__'
    trashbins = TrashbinSerializer(many=True, read_only=True)

    class Meta:
        model = Floor
        fields = '__all__'