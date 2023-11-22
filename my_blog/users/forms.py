
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={

        'class': 'input100',
        'placeholder': 'Enter username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={

        'class': 'input100',
        'placeholder': 'Enter password',
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input100',
        'placeholder': 'Enter name',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input100',
        'placeholder': 'Enter surname',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input100',
        'placeholder': 'Enter username',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input100',
        'placeholder': 'Enter email',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={

        'class': 'input100',
        'placeholder': 'Enter password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={

        'class': 'input100',
        'placeholder': 'Сonfirm  password',
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')
