from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.
from .models import Task

class TaskAdmin(admin.ModelAdmin):

    list_display = ["__str__", "date"]
    list_filter = ["complete"]
    search_fields = ["title", "description"]

    class Meta:
        model = Task

admin.site.register(Task, TaskAdmin)