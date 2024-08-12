from django.urls import path
from apps.galery.views import home, photo, search, return_photos_tag_filter, new_photo, edit_photo, delete_photo

urlpatterns = [
    path('', home, name='home'),
    path('photo/<int:photo_id>', photo, name='photo'),
    path('search', search, name='search'),
    path('category-filter/<int:tag_id>', return_photos_tag_filter, name='category_filter'),
    path('new-photo', new_photo, name='new_photo'),
    path('edit-photo/<int:photo_id>', edit_photo, name='edit_photo'),
    path('delete-photo/<int:photo_id>', delete_photo, name='delete_photo')
]
