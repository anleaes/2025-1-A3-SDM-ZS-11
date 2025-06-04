from .models import ProfissonalSaude
from rest_framework import serializers

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfissonalSaude
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']