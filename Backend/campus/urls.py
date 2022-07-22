from django.urls import path
from . import views

urlpatterns = [
    path('', views.campuses),  # 전체 캠퍼스 목록 조회
    path('<int:campus_pk>/', views.campus),  # 해당 캠퍼스 + 빌딩 목록 조회
    path('<int:campus_pk>/manager/', views.campus_manager),  # 해당 캠퍼스 + 관리자 목록 조회
    path('<int:campus_pk>/student/', views.campus_student),  # 해당 캠퍼스 + 학생 목록 조회

    path('<int:campus_pk>/students/', views.students), # 학생 추가
    path('<int:campus_pk>/student/<int:student_pk>/', views.student_detail), # 학생 수정, 삭제
    path('<int:campus_pk>/<int:building_pk>/floor/', views.floor_create),  # 층 추가
    path('<int:campus_pk>/<int:building_pk>/floor/<int:floor_pk>/', views.floor_UD), # 층 수정, 삭제
    path('<int:campus_pk>/<int:floor_pk>/trashbins/', views.floor_trashbins) # 층 내 모든 쓰레기통 조회, 추가
]