from django.shortcuts import render
from galeria.models import Fotografia


def index(request):

    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {'cards': fotografias})


def imagem(request, foto_id):
    return render(request, 'galeria/imagem.html')
