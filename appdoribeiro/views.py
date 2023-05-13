from django.shortcuts import render, redirect
from .models import Jogadore, Tecnico

# Create your views here.
def home(request): #renderiza o html da página principal, carregando todos os objetos criados para os dois modelos e voltando para a url que está associada a essa view
  jogadores = Jogadore.objects.all()#pega todos os objetos atuais, do modelo Jogadore, registrados no banco de dados 
  tecnicos = Tecnico.objects.all()#pega todos os objetos atuais, do modelo Tecnico, registrados no banco de dados 
  context = { "jogadores": jogadores, "tecnicos": tecnicos }
  return render(request, "home.html", context=context)
  
def lista_jogadores(request): #essa view está relacionada com a página principal também, então só serve para carregar o html dos dados dos jogadores
  jogadores = Jogadore.objects.all()
  context = { "jogadores": jogadores }
  return render(request, "jogador.html", context=context)

def lista_tecnicos(request): #a mesma lógica da view acima se aplica para essa
  tecnicos = Tecnico.objects.all()
  context = { "tecnicos": tecnicos }
  return render(request, "tecnico.html", context=context)

def forms_jogadores(request): #view do formulário de jogadores; ela vai analisar os dados inseridos pelo usuário (a partir do método POST) e vai criar o objeto, fazendo o pedido
#para o html que contém o formulário dos jogadores, e vai redirecionar de volta para a função lista_jogadores, que é a view que está relacionada com a página principal
  if request.method == "POST":
    if "jogou" not in request.POST: #verificação da check box marcada ou não
      jogou_no_botafogo=False
    else:
      jogou_no_botafogo=True
    Jogadore.objects.create( #criação do objeto
      nome=request.POST["nome"],
      data_de_nascimento=request.POST["data"],
      posicao=request.POST["posicao"],
      jogou_no_botafogo=jogou_no_botafogo
    )
    return redirect("lista_jogadores")
  return render(request, "form_jogador.html")

def forms_tecnicos(request): #a explicação da view acima se aplica para esta
  if request.method == "POST":
    if "ganhou" not in request.POST:
      ganhou_titulos=False
    else:
      ganhou_titulos=True
    Tecnico.objects.create(
      nome=request.POST["nome"],
      data_de_nascimento=request.POST["data"],
      tempo_de_trabalho_no_botafogo=request.POST["tempo"],
      ganhou_titulos=ganhou_titulos
    )
    return redirect("lista_tecnicos")
  return render(request, "form_tecnico.html")

"""jogador é o valor do context do update_jogador que está entre aspas, e o nome é o nome da variavel no modelo(isso no form_jogador)"""

def update_jogador(request, jogador_id): #função para atualizar as informações de um objeto já existente e redirecionar de volta para a página principal com as informações atualizadas
  jogador = Jogadore.objects.get(id = jogador_id) #pega o id referente ao objeto
  jogador.data_de_nascimento = jogador.data_de_nascimento.strftime("%Y-%m-%d") #converter formato da data
  if request.method == "POST":#atualização das informações de cada atributo do objeto
      jogador.nome=request.POST["nome"]
      jogador.data_de_nascimento=request.POST["data"]
      jogador.posicao=request.POST["posicao"]
      if "jogou" not in request.POST:
        jogador.jogou_no_botafogo=False
      else:
        jogador.jogou_no_botafogo=True
      jogador.save()#salva o "novo" objeto
      return redirect("lista_jogadores")
  context = { "jogador": jogador }
  return render(request, "form_jogador.html", context=context)
  
def delete_jogador(request, jogador_id):#função para deletar um objeto do banco de dados e redirecionar para a página principal sem o objeto que foi excluído
  jogador = Jogadore.objects.get(id = jogador_id)#pega o id do objeto, igual na função de update
  if request.method == "POST":
    if "confirm" in request.POST:#confirmando se a checkbox de deleção foi apertada ou não
      jogador.delete()#deleta o objeto
    return redirect("lista_jogadores")
  context = { "jogador": jogador }
  return render(request, "delete_jogador.html", context=context)

def update_tecnico(request, tecnico_id):#toda a explicação da update_jogador serve para essa função
  tecnico = Tecnico.objects.get(id = tecnico_id)
  tecnico.data_de_nascimento = tecnico.data_de_nascimento.strftime("%Y-%m-%d")
  if request.method == "POST":
    tecnico.nome=request.POST["nome"]
    tecnico.data_de_nascimento=request.POST["data"]
    tecnico.tempo_de_trabalho_no_botafogo=request.POST["tempo"]
    if "ganhou" not in request.POST:
      tecnico.ganhou_titulos = False
    else:
      tecnico.ganhou_titulos = True
    tecnico.save()
    return redirect("lista_tecnicos")
  context = { "tecnico": tecnico }
  return render(request, "form_tecnico.html", context=context)

def delete_tecnico(request, tecnico_id):#toda a explicação da delete_jogador serve para essa função
  tecnico = Tecnico.objects.get(id = tecnico_id)
  if request.method == "POST":
    if "confirm" in request.POST:
      tecnico.delete()
    return redirect("lista_tecnicos")
  context = { "tecnico": tecnico }
  return render(request, "delete_tecnico.html", context=context)
