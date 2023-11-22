
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
        fields = ('usermae', 'password')


# class UserRegistretionForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('usermae', 'password')
