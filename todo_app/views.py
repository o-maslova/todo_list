from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView
from .models import Task


class TaskCreate(CreateView):
    model = Task
    fields = ['task_name']


class TaskList(ListView):
    model = Task



