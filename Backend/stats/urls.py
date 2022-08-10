from django.urls import path
from .views import *

urlpatterns = [
    path('<dates>/', TestView.as_view())
]