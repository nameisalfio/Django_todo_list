from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from .models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View

def welcome(request):
    return render(request, 'welcome.html', {'current_year': datetime.now().year})

def about(request):
    return render(request, 'about.html', {'current_year': datetime.now().year})

def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.complete = not task.complete
    task.save()
    return redirect('tasks_list')  # Assumi che 'tasks_list' sia il nome della tua vista per la lista dei task

@csrf_exempt
def update_task_position(request):
    if request.method == 'POST':
        task_ids = request.POST.getlist('task_ids[]')
        for index, task_id in enumerate(task_ids):
            Task.objects.filter(id=task_id).update(position=index)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)

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
        # Set the position of the new task
        self.object.position = Task.objects.count() + 1
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

class UpdateTaskPositionView(View):
    def post(self, request):
        task_ids = request.POST.getlist('task_ids[]')
        for index, task_id in enumerate(task_ids):
            Task.objects.filter(id=task_id).update(position=index + 1)
        return JsonResponse({'status': 'success'})