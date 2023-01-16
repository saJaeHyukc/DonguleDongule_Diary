from rest_framework import permissions

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="동글동글 다이어리",
        default_version='v1',
        description="동글동글 다이어리 API",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="wogur981208@gmail.com"),
        license=openapi.License(name="DonguleDongule Diary License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    
    # Apps
    path('users/', include('users.urls')),
    path('users/', include('dj_rest_auth.urls')),
    path('users/', include('allauth.urls')),
    
    # Swagger
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/api.json/', schema_view.without_ui(cache_timeout=0), name='schema-swagger-json'), 
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)