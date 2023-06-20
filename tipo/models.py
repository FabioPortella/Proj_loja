from django.db import models

class Tipos(models.Model):
    titulo = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return f"{self.titulo}"

