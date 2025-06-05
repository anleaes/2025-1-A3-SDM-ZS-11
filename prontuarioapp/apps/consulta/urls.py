from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'consulta'

router = routers.DefaultRouter()
router.register('', views.ConsultaViewSet, basename='consulta')

urlpatterns = [
    path('', include(router.urls) )
]