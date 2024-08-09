from django.contrib import admin
from galery.models import Photo, Category

class PhotosList(admin.ModelAdmin):
    list_display = ("id", "title", "subtitle", "card_tag", "image", "category")
    list_display_links = ("id", "title", "subtitle", "card_tag", "image", "category")
    search_fields = ("title", "subtitle", "description", "card_tag")
    list_filter = ("category",)
    list_per_page = 1

class CategoriesList(admin.ModelAdmin):
    list_display = ("id", "name", "description", "active")
    list_display_links = ("id", "name", "description", "active")
    search_fields = ("id", "name", "description")
    list_filter = ("active",)

admin.site.register(Photo, PhotosList)
admin.site.register(Category, CategoriesList)