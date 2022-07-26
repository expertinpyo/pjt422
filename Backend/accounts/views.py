from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from .serializers.managers import ManagerListSerializer, ManagerSerializer, ManagerUpdateSerializer
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()
@api_view(['GET'])
def managers(request):
    managers = User.objects.order_by('pk')
    serializer = ManagerListSerializer(managers, many=True)
    return Response(serializer.data)

# 일단 생성은 된다
# 추가해야할 점
# 1. campus : 요청 보낸 슈퍼 유저의 캠퍼스 id로 생성되게 할 것
# 2. position : 값이 MR라면 admin유저로 격상시켜주기(생성시)
@api_view(['POST'])
@permission_classes([IsAdminUser])
def campus_managers(request, campus_id):
    def manager_create():
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method == 'POST':
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


