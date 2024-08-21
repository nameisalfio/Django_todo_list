from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from .models import Task

# Funzioni semplici per pagine statiche
def welcome(request):
    return render(request, 'welcome.html')

def about(request):
    return render(request, 'about.html')

# Funzione per alternare lo stato di completamento di una task
def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.complete = not task.complete
    task.save()
    return redirect('tasks_list')

# Vista per aggiornare la posizione delle task tramite AJAX
@csrf_exempt
def update_task_position(request):
    if request.method == 'POST':
        task_ids = request.POST.getlist('task_ids[]')
        for index, task_id in enumerate(task_ids):
            Task.objects.filter(id=task_id).update(position=index + 1)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)

# Vista per visualizzare la lista delle task
class TaskListView(ListView):
    model = Task
    template_name = "tasks_list.html"
    context_object_name = 'tasks'

# Vista per visualizzare i dettagli di una task
class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = 'task'

# Vista per creare una nuova task
class TaskCreateView(CreateView):
    model = Task
    template_name = "task_form.html"
    fields = ['title', 'description', 'complete']

    def form_valid(self, form):
        # Assegna la posizione alla nuova task
        response = super().form_valid(form)
        last_position = Task.objects.aggregate(models.Max('position'))['position__max']
        self.object.position = (last_position or 0) + 1
        self.object.save()
        return redirect('tasks_list')

# Vista per aggiornare una task
class TaskUpdateView(UpdateView):
    model = Task
    template_name = "task_form.html"
    fields = ['title', 'description', 'complete']

# Vista per eliminare una task
class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy('tasks_list')
