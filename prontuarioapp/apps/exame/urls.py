from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'paciente'

router = routers.DefaultRouter()
router.register('', views.ExameViewSet, basename='exame')

urlpatterns = [
    path('', include(router.urls) )
]