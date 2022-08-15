from django.urls import path
from .views import *

urlpatterns = [
    path('building/<int:building_pk>/<dates>/', BuildingDailyView.as_view()),   # 빌딩 일간 데이터 조회
    path('building/<int:building_pk>/week/<dates>/', BuildingWeeklyView.as_view()),   # 빌딩 주간 데이터 조회
    path('building/<int:building_pk>/month/<months>/', BuildingMonthlyView.as_view()),  # 빌딩 월간 데이터 조회
    path('building/<int:building_pk>/year/<year>/', BuildingYearView.as_view()),    # 빌딩 연간 데이터 조회
    
    path('floor/<int:floor_pk>/<dates>/', FloorDailyView.as_view()),    # 층 일간 데이터 조회
    path('floor/<int:floor_pk>/week/<dates>/', FloorWeeklyView.as_view()),    # 층 주간 데이터 조회
    path('floor/<int:floor_pk>/month/<months>/', FloorMonthlyView.as_view()),  # 층 월간 데이터 조회
    path('floor/<int:floor_pk>/year/<year>/', FloorYearView.as_view()),    # 층 연간 데이터 조회
    
    path('trashbin/<token>/<dates>/', TrashbinDailyView.as_view()),     # 쓰레기통 일간 데이터 조회
    path('trashbin/<token>/week/<dates>/', TrashbinWeeklyView.as_view()),   # 쓰레기통 주간 데이터 조회
    path('trashbin/<token>/month/<months>/', TrashbinMonthlyView.as_view()),  # 빌딩 월간 데이터 조회
    path('trashbin/<token>/year/<year>/', TrashbinYearView.as_view()),    # 빌딩 연간 데이터 조회
    
]