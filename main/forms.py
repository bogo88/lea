from ibus.keysyms import value
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RateForm(forms.Form):
    value = forms.IntegerField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}),
                               label="")
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password'}),
                               label="")


class RegisterForm(UserCreationForm):
    username = forms.RegexField(max_length=30,
                                regex=r'^[\w.@+-]+$',
                                help_text="Required. 30 characters or fewer. Letters, digits and "
                                "@/./+/-/_ only.",
                                error_messages={
                                'invalid': "This value may contain only letters, numbers and "
                                "@/./+/-/_ characters."},
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                                help_text="Enter the same password as above, for verification.")
