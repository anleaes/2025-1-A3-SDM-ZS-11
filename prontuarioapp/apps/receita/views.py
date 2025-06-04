from .models import Receita
from rest_framework import viewsets
from .serializer import ReceitaSerializer

class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer 