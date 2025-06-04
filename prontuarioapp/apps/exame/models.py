from django.db import models

class Exame(models.Model):
    nomeExame = models.CharField(max_length=100, verbose_name='Nome do Exame')
    dataRealizacao = models.DateField(verbose_name='Data de Realização')
    resultado = models.TextField(verbose_name='Resultado do Exame')
    
    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exame'
        ordering =['id']
        

    def __str__(self):
        return self.nome