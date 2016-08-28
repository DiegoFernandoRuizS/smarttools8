from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from .models import Usuario, User

class IndexView (ListView):
    model = Usuario
    template_name = 'index.html'

class RegisterView (ListView):
    model = Usuario
    template_name = 'register.html'

class HomeView (ListView):
    model = User
    template_name = 'homecompetitions.html'
    context_object_name = 'company'

    def get_queryset(self, **kwargs):
        company = self.kwargs['company_name']
        print("---> "+company)
        queryset = User.objects.filter(username__exact= company)
        return queryset

class CompetitionView (ListView):
    model = Usuario
    template_name = 'homecompetition.html'