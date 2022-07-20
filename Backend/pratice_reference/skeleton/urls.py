from django.urls import path, include

urlpatterns = [
    path('buildings/', include('buildings.urls')),
    path('accounts/', include('accounts.urls')),
]
