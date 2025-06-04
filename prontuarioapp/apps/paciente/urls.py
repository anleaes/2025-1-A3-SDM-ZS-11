from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'paciente'

router = routers.DefaultRouter()
router.register('', views.PacienteViewSet, basename='paciente')

urlpatterns = [
    path('', include(router.urls) )
]