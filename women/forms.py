
from django import forms
from .models import Women, Category, Husband

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Women  # Модель, с которой будет работать форма
        fields = ['title', 'slug', 'content','photo', 'is_publisher', 'cat', 'husband', 'tags']  # Поля, которые будут в форме
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 40}),  # Можем кастомизировать виджет для content
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_publisher'].initial = Women.Stutus.PABLISHED

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Файл')