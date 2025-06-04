from .models import ProfissonalSaude
from rest_framework import viewsets
from .serializer import ProfissionalSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = ProfissonalSaude.objects.all()
    serializer_class = ProfissionalSerializer 