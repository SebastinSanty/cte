from django import forms
from .models import Profile
from django.contrib.auth.models import User
from registration.forms import RegistrationForm

class LoginForm(forms.Form):
        username = forms.CharField(max_length = 20)
        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'password': forms.PasswordInput(),
        }

class EmailDomainFilterRegistrationForm(RegistrationForm):

    def clean_email(self):
        submitted_data = self.cleaned_data['email']
        ALLOWED_DOMAINS = ['goa.bits-pilani.ac.in']

        if not ALLOWED_DOMAINS: # If we allow any domain
            return submitted_data

        domain = submitted_data.split('@')[1]
        # logger.debug(domain)
        if domain not in ALLOWED_DOMAINS:
            raise forms.ValidationError(
                u'Please register using your BITSmail (...@goa.bits-pilani.ac.in)'
            )
        return submitted_data