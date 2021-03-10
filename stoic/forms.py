from django import forms
from .models import Month


class StoicForm(forms.Form):
    title = forms.CharField(max_length=150, label='Заголовок', widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5
    }))
    is_published = forms.BooleanField(label='Опубликовать?', initial=True)
    month = forms.ModelChoiceField(empty_label='Выберите месяц', label='Месяц',
                                      queryset=Month.objects.all(),
                                      widget=forms.Select(attrs={"class": "form-control"}))
