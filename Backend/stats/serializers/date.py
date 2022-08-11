from rest_framework import serializers
# models import
from ..models import *

class TrashbinDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrashbinDate
        fields = '__all__'
        

class FloorDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = FloorDate
        fields = '__all__'


class BuildingDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuildingDate
        fields = '__all__'