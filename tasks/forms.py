from django.forms import ModelForm
from .models import Task
from django import forms

class TaskModelFrom(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']


class TitleFilterForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        label='Search task by title'
    )