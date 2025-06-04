from django.db import models
from apps.pessoa.models import Pessoa
 

class Paciente(Pessoa):

    def __str__(self):
        return f'{self.nome} - Prontuário: {self.numero_prontuario}'