from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import WebIndexView

urlpatterns = [
    url(r'^web$', login_required(WebIndexView.as_view()), name='web_index'),
]
