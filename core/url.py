from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('cadastro/', cadastro, name='cadastro'),
    path('curso_detalhes/', curso_detalhes, name='curso_detalhes'),
    path('cursos/', cursos, name='cursos'),
    path('login/', login, name='login'),
]