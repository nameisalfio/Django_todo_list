# Generated by Django 5.1 on 2024-08-18 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='task',
            name='position',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
