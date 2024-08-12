from django.urls import path
from apps.galery.views import index, photo, search

urlpatterns = [
    path('', index, name='index'),
    path('photo/<int:photo_id>', photo, name='photo'),
    path('search', search, name='search')
]
