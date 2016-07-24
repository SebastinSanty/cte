from django import forms
from .models import Profile
from django.contrib.auth.models import User

class LoginForm(forms.Form):
        username = forms.CharField(max_length = 20)
        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'password': forms.PasswordInput(),
        }