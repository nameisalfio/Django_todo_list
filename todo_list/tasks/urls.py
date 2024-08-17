from django.urls import path
from django.views.generic import ListView, DetailView
from . import views as task_views
from . models import Task

# Task list
# Single task of list

urlpatterns = [
    path('', ListView.as_view(
        queryset=Task.objects.all().order_by("-date"),
        template_name="tasks_list.html"
    ), name="list"),
]