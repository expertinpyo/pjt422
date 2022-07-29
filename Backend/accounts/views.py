from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import status
from rest_framework.response import Response
from .serializers.managers import ManagerAllUpdateSerializer, ManagerListSerializer, ManagerCreateSerializer, ManagerUpdateSerializer, ManagerMasterUpdateSerializer, ManagerNormalUpdateSerializer
from django.contrib.auth import get_user_model
from campus.models import Campus

# Create your views here.
User = get_user_model()
@api_view(['GET'])
@permission_classes([IsAdminUser])
def managers(request):
    managers = User.objects.order_by('pk')
    serializer = ManagerListSerializer(managers, many=True)
    return Response(serializer.data)

# 일단 생성은 된다
# 추가해야할 점
# 1. campus : 요청 보낸 슈퍼 유저의 캠퍼스 id로 생성되게 할 것 => 확인
# 2. position : 값이 MR라면 admin유저로 격상시켜주기(생성시) => 확인
# 가능하다면, 비밀번호를 따로 입력받지 않고, 아이디 값을 초기 비밀번호로 생성해주기
# 진행해야 하는 것 => 다른 폼을 거치지 않고 db로 바로 유저를 생성해주기 => 현재 생성만 가능, password를 암호화하는 과정 필요한 것으로 확인 => 확인


@api_view(['POST'])
@permission_classes([IsAdminUser])
def campus_managers(request, campus_id):
    def manager_create():
        campus = get_object_or_404(Campus, pk=campus_id)
        serializer = ManagerCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(campus=campus)
            return Response(serializer.data)
    
    if request.method == 'POST':
        print("accounts로 들어옴")
        return manager_create()


# 기본 로직
# 1. 해당 캠퍼스의 마스터 매니저가 해당 캠퍼스의 매니저 수정 삭제 가능
# 2. 일반 / 선임 매니저는 본인 계정의 비밀번호만 변경 가능
# @api_view(['PUT', 'DELETE'])
# def manager_detail(request, manager_id):
    
#     def update_manager():
#         # serializer = ManagerSerializer(instance=)
#         pass
#     def delete_manager():
#         pass

#     if request.method == "PUT":
#         return update_manager()
#     elif request.method == 'DELETE':
#         return delete_manager()


# 관리자 본인이 자신의 회원 정보를 수정
@api_view(['PUT'])
def manager_detail(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    if request.user == user:
        serializer = ManagerUpdateSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# master manager가 관리자들의 회원 정보를 수정
@api_view(['PUT'])
def edit_managers(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    print(user.position)
    if user.position == 'MR':
        serializer = ManagerAllUpdateSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)       
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def master_edit(request, user_pk):    
    user = get_object_or_404(User, pk=user_pk)

    def update_as_master():
        serializer = ManagerMasterUpdateSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def update_as_normal():
        if request.user == user:
            serializer = ManagerNormalUpdateSerializer(instance=user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete_manager():
        if request.user.campus == user.campus:
            user.delete()
            users = User.objects.all().filter(campus=request.user.campus)
            serializer = ManagerListSerializer(users, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        if request.user.is_superuser:
            return update_as_master()
        else:
            return update_as_normal()
    elif request.method == 'DELETE' and request.user.is_superuser:
        return delete_manager()