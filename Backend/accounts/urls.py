from django.urls import path
from . import views

urlpatterns = [
    path('', views.managers),  # 전체 매니저
    path('<int:campus_id>/', views.campus_managers),
    path('user/<int:user_pk>/', views.manager_detail),
    path('master/<int:user_pk>/', views.edit_managers) # master 관리자가 전체 관리자 회원정보 수정
]