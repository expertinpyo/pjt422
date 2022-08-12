from django.urls import path
from .views import *

urlpatterns = [
    path('<dates>/', TestView.as_view()),
    path('building/<int:building_pk>/<dates>/', BuildingDailyView.as_view()),
    # path('building/<int:building_pk>/month/<months>/', BuildingMonthlyView.as_view()),
    # path('building/<int:building_pk>/year/<year>/', BuildingYearView.as_view()),
    path('floor/<int:floor_pk>/<dates>/', FloorDailyView.as_view()),
    path('pandas/floor/<int:floor_pk>/<months>/', PandasTestView.as_view()),
    path('trashbin/<token>/<dates>/', TrashbinDailyView.as_view()),
    
]