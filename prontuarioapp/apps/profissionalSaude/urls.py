from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ProfissionalSaude'

router = routers.DefaultRouter()
router.register('', views.ProfissionalViewSet, basename='ProfissionalSaude')

urlpatterns = [
    path('', include(router.urls) )
]