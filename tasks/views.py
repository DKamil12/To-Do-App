from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task


class TaskListView(ListView):
    model = Task


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(CreateView):
    model= Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')


class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    
    def get_success_url(self) -> str:
        return reverse_lazy('task-detail', kwargs={'pk': self.object.pk})
    

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')