from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    senha = models.CharField(max_length=20)
    telefone = models.CharField(max_length=13)