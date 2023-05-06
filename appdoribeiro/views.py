from django.shortcuts import render, redirect
from .models import Jogadore, Tecnico

# Create your views here.
def home(request):
  jogadores = Jogadore.objects.all()
  tecnicos = Tecnico.objects.all()
  context = { "jogadores": jogadores, "tecnicos": tecnicos }
  return render(request, "home.html", context=context)
  
def lista_jogadores(request):
  jogadores = Jogadore.objects.all()
  context = { "jogadores": jogadores }
  return render(request, "jogador.html", context=context)

def lista_tecnicos(request):
  tecnicos = Tecnico.objects.all()
  context = { "tecnicos": tecnicos }
  return render(request, "tecnico.html", context=context)

def forms_jogadores(request): #lado esquerdo: propriedade do modelo
  if request.method == "POST":
    if "jogou" not in request.POST:
      jogou_no_botafogo=False
    else:
      jogou_no_botafogo=True
    Jogadore.objects.create(
      nome=request.POST["nome"],
      data_de_nascimento=request.POST["data"],
      posicao=request.POST["posicao"],
      jogou_no_botafogo=jogou_no_botafogo
    )
    return redirect("lista_jogadores")
  return render(request, "form_jogador.html")

def forms_tecnicos(request):
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

"""jogador e o valor do context do update_jogador que está entre aspas, e o nome é o nome da variavel no modelo(isso no form_jogador)"""

def update_jogador(request, jogador_id):
  jogador = Jogadore.objects.get(id = jogador_id)
  jogador.data_de_nascimento = jogador.data_de_nascimento.strftime("%Y-%m-%d") #converter formato da data
  if request.method == "POST":
      jogador.nome=request.POST["nome"]
      jogador.data_de_nascimento=request.POST["data"]
      jogador.posicao=request.POST["posicao"]
      if "jogou" not in request.POST:
        jogador.jogou_no_botafogo=False
      else:
        jogador.jogou_no_botafogo=True
      jogador.save()
      return redirect("lista_jogadores")
  context = { "jogador": jogador }
  return render(request, "form_jogador.html", context=context)
  
def delete_jogador(request, jogador_id):
  jogador = Jogadore.objects.get(id = jogador_id)
  if request.method == "POST":
    if "confirm" in request.POST:
      jogador.delete()
    return redirect("lista_jogadores")
  context = { "jogador": jogador }
  return render(request, "delete_jogador.html", context=context)

def update_tecnico(request, tecnico_id):
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

def delete_tecnico(request, tecnico_id):
  tecnico = Tecnico.objects.get(id = tecnico_id)
  if request.method == "POST":
    if "confirm" in request.POST:
      tecnico.delete()
    return redirect("lista_tecnicos")
  context = { "tecnico": tecnico }
  return render(request, "delete_tecnico.html", context=context)
