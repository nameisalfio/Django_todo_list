from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now=False, auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
