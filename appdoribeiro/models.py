from django.db import models

# Create your models here.
class Jogadore(models.Model): #modelo de nome Jogadore, sendo os atributos, ou seja, as características desse modelo a serem inseridas as váriaveis nome, data_de_nascimento, posicao e jogou_no_botafogo
  nome = models.CharField(max_length = 50) #CharField serve para criar um espaço para escrever caracteres, e o max_length determina o número máximo de caracteres que podem ser digitados
  data_de_nascimento = models.DateField() #DateField serve para criar um campo com seleção de data
  posicao = models.CharField(max_length = 50)
  jogou_no_botafogo = models.BooleanField() #BooleanField cria uma checkbox para marcar ou deixar em branco

class Tecnico(models.Model): #o mesmo que vale para o modelo Jogadore, vale para o modelo Tecnico, só que as variáveis tem nomes e valores diferentes (não precisa obrigatoriamente ser diferente)
  nome = models.CharField(max_length = 50)
  data_de_nascimento = models.DateField()
  tempo_de_trabalho_no_botafogo = models.IntegerField() #IntegerField serve para escrever números inteiros
  ganhou_titulos = models.BooleanField()