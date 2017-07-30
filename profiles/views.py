from django.shortcuts import render, redirect
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout
)
from .forms import RegisterForm, LoginForm
from django.contrib import messages


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            messages.info(
                request,
                'Kayıt başarılı. Şimdi login olabilirsiniz.'
            )

            return redirect('login')

    return render(request, './profiles/register.html', {
        'form': form,
    })


def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            auth_login(request, form.user)
            messages.info(
                request,
                'Giriş yaptınız.'
            )
            return redirect('home')

    return render(request, './profiles/login.html', {
        'form': form
    })

def logout(request):
    auth_logout(request)
    return redirect('/')