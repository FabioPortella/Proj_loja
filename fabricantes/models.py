from django.db import models
from tipo.models import Tipos

class Fabricante(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    tipo = models.ForeignKey(Tipos, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return f'{self.nome}'