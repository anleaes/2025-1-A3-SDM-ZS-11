from .models import Exame
from rest_framework import viewsets
from .serializer import ExameSerializer

class ExameViewSet(viewsets.ModelViewSet):
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer 