from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def curso_detalhes(request):
    return render(request, 'curso_detalhe.html')

def cursos(request):
    return render(request, 'cursos.html')

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')
