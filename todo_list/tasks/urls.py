from django.urls import path
from . import views as task_views
from . models import Task
from . views import TaskListView, TaskDetailView

# Task list
# Single task of list

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('about/', task_views.about, name='about'),
]