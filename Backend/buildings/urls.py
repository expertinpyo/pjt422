from django.urls import path
from . import views
urlpatterns = [
    path('<int:floor_num>/', views.floor),
]
