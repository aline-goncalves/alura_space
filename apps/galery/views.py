from django.shortcuts import render, get_object_or_404, redirect
from apps.galery.models import Photo, Category
from apps.galery.forms import PhotoForm
from django.contrib import messages

def home(request):
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
    
    return render(request, 'galery/index.html', {"cards": return_photos_search(request)})

def new_photo(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!')
        return redirect('login')
    
    form = PhotoForm
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        
        if form.is_valid:
            form.save()
            messages.success(request, 'Nova imagem cadastrada com sucesso!')
            return redirect('home')
            
    return render(request, 'galery/new_photo.html', {'form': form})

def edit_photo(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    form = PhotoForm(instance=photo)
    
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid:
            form.save()
            messages.success(request, 'Imagem editada com sucesso!')   
            return redirect('photo', photo_id)
    
    return render(request, 'galery/edit_photo.html', {'form': form, 'photo_id': photo_id})

def delete_photo(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    deleted_photo_title = photo.title
    photo.delete()
    messages.success(request, f'A deleção da foto {deleted_photo_title} foi realizada com sucesso!')
    return redirect('home')

def return_photos_search(request):
    photos = Photo.objects.all()
    
    if "search" in request.GET:
        name_to_search = request.GET['search']
        if name_to_search:
            photos = photos.filter(title__icontains=name_to_search)
        
    return photos

def return_photos_tag_filter(request, tag_id):
    photos = Photo.objects.order_by('created_at').filter(category_id=tag_id, published=True)
    return render(request, 'galery/index.html', {"tags": return_categories(), "cards":photos})
    
def return_photos():
    return Photo.objects.order_by("created_at").filter(published=True)    

def return_photo(photo_id):
    return get_object_or_404(Photo, pk=photo_id)  

def return_categories():
    return Category.objects.filter(active=True)