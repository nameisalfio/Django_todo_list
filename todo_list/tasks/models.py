from django.db import models
from django.urls import reverse

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now=False, auto_now_add=True)
    complete = models.BooleanField(default=False)
    position = models.PositiveIntegerField(default=0)  # Add this field

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['position']