from django.db import models

class Pessoa(models.Model):
    cpf = models.CharField('CPF', max_length=11, unique=True)
    nome = models.CharField('Nome', max_length=50)
    dataNascimento = models.DateField('Data de Nascimento', max_length=100)
    
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering =['id']
        abstract = True

    def __str__(self):
        return self.nome