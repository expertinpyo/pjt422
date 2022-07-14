from rest_framework import serializers
from ..models import Trashbin

class TrashbinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trashbin
        fields = '__all__'
        