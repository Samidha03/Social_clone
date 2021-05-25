from django.shortcuts import render 
from django.urls import reverse_lazy    #reverse_lazy is used when some one is login/logout where does he should go.
from django.views.generic import CreateView
from . import forms


# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')      #Once u login after successful login i ll reverse to login
    template_name = 'accounts/signup.html'
