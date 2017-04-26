from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    attributos = {'class': 'form-control'}
    email = forms.CharField(max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre de usuario'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Contraseña'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirmación de la contraseña'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )