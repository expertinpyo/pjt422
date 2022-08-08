from django.urls import path
from .views import *

urlpatterns = [
    path('', ManagerAllView.as_view()),
    path('<int:user_pk>/', ManagerView.as_view()),
]