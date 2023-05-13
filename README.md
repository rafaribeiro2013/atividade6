Configuração do Django

1º passo: Criar uma Secret Key

python import secrets secrets.token_urlsafe(32)

Após isso, copie o resultado e insira numa secret key de nome 'SECRET_KEY' Depois, insira o comando

exit()

2º passo: Começar o app

python3 manage.py startapp <nome_do_seu_app>

3º passo: Exportar models para o admin do Django

python3 manage.py makemigrations python3 manage.py migrate python3 manage.py createsuperuser

4º passo: Rode o programa

python3 manage.py runserver 0.0.0.0:3000
