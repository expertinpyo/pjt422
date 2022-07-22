from rest_framework import serializers
from ..models import Trashbin

# 층 별 쓰레기통 전체 조회
class TrashbinListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trashbin
        fields = '__all__'