from django.shortcuts import render, get_object_or_404, redirect # Se importa la funcion render
from .forms import TareaForm # Se importa el formulario de tareas
from .models import Tareamodel # Se importa el modelo de tareas
from django.utils import timezone # Se importa la libreria timezone
# Create your views here.
from django.contrib.auth.decorators import login_required  # importamos el decorador de login_required

@login_required  # decoramos la vista tarea
def Tareas(request): # Funcion que se encarga de mostrar las tareas

    if request.method == 'GET': # Si el metodo es GET, se muestra el formulario
        return render(request, 'tareas.html', {'tareas': TareaForm}) # Se muestra el formulario
    
    else: # Si el metodo es POST, se guarda la tarea
        try: # Se intenta guardar la tarea
            form = TareaForm(request.POST) # Se crea el formulario con los datos enviados por POST
            nueva_tarea = form.save(commit=False) # Se guarda la tarea en la base de datos
            nueva_tarea.user = request.user # Se asigna el usuario que creo la tarea
            nueva_tarea.save() # Se guarda la tarea en la base de datos
            #print (nueva_tarea)
            #print (request.POST) # Imprime los datos que se envian por POST
            return redirect('tarea')
        except ValueError: # Si no se puede guardar la tarea, se muestra el formulario con un mensaje de error
            return render(request, 'tareas.html', {'tareas': TareaForm, 'error': 'Datos incorrectos'}) # Se muestra el formulario con un mensaje de error

@login_required  # decoramos la vista tarea
def obtener_tareas(request, tarea_id):

    if request.method == 'GET':
        t = get_object_or_404(Tareamodel, pk=tarea_id, user=request.user)
        tform = TareaForm(instance=t)
    #t = Tareamodel.objects.get(id=tarea_id) # Se obtiene la tarea con el id que se envia por parametro
        return render(request, 'obtener_tareas.html', {'tarea1': t, 'tarea2': tform}) 
    
    else:
        try:
            t = get_object_or_404(Tareamodel, pk=tarea_id, user=request.user)
            tform = TareaForm(request.POST, instance= t)
            tform.save()
            return redirect('tarea')
            #print (request.POST)
        except ValueError:

            return render(request, 'obtener_tareas.html', {'tarea1': t, 'tarea2': tform, 'error': 'Error al actualizar la tarea'})

@login_required  # decoramos la vista tarea
def completar_tarea(request, tarea_id):
    tc = get_object_or_404(Tareamodel, pk=tarea_id, user=request.user)

    if request.method == 'POST':
        tc.datecompleted = timezone.now()
        tc.save()
        return redirect('tarea')
    

@login_required  # decoramos la vista tarea
def eliminar_tarea(request, tarea_id):
    te = get_object_or_404(Tareamodel, pk=tarea_id, user=request.user)

    if request.method == 'POST':
        te.delete()
        return redirect('tarea')

