from django import forms
from apps.galery.models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['published', 'created_at', 'user', 'card_tag']
        labels = {
            'title': 'Título: ',
            'subtitle': 'Legenda: ',
            'description': 'Descrição: ',
            'category': 'Categoria: ',
            'image': 'Imagem'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
        }