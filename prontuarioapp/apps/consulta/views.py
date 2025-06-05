from .models import Consulta
from rest_framework import viewsets
from .serializer import ConsultaSerializer

class ProntuarioViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer 
