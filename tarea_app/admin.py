from django.contrib import admin
from .models import Tareamodel
# Register your models here.

class TareaAdmin(admin.ModelAdmin): # Creamos la clase TareaAdmin
    readonly_fields = ('created',) # Definimos los campos que queremos que sean de solo lectura

admin.site.register(Tareamodel, TareaAdmin) # Registramos el modelo Tarea en el administrador