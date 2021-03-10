from django import forms
from .models import Stoic


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