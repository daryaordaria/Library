from django import forms
from .models import Search
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SearchForm(forms.ModelForm):
    name_book = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control me-2", 'placeholder': 'Enter name of book'
    }))
    class Meta:
        model = Search
        fields = ['name_book',]
    
class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={
        'class' : 'form-control', 'placeholder': 'Enter Username'
    }))

    email = forms.CharField(max_length = 150, widget = forms.EmailInput(attrs={
        'class' : 'form-control', 'placeholder': 'Enter email '
    }))

    password1 = forms.CharField(max_length = 50, widget = forms.PasswordInput(attrs={
        'class' : 'form-control', 'placeholder': 'At least 8 characters'
    }))
    password2 = forms.CharField(max_length = 50, widget = forms.PasswordInput(attrs={
        'class' : 'form-control', 'placeholder': 'Confirm Password'
    }))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']