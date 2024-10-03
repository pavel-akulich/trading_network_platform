"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Онлайн платформа торговой сети электроники",
        default_version='v1',
        description="API документация. Для поиска в документации вы можете использовать Ctrl+F",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="pavelakulich1999@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
                  path('openapi/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('openapi/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

                  path('admin/', admin.site.urls),
                  path('api/users/', include('users.urls', namespace='users')),
                  path('api/products/', include('products.urls', namespace='products')),
                  path('api/networks/', include('trading_networks.urls', namespace='networks')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
