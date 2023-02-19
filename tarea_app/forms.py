from django.forms import ModelForm # Importamos el ModelForm
from .models import Tareamodel # Importamos el modelo Tarea

class TareaForm(ModelForm): # Creamos el formulario
    class Meta: # Creamos la clase Meta
        model = Tareamodel # Definimos el modelo
        fields = ['titulo', 'descripcion', 'important'] # Definimos los campos que queremos que se muestren en el formulario