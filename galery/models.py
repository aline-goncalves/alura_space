from django.db import models
    
class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
class Photo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.CharField(max_length=100, null=False, blank=False)
    card_tag = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self) -> str:
        return f'Photo [title={self.title}]'