from django.urls import path
from . import views as task_views

# Task list
# Single task of list

urlpatterns = [
    path('', task_views.TaskListView.as_view(), name='tasks_list'),
    path('about/', task_views.about, name='about'),
    path('create/', task_views.TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/', task_views.TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/update/', task_views.TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', task_views.TaskDeleteView.as_view(), name='task_delete'),
    path('toggle-task-status/<int:task_id>/', task_views.toggle_task_status, name='toggle_task_status'),
    path('update-task-position/', task_views.update_task_position, name='update_task_position'),
]

