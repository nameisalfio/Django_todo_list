from django.shortcuts import render, redirect
from datetime import datetime
from django.urls import reverse_lazy
from .models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def welcome(request):
    return render(request, 'welcome.html', {'current_year': datetime.now().year})

def about(request):
    return render(request, 'about.html', {'current_year': datetime.now().year})

class TaskListView(ListView):
    model = Task
    template_name = "tasks_list.html"
    context_object_name = 'tasks'
    ordering = ['-date']

class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = Task
    template_name = "task_form.html"
    fields = ['title', 'description', 'complete']

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('tasks_list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = "task_form.html"
    fields = ['title', 'description', 'complete']

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy('tasks_list')
