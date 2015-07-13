from django import forms
from django.utils.translation import ugettext as _

class LoginForm(forms.Form):
    username = forms.CharField(label=_('Adres email'))
    password = forms.CharField(widget=forms.PasswordInput,
        label=_('Hasło'))
