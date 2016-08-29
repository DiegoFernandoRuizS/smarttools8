from django.contrib.gis.db.models import fields
from django.shortcuts import render
from django.http import HttpResponse
from itertools import chain
from django.views.generic import ListView, TemplateView
from .models import Usuario, User, Video, Competition


class IndexView(ListView):
    model = Usuario
    template_name = 'index.html'


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
            queryset = User.objects.filter(username__exact=company)
            queryset2 = Competition.objects.filter(user__username__exact=company)
            result_list = list(chain(queryset, queryset2))
            for x in result_list:
                print("--- > "+str(x))
        except User.DoesNotExist:
            result_list = None
        return result_list

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