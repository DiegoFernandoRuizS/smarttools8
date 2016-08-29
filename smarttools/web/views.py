from django.views.generic import ListView
from .models import User


class WebIndexView(ListView):
    model = User
    template_name = 'web/index.html'
