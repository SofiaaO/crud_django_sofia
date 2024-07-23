from django.urls import path
from myapp.views import *

urlpatterns = [
    path('autor/', autor_lista, name="Lista_Autores"),
    path('autor/crear/', crear_autor, name="Crear_Autor"),
    path('autor/modificar/<int:pk>/', autor_modificar, name="Modificar_Autor"),
    path('autor/eliminar/<int:pk>/', autor_eliminar, name="Eliminar_Autor"),

    path('obra/', obra_lista, name="Lista_Obras"),
    path('obra/crear/', crear_obra, name="Crear_Obra"),
    path('obra/modificar/<int:pk>/', obra_modificar, name='Modificar_Obra'),
    path('obra/eliminar/<int:pk>/', obra_eliminar, name='Eliminar_Obra'),
]