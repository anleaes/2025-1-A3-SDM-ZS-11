from .models import Paciente
from rest_framework import viewsets
from .serializer import PacienteSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer 