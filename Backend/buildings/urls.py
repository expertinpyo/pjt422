from django.urls import path
from . import views
urlpatterns = [
    path('', views.buildings),
    path('<b_name>/', views.floors),
    
]
