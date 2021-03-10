from django import forms
from .models import Month


class StoicForm(forms.Form):
    title = forms.CharField(max_length=150)
    content = forms.CharField()
    is_published = forms.BooleanField()
    month = forms.ModelChoiceField(queryset=Month.objects.all())
