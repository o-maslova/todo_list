from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=140)
