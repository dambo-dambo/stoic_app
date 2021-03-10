from django import forms
from .models import Stoic
import re
from django.core.exceptions import ValidationError

class StoicForm(forms.ModelForm):
    class Meta:
        model = Stoic
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'month']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'month': forms.Select(attrs={'class': 'form-control'}),
        }
#очищаем данные
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title