from django.contrib.gis.db.models import fields
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from .models import Usuario, User


class IndexView(ListView):
    model = Usuario
    template_name = 'index.html'


class RegisterView(ListView):
    model = Usuario
    template_name = 'register.html'


class HomeView(ListView):
    model = User
    template_name = 'homecompetitions.html'
    context_object_name = 'company'

    def get_queryset(self, **kwargs):
        company = self.kwargs['company_name']
        try:
            queryset = User.objects.filter(username__exact=company).get()
        except User.DoesNotExist:
            queryset = None
        return queryset


class CompetitionView(ListView):
    model = User
    template_name = 'homecompetition.html'
    context_object_name = 'company_competition'

    def get_queryset(self, **kwargs):
        company = self.kwargs['company_name']
        print("--->>>>>>>>>>> "+company)
        try:
            queryset = User.objects.filter(username__exact=company).get()
        except User.DoesNotExist:
            queryset = None
        return queryset

