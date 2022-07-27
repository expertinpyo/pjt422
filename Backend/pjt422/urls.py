from django.contrib import admin
from django.urls import path, include

# for swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path


schema_view = get_schema_view(
    openapi.Info(
        title="A207 PJT 422",
        default_version='v1',
    #   description="Test description",
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@snippets.local"),
    #   license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/accounts/', include('dj_rest_auth.urls')), # django accounts template 이용
    path('api/v1/campus/', include('campus.urls')),
    path('api/v1/stats/', include('stats.urls')),
    path('swagger/', schema_view.with_ui('swagger')),
]
