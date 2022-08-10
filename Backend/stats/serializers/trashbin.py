from rest_framework import serializers
# models import
from ..models import *

class TrashbinDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrashbinStats
        fields = '__all__'
        