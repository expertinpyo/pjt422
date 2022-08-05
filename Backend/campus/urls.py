from django.urls import path
from . import views

urlpatterns = [
    path('', views.campuses),  # 전체 캠퍼스 목록 조회 및 캠퍼스 추가
    path('notification/', views.notification), # 쓰레기통 알림
    path('<int:campus_pk>/', views.campus), # 특정 캠퍼스 세부사항 + 해당 캠퍼스 내 건물 목록 조회, 캠퍼스 수정 및 삭제

    path('building/<int:building_pk>/', views.building), # 특정 빌딩 세부사항 + 해당 빌딩 내 모든 층 목록 조회, 빌딩 수정 및 삭제
    path('floor/<int:floor_pk>/', views.floor), # 특정 층 세부사항 + 모든 쓰레게통 조회, 층 수정 및 삭제 
    
    path('trashbin/<int:trashbin_pk>/', views.trashbin), # 특정 쓰레기통 조회, 수정 및 삭제

    path('<int:campus_pk>/manager/', views.managers),  # 해당 캠퍼스 + 관리자 목록 조회, 추가
    # path('<int:campus_pk>/manager/<int:manager_pk>', views.manager_detail),  # 매니저 수정, 삭제
    path('<int:campus_pk>/student/', views.students),  # 해당 캠퍼스 + 학생 목록 조회, 추가
    path('<int:campus_pk>/student/<int:student_pk>/', views.student_detail),  # 학생 수정, 삭제
    
    path('test/<rfid>/<int:trashbin_pk>/', views.test),
    path('all/<str:rfid>/', views.check_all),  # 신원 조회

    # path('trashbin/check/', views.trashbin_check),
    # path('trashbins/status/', views.trashbin_status),
    

    # path('<int:campus_pk>/building', views.campus),  # 특정 캠퍼스 내 빌딩 추가
    # path('building/<int:building_pk>/floor/', ),  # 특정 빌딩 내 층 추가
    # path('floor/<int:floor_pk>/trashbin/',), # 특정 층 내 쓰레기통 추가
]
