from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers.managers import ManagerAllUpdateSerializer, ManagerListSerializer, ManagerCreateSerializer, ManagerUpdateSerializer, ManagerMasterUpdateSerializer, ManagerNormalUpdateSerializer
from django.contrib.auth import get_user_model
import re

# Create your views here.
User = get_user_model()

class ManagerAllView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        managers = User.objects.order_by('pk')
        serializer = ManagerListSerializer(managers, many=True)
        return Response(serializer.data)

    def post(self, request):
        # password = request.data.get('password')
        # if len(password) < 8:
        #     return Response({'password': '비밀번호는 8자 이상 입력하세요'})
        # elif not re.findall('[0-9]+', password) or not re.findall('[a-zA-z]',password):
        #     return Response({'password': '숫자와 영어의 조합으로 비밀번호를 만들어주세요'})
        serializer = ManagerCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class ManagerView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, user_pk):
        IsOk = False
        user = get_object_or_404(User, pk=user_pk)
        if request.user.position == 'MR':
            serializer = ManagerMasterUpdateSerializer(instance=user, data=request.data, partial=True)
            IsOk = True
        else:
            if request.user == user:
                serializer = ManagerNormalUpdateSerializer(instance=user, data=request.data)
                IsOK = True
        if IsOk:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_pk):
        if request.user.is_superuser:
            user = get_object_or_404(User, pk=user_pk)
            user.delete()
            users = User.objects.all().filter(campus=request.user.campus)
            serializer = ManagerListSerializer(users, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
