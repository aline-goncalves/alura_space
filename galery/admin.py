from django.contrib import admin
from galery.models import Photo, Category

class PhotosList(admin.ModelAdmin):
    list_display = ("id", "title", "subtitle", "card_tag", "image", "category", "published")
    list_display_links = ("id", "title", "subtitle", "card_tag", "image", "category")
    search_fields = ("title", "subtitle", "description", "card_tag")
    list_filter = ("category","published")
    list_editable = ("published",)
    list_per_page = 1

class CategoriesList(admin.ModelAdmin):
    list_display = ("id", "name", "description", "active")
    list_display_links = ("id", "name", "description")
    search_fields = ("id", "name", "description")
    list_filter = ("active",)
    list_editable = ("active",)

admin.site.register(Photo, PhotosList)
admin.site.register(Category, CategoriesList)