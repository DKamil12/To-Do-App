from django.forms import ModelForm
from .models import Task

class TaskModelFrom(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']
