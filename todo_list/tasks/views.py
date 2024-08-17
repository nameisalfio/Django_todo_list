from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView

# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def about(request):
    return render(request, 'about.html')

# Classes for views

class TaskListView(ListView):
    model = Task
    template_name = "tasks_list.html"
    context_object_name = 'tasks'
    ordering = ['-date']  # Order by date descending

class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = 'task'
