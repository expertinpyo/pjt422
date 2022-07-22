from django.urls import path
from . import views

urlpatterns = [
    path('', views.campuses),  # 전체 캠퍼스 목록 조회
    path('<int:campus_pk>/', views.campus),  # 해당 캠퍼스 + 빌딩 목록 조회
    path('<int:campus_pk>/manager/', views.campus_manager),  # 해당 캠퍼스 + 관리자 목록 조회
    path('<int:campus_pk>/student/', views.campus_student),  # 해당 캠퍼스 + 학생 목록 조회
    path('building/<int:building_pk>', views.building),  # 해당 빌딩 + 전체 층 목록 조회

]