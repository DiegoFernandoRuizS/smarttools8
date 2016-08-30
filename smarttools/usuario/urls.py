from django.conf.urls import url
from .views import RegisterUser

urlpatterns = [
    url(r'^usuario/', RegisterUser.as_view(), name='register'),
]
