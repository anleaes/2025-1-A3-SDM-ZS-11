from django.db import models
from exame.models import Exame


class Prontuario(models.Model):
    
    exames = models.ManyToManyField(Exame, blank=True, related_name='Exames')
    conteudo = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Prontuário'
        verbose_name_plural = 'Prontuários'
        ordering =['id']
        

    def __str__(self):
        return self.nome