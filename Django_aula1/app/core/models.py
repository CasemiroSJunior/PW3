from django.db import models

class FeriadoModel(models.Model):
    nome = models.CharField("Feriado", max_length=50)
    dia = models.IntegerField("Dia")
    mes = models.IntegerField("Mês")
    modificacao = models.DateTimeField(verbose_name="Modificado em", auto_now_add=False, auto_now=True)

    def __str__(self):
        text= f"{self.nome} - Dia: {self.dia}/{self.mes}"
        return text
