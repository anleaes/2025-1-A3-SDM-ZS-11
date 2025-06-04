from django.db import models
from exame.models import Exame
from paciente.models import Paciente
from receita.models import Receita



class Prontuario(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='prontuarios', default=1)
    exames = models.ManyToManyField(Exame, blank=True, related_name='Exames')
    conteudo = models.TextField(blank=True, null=True)
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE, related_name='receitas', default=1)

    class Meta:
        verbose_name = 'Prontuário'
        verbose_name_plural = 'Prontuários'
        ordering =['id']
        

    def __str__(self):
        return self.nome