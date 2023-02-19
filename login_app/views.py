# importamos el metodo render y redirect
from django.shortcuts import render, redirect
# importamos el formulario de creacion de usuarios y el formulario de autenticacion
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User  # importamos el modelo de usuario
# importamos el metodo de login y logout
from django.contrib.auth import login, logout, authenticate
# importamos la excepcion de error de integridad
from django.db import IntegrityError
# Create your views here.
# importamos el modelo de la base de datos
from tarea_app.models import Tareamodel
from django.contrib.auth.decorators import login_required  # importamos el decorador de login_required

def home(request):  # creamos la vista home
    return render(request, "home.html")  # renderizamos la pagina home.html


def registro(request):  # creamos la vista registro

    if request.method == "GET":  # si el metodo es GET
        # renderizamos la pagina registro.html con el formulario de creacion de usuarios
        return render(request, "registro.html", {'userform': UserCreationForm})

    else:
        # si las contraseñas coinciden
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],  # creamos el usuario
                                                password=request.POST['password1'])
                user.save()  # guardamos el usuario
                login(request, user)  # iniciamos sesion
                # redireccionamos a la pagina tarea.html
                return redirect('tarea')

            except IntegrityError:  # si el usuario ya existe

                # renderizamos la pagina registro.html con el formulario de creacion de usuarios y el error de usuario ya existente
                return render(request, "registro.html", {'userform': UserCreationForm, 'error': 'El usuario ya existe'})

        # renderizamos la pagina registro.html con el formulario de creacion de usuarios y el error de contraseñas no coincidentes
        return render(request, "registro.html", {'userform': UserCreationForm, 'error': 'Las contraseñas no coinciden'})


@login_required  # decoramos la vista tarea
def tarea(request):  # creamos la vista tarea

    # filtramos las tareas por el usuario que inicio sesion
    tareas = Tareamodel.objects.filter(
        user=request.user, datecompleted__isnull=True)
    # renderizamos la pagina tarea.html
    return render(request, "tarea.html", {'tareas': tareas})

@login_required  # decoramos la vista crear_tarea
def tarea_complet(request):  # creamos la vista tarea_complet
    tareas = Tareamodel.objects.filter(
        user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, "tarea.html", {'tareas': tareas})


@login_required  # decoramos la vista crear_tarea
def cerrar_sesion(request):  # creamos la vista cerrar_sesion
    logout(request)  # cerramos sesion
    return redirect('home')  # redireccionamos a la pagina home.html


def logiarse(request):  # creamos la vista logiarse
    if request.method == "GET":  # si el metodo es POST
        # renderizamos la pagina login.html con el formulario de autenticacion
        return render(request, "login.html", {'form': AuthenticationForm})

    else:
        # autenticamos al usuario
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        # si el usuario existe
        if user is None:
            return render(request, "login.html", {'form': AuthenticationForm, 'error': 'Usuario o contraseña incorrectos'})
        else:
            login(request, user)
            return redirect('tarea')
