from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'your-input-class'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'your-input-class'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'your-input-class'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'your-input-class'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].help_text = None


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'your-input-class'})

    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'your-input-class'})
    )
