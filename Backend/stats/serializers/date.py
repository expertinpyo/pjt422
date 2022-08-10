from rest_framework import serializers
# models import
from ..models import *

class DailyDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Date
        fields = '__all__'
        