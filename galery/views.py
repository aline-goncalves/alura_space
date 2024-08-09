from django.shortcuts import render

def index(request):
    return render(request, 'galery/index.html')

def imagem(request):
    return render(request, 'galery/imagem.html')