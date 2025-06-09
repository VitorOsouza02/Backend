

# config/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API de Coleta de Dados (Censo)",
        default_version='v1',
        description="Documentação Swagger para o app Censo",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Endpoint para obtenção de token
    path('api/token/', obtain_auth_token, name='api_token_auth'),

    # Admin do Django
    path('admin/', admin.site.urls),

    # Aqui: inclui todo o “censo/urls.py” sob o prefixo "/api/"
    path('api/', include('censo.urls')),

    # Swagger/OpenAPI
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
