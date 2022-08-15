from rest_framework import serializers
# models import
from ..models import *

class TrashbinWeekSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrashbinDate
        exclude = ('date','id', 'year', 'month','building_pk', 'floor_pk')
        

class FloorWeekSerializer(serializers.ModelSerializer):

    class Meta:
        model = FloorDate
        exclude = ('date','id', 'year', 'month', 'building_pk')


class BuildingWeekSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuildingDate
        exclude = ('date','id', 'year', 'month')