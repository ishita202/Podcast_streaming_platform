from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','email', 'password1', 'password2']

class LoginForm(forms.Form):
    username_or_email = forms.CharField(label="Email or Username")
    password = forms.CharField(widget=forms.PasswordInput)
