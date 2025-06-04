from .models import Prontuario
from rest_framework import viewsets
from .serializer import ProntuarioSerializer

class ProntuarioViewSet(viewsets.ModelViewSet):
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer 