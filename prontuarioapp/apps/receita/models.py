from django.db import models

class Receita(models.Model):
    medicamento = models.CharField(max_length=255, blank=False, null=False)
    dataEmissao = models.DateField(blank=False, null=False)
    validade = models.DateField(blank=False, null=False)

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
        ordering =['id']
        

    def __str__(self):
        return self.medicamento