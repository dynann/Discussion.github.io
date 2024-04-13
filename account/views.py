from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .form import UserCreation

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreation
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    context_object_name = 'signup'