from django.db import models
from django.contrib.auth.models import AbstractUser, Group


# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Arquivo(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.arquivo.name + ' - ' + self.pessoa.nome

