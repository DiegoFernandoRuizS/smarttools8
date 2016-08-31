import subprocess
import logging
from django.views.generic import ListView, TemplateView
from .models import Usuario, User, Video, Competition


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

    def get_queryset(self, **kwargs):
        company = self.kwargs['company_name']
        print("--->>>>>>>>>>> " + company)
        try:
            queryset = User.objects.filter(username__exact=company).get()
        except User.DoesNotExist:
            queryset = None
        return queryset


class AddVideoView(ListView):
    model = Video
    template_name = 'addvideo.html'
    print("Llego a video add....")

    video = Video.objects.filter(id=1).get()
    pathConverted = 'C:\\Users\\diego\\Documents\\GitHub\\convertido.mp4'

    cmd = ['ffmpeg', '-i ', video.original_video.path, ' -b 1500k -vcodec libx264 -g 30', pathConverted]
    print('Ejecutando... ', ' '.join(cmd))
    proc = subprocess.Popen(cmd)
    proc.subprocess.wait()

    print("Esta convertido? " + video.converted)

    if proc.returncode != 0:
        print('Falló algo en command failed with ret val %s', proc.returncode)
        print(proc.stderr)
        print(proc.stdout)
    else:
        video.converted = True
        video.save()
        print.info('Video convertido ok')
