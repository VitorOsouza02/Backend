
from django.urls import path, include
from rest_framework import routers
from .views_api import DomicilioViewSet, PessoaViewSet

router = routers.DefaultRouter()
router.register(r'domicilios', DomicilioViewSet, basename='domicilio')
router.register(r'pessoas', PessoaViewSet, basename='pessoa')

urlpatterns = [
    path('', include(router.urls)),    # <— agora o router fica na raiz do app
]

