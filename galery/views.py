from django.shortcuts import render, get_object_or_404, redirect
from galery.models import Photo, Category
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!')
        return redirect('login')
    
    return render(request, 'galery/index.html', {"tags": return_categories(),"cards": return_photos()})

def photo(request, photo_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!')
        return redirect('login')
    
    return render(request, 'galery/imagem.html', {"photo": return_photo(photo_id)})

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!')
        return redirect('login')
    
    return render(request, 'galery/search.html', {"cards": return_photos_search(request)})

def return_photos_search(request):
    photos = Photo.objects.all()
    
    if "search" in request.GET:
        name_to_search = request.GET['search']
        if name_to_search:
            photos = photos.filter(title__icontains=name_to_search)
        
    return photos

def return_photos():
    return Photo.objects.order_by("created_at").filter(published=True)    

def return_photo(photo_id):
    return get_object_or_404(Photo, pk=photo_id)  

def return_categories():
    return Category.objects.filter(active=True)