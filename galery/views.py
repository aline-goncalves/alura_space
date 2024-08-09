from django.shortcuts import render, get_object_or_404
from galery.models import Photo

def index(request):
    return render(request, 'galery/index.html', {"cards": return_photos()})

def imagem(request, photo_id):
    return render(request, 'galery/imagem.html', {"photo": return_photo(photo_id)})

def return_photos():
    return Photo.objects.all()    

def return_photo(photo_id):
    return get_object_or_404(Photo, pk=photo_id)  