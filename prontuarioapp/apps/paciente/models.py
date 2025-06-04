from django.db import models

class Paciente(models.Model):
    cpf = models.CharField('CPF', max_length=11, unique=True)
    nome = models.CharField('Nome', max_length=50)
    dataNascimento = models.DateField('Data de Nascimento', max_length=100)
    
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Paciente'
        ordering =['id']
        

    def __str__(self):
        return self.nome