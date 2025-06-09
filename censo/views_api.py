# censo/views_api.py

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Domicilio, Pessoa
from .serializers import DomicilioSerializer, PessoaSerializer


class DomicilioViewSet(viewsets.ModelViewSet):
    """
    ViewSet para CRUD completo de Domicilio.
    """
    queryset = Domicilio.objects.all()
    serializer_class = DomicilioSerializer
    permission_classes = [AllowAny]
    # Se quiser filtragem básica, você pode habilitar:
    # filterset_fields = ['bairro', 'cidade', 'uf', 'rua']


class PessoaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para CRUD completo de Pessoa.
    """
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = [AllowAny]
    # Para filtros, por exemplo:
    # filterset_fields = ['sexo', 'parentesco', 'nome', 'sobrenome']

