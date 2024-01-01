from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import logout 

def register(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registro com sucesso!!")
            return redirect('contact:index')
        messages.error(request," Erro no cadastro ")

    context = {
        'form': form,
        'is_login_page': False,
    }

    return render(
        request,
        'contact/register.html',
        context
    )

def authenticator(request):
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucess')
            return redirect('contact:index')
        messages.error(request, 'login invalid')

    context = {
        'form': form,
        'is_login_page': True,
    }

    return render(
        request,
        'contact/authenticator.html',
        context
    )

def logout_view(request):
    logout(request)
    return redirect('contact:authenticator')

def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request, 'contact/register.html',
            {
                'form': form
            }
        )
    form = RegisterUpdateForm(data=request.POST ,instance=request.user)

    if not form.is_valid():
        return render(
            request, 'contact/register.html',
            {
                'form': form
            }
        )
    form.save()
    messages.success(request, 'perfil atualizado com sucesso')
    return render(           
        request, 'contact/register.html',
            {
                'form': form
            }
        )