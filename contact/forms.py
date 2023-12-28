from typing import Any
from django.core.exceptions import ValidationError
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email ja cadastrado')
        
        return email