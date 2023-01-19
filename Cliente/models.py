from django.db import models

class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.nome
