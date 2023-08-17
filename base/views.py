from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


class CustomLogin(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/index.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(CreateView):
    model = Task
    template_name = 'base/task_create.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_create.html'
    success_url = reverse_lazy('index')


class TaskDelete(DeleteView):
    model = Task
    template_name = "base/task_delete.html"
    context_object_name = 'task'
    success_url = reverse_lazy('index')