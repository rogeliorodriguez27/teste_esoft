from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from accounts.models import CustomUser


class CreationUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'email', 'password1', 'password2', 'cep', 'address', 'number', 'complement', 'neighborhood', 'city', 'uf' )
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')