from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'receita'

router = routers.DefaultRouter()
router.register('', views.ReceitaViewSet, basename='receita')

urlpatterns = [
    path('', include(router.urls) )
]