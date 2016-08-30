from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from .forms import RegisterForm

class RegisterUser(CreateView):
    model = User
    template_name = "usuario/register.html"
    form_class = RegisterForm #UserCreationForm
    success_url = reverse_lazy('web_index')


"""
def login_request(request):
   if request.method == 'POST':
       email = request.POST['email']
       password = request.POST['password']

       user = authenticate(email=email, password=password)
       if user is not None and user.is_active:
           login(request, user)
           return reverse_lazy('web_index')
"""


