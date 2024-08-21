import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max
from .models import Task

def about(request):
    return render(request, 'about.html')

@csrf_exempt
def toggle_task_status(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.complete = not task.complete
        task.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)

@csrf_exempt
def update_task_position(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task_ids = data.get('task_ids', [])

        if isinstance(task_ids, list):
            for index, task_id in enumerate(task_ids):
                Task.objects.filter(id=task_id).update(position=index + 1)
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)

def task_list(request):
    search_query = request.GET.get('search', '')  # Get search query from URL parameters
    tasks = Task.objects.filter(title__icontains=search_query).order_by('-date')  # Filter tasks based on search query
    return render(request, 'tasks_list.html', {'tasks': tasks})

class TaskListView(ListView):
    model = Task
    template_name = "tasks_list.html"
    context_object_name = 'tasks'
    ordering = ['position']

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')  # Get search query from URL parameters
        queryset = super().get_queryset()
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)  # Filter tasks based on search query
        return queryset

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
        # Set the position of the new task
        last_position = Task.objects.aggregate(Max('position'))['position__max']
        self.object.position = (last_position or 0) + 1
        self.object.save()
        return redirect('tasks_list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = "task_form.html"
    fields = ['title', 'description', 'complete']

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy('tasks_list')
