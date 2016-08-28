from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from .models import Usuario

class IndexView (ListView):
    model = Usuario
    template_name = 'index.html'

class RegisterView (ListView):
    model = Usuario
    template_name = 'register.html'

class HomeView (ListView):
    model = Usuario
    template_name = 'homecompetitions.html'

class CompetitionView (ListView):
    model = Usuario
    template_name = 'homecompetition.html'