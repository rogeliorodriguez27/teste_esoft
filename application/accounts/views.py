from django.http import HttpResponseRedirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views



from accounts.forms import CreationUserForm, LoginForm



class SignUpView(generic.CreateView):
    form_class = CreationUserForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/signup.html'


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index:index')




def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse_lazy('index:index'))

