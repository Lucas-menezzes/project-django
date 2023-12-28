from django.shortcuts import render, redirect
from contact.forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def authenticator(request):

    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            print(user)

    context = {
        'form': form,
        'is_login_page': True,
    }

    return render(
        request,
        'contact/authenticator.html',
        {
            'form': form,
        }
    )