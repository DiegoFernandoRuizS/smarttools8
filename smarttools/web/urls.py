from django.conf.urls import url

from .views import IndexView,RegisterView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^register/', RegisterView.as_view(), name='register'),
]
