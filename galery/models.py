from django.db import models
from datetime import datetime
    
class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name
    
class Photo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='photos', blank=True)
    card_tag = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, null=False)
    
    def __str__(self) -> str:
        return self.title