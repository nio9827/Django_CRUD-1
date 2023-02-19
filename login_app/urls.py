from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('registro', views.registro, name="registro"),
    path('tarea', views.tarea, name="tarea"),
    path('cerrar_sesion', views.cerrar_sesion, name="cerrar_sesion"),
    path('logiarse', views.logiarse, name="logiarse"),
    path ('tarea_complet', views.tarea_complet, name='tarea_complet' ),

    ]

