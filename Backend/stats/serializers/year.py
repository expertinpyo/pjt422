from rest_framework import serializers
# models import
from ..models import *

class TrashbinYearSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrashbinDate
        exclude = ('date', 'month','id')
        

class GroupYearSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupDate
        exclude = ('date', 'month','id')


class FloorYearSerializer(serializers.ModelSerializer):

    class Meta:
        model = FloorDate
        exclude = ('date', 'month','id')


class BuildingYearSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuildingDate
        exclude = ('date', 'month', 'id')