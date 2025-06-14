from .models import Pessoa
from rest_framework import viewsets
from .serializer import PessoaSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer 