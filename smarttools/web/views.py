from django.contrib.gis.db.models import fields
from django.shortcuts import render
from django.http import HttpResponse
from itertools import chain
from django.views.generic import ListView, TemplateView
from .models import Usuario, User, Video, Competition


class WebIndexView(ListView):
    model = User
    template_name = 'web/index.html'


class RegisterView(ListView):
    model = Usuario
    template_name = 'register.html'


class HomeView(ListView):
    model = User
    template_name = 'home.html'
    context_object_name = 'company'

    def get_queryset(self, **kwargs):
        company = self.kwargs['company_name']
        try:
            queryset = User.objects.filter(username__exact=company).get()
        except User.DoesNotExist:
            queryset = None
        return queryset

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        company = self.kwargs['company_name']
        queryset2 = Competition.objects.filter(user__username__exact=company)

        context['competitions'] = queryset2
        return context

class CompetitionView(ListView):
    model = User
    template_name = 'competition.html'
    context_object_name = 'company_competition'

    def get_queryset(self, **kwargs):
        company = self.kwargs['company_name']
        print("--->>>>>>>>>>> "+company)
        try:
            queryset = User.objects.filter(username__exact=company).get()
        except User.DoesNotExist:
            queryset = None
        return queryset

class AddVideoView(ListView):
    model = Video
    template_name = 'addvideo.html'
