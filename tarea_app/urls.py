from django.urls import path
from . import views

urlpatterns = [
    path('Tareas/', views.Tareas, name='Tareas'), # Se crea la ruta para la funcion Tareas
    path('obtener_tareas/<int:tarea_id>', views.obtener_tareas, name='obtener_tareas'), # Se crea la ruta para la funcion obtener_tareas
    path('completar_tarea/<int:tarea_id>', views.completar_tarea, name='completar_tarea'), # Se crea la ruta para la funcion completar_tarea
    path('eliminar_tarea/<int:tarea_id>', views.eliminar_tarea, name='eliminar_tarea'), # Se crea la ruta para la funcion eliminar_tarea
]

