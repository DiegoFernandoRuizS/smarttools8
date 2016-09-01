import subprocess
import logging
from django.views.generic import ListView, TemplateView
from .models import Usuario, User, Video, Competition, VideoForm
from django import forms
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import datetime


class WebIndexView(ListView):
    model = Usuario
    template_name = 'web/index.html'


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

    # convert_video.delay(2)


"""    def get_queryset(self, **kwargs):
        company = self.kwargs['company_name']
        print("--->>>>>>>>>>> " + company)
        try:
            queryset = User.objects.filter(username__exact=company).get()
        except User.DoesNotExist:
            queryset = None
        return queryset
"""


class AddVideoView(ListView):
    model = Video
    template_name = 'addvideo.html'

def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)

        if form.is_valid():
            new_video = Video(name=request.POST.get('name'),
                              state='En proceso',
                              user_email=request.POST.get('user_email'),
                              message=request.POST.get('message'),
                              original_video=request.FILES['original_video'],
                              uploadDate=datetime.datetime.now(),
                              competition=Competition.objects.filter(id=1).get()
                              )
            new_video.save()
        return HttpResponseRedirect(reverse('competition'))
    else:
        form = VideoForm()
    return render(request, 'addvideo.html', {'form': form})
