from django.db import models  #importamos el modelo de django
from django.contrib.auth.models import User #importamos el modelo de usuario de django
# Create your models here.

class Tareamodel(models.Model): #Tarea es el nombre de la tabla en la base de datos
    titulo = models.CharField(max_length=100) #titulo es el nombre de la columna en la base de datos
    descripcion = models.TextField(blank=True) #descripcion es el nombre de la columna en la base de datos
    created = models.DateTimeField(auto_now_add=True) #created es el nombre de la columna en la base de datos
    datecompleted = models.DateTimeField(null=True, blank=True) #datecompleted es el nombre de la columna en la base de datos
    important =  models.BooleanField(default=False) #important es el nombre de la columna en la base de datos
    user =  models.ForeignKey(User, on_delete=models.CASCADE) #user es el nombre de la columna en la base de datos y es una llave foranea que hace referencia a la tabla User de la base de datos

    def __str__(self): #metodo que nos permite mostrar el titulo de la tarea y el usuario que la creo
        return self.titulo + ' by ' + str(self.user) #retornamos el titulo de la tarea y el usuario que la creo