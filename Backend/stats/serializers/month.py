from rest_framework import serializers
# models import
from ..models import *

class TrashbinMonthSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrashbinDate
        exclude = ('date','id')
        

class FloorMonthSerializer(serializers.ModelSerializer):

    class Meta:
        model = FloorDate
        exclude = ('date','id')


class BuildingMonthSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuildingDate
        exclude = ('date','id')