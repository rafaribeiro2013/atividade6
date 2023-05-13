from django.contrib import admin
from .models import Jogadore, Tecnico

# Register your models here.
admin.site.register(Jogadore) #registra o modelo Jogadore no admin do Django
admin.site.register(Tecnico) #registra o modelo Tecnico no admin do Django