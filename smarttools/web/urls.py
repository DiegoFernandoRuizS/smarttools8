from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import WebIndexView, RegisterView, HomeView, CompetitionView, AddVideoView

urlpatterns = [
    url(r'^web$', login_required(WebIndexView.as_view()), name='web_index'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^home/(?P<company_name>\w+)', HomeView.as_view(), name='home'),
    url(r'^competition/(?P<company_name>\w+)', CompetitionView.as_view(), name='competition'),
    url(r'^video/add', AddVideoView.as_view(), name='addvideo'),
]
