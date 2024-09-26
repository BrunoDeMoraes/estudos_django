from django.db import models

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descrição = models.TextField(null=False, blank=False)
    fotos = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return f'Fotograia [nome={self.nome}]'
