from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers.managers import ManagerListSerializer 
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()
@api_view(['GET'])
def managers(request):
    managers = User.objects.order_by('pk')
    serializer = ManagerListSerializer(managers, many=True)
    return Response(serializer.data)

def campus_managers(request, campus_id):
    managers = User.objects.filter()