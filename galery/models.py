from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.CharField(max_length=100, null=False, blank=False)
    card_tag = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f'Photo [name={self.title}]'