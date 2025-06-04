from django.db import models
from paciente.models import Paciente
from profissionalSaude.models import ProfissonalSaude
from prontuario.models import Prontuario

class Consulta(models.Model):
    profissional = models.ForeignKey(ProfissonalSaude, on_delete=models.CASCADE, related_name='consultas', default=1)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas', default=1)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE, related_name='consultas', default=1)
    dataConsulta = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consulta'
        ordering =['id']
        

    def __str__(self):
        return self.nome