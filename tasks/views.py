from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from .filters import TaskFilter
from .forms import TitleFilterForm


class TaskListView(ListView):
    model = Task

    def get_queryset(self):
        qs = super().get_queryset()
        # self.filterset = TaskFilter(request=self.request.GET, queryset=qs)
        # return self.filterset.qs

        searched_title = self.request.GET.get('title')
        if searched_title:
            qs = qs.filter(title__contains=searched_title)
        return qs
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        # context['search_form'] = self.filterset.form
        context['search_form'] = TitleFilterForm()
        return context


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