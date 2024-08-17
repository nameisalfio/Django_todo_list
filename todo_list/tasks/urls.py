from django.urls import path
from . import views as task_views
from . models import Task
from . views import *

# Task list
# Single task of list

urlpatterns = [
    path('', task_views.TaskListView.as_view(), name='tasks_list'),
    path('welcome/', task_views.welcome, name='welcome'),
    path('about/', task_views.about, name='about'),
    path('create/', task_views.TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/', task_views.TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/update/', task_views.TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', task_views.TaskDeleteView.as_view(), name='task_delete'),
]
