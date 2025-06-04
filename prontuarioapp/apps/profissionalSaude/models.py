from django.db import models

class ProfissonalSaude(models.Model):
    cpf = models.CharField('CPF', max_length=11, unique=True)
    nome = models.CharField('Nome', max_length=50)
    dataNascimento = models.DateField('Data de Nascimento', max_length=100)
    registroConselho = models.CharField('Registro no Conselho', max_length=20, unique=True)
    especialidade = models.CharField('Especialidade', max_length=50)
    tipoProfissional = models.CharField('Tipo de Profissional', max_length=50, choices=[
        ('Medico', 'Médico'),
        ('Enfermeiro', 'Enfermeiro'),
        ('Fisioterapeuta', 'Fisioterapeuta'),
        ('Psicologo', 'Psicólogo'),
        ('Outro', 'Outro')
    ])
    
    class Meta:
        verbose_name = 'Profissional de Saúde'
        verbose_name_plural = 'Profissionais de Saúde'
        ordering =['id']
        

    def __str__(self):
        return self.nome