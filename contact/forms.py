from typing import Any
from django.core.exceptions import ValidationError
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import password_validation


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget= forms.FileInput(
            attrs={
                "accept":  'image/*',
            }
        )
    )
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone', 'description', 'email', 'category', 'picture')
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if any(char.isdigit() for char in first_name):
            self.add_error(
                'first_name',
                ValidationError('Somente Letras',
                    code= 'invalid'
                )
            )
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if any(char.isdigit() for char in last_name):
            self.add_error(
                'last_name',
                ValidationError('Somente Letras',
                    code= 'invalid'
                )
            )
        return last_name
    
    def clean_phone(self):
        phone_number = self.cleaned_data.get('phone')

        if any(char.isalpha() for char in phone_number):
            self.add_error(
                'phone',
                ValidationError('Somente Numeros',
                    code= 'invalid'
                )
            )
        return phone_number
            
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Email ja cadastrado')
        
        return email
    
class LoginForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ('username', 'password')

class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required'
    )
    
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required'
    )
    password1 = forms.CharField(
        label='Password 1',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
    password2 = forms.CharField(
        label='Password 2',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        )