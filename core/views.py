from django.shortcuts import render, redirect
from .models import Area, PublicoAlvo, Curso
from .forms import AreaForm, PublicoAlvoForm, CursoForm
from django.contrib.auth import authenticate, login, logout
# Usuários
from .models import Usuario
from .forms import UsuarioFormCadastro
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def cadastro(request):
    form = UsuarioFormCadastro(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'cadastro.html')

def curso_detalhes(request):
    return render(request, 'curso_detalhes.html')

def cursos(request):
    return render(request, 'cursos.html')

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')
