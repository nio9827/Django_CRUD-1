from django import forms # Importamos el ModelForm
from .models import Tareamodel # Importamos el modelo Tarea

class TareaForm(forms.ModelForm): 
     # Creamos el formulario TareaForm que hereda de ModelForm
    class Meta: # Creamos la clase Meta para definir el modelo y los campos que queremos que se muestren en el formulario
        model = Tareamodel # Definimos el modelo
        fields = ['titulo', 'descripcion', 'important'] # Definimos los campos que queremos que se muestren en el formulario
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control' }),
            'descripcion': forms.Textarea(attrs={'class': 'form-control' }),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input' }),
        }
        