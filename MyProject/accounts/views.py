# accounts/views.py
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views import generic
from .models import BaseRegisterForm


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


class SignUpView(generic.CreateView):
    form_class = BaseRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'