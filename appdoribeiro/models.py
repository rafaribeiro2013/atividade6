from django.db import models

# Create your models here.
class Jogadore(models.Model): 
  nome = models.CharField(max_length = 50)
  data_de_nascimento = models.DateField()
  posicao = models.CharField(max_length = 50)
  jogou_no_botafogo = models.BooleanField()

class Tecnico(models.Model):
  nome = models.CharField(max_length = 50)
  data_de_nascimento = models.DateField()
  tempo_de_trabalho_no_botafogo = models.IntegerField()
  ganhou_titulos = models.BooleanField()