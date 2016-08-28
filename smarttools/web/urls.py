from django.conf.urls import url

from .views import IndexView, RegisterView, HomeView, CompetitionView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^home/', HomeView.as_view(), name='home'),
    url(r'^competition/', CompetitionView.as_view(), name='competition'),
]
