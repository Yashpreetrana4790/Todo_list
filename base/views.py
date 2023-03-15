from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.views.generic.edit	import CreateView,UpdateView,DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class TaskList(LoginRequiredMixin,ListView):
	model = Task 
	context_object_name = 'tasks'

	def get_contect_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tasks']=context['tasks'].filter(user =self.request.user)
		return context


class TaskDetail(LoginRequiredMixin,DetailView):
	model = Task
	context_object_name = 'task'


class TaskCreate(LoginRequiredMixin,CreateView):
	model = Task
	fields = '__all__'
	success_url = reverse_lazy('tasks')


class TaskUpdate(LoginRequiredMixin,UpdateView):
	model = Task
	fields = '__all__'
	success_url = reverse_lazy('tasks')


class DeleteView(LoginRequiredMixin,DeleteView):
	model = Task
	context_object_name = 'tasks'
	success_url = reverse_lazy('tasks')


class CustomLoginView(LoginView):
	template_name = 'base/login.html'
	fields = '__all__'
	redirect_authenticated_user =True

	def get_success_url(self):
		return reverse_lazy('tasks')

class RegisterPage(FormView):
	template_name = 'base/register.html'
	form_class = UserCreationForm
	redirect_authenticated_user = True		
	success_url = reverse_lazy('tasks')







