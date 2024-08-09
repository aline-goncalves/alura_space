from django.shortcuts import render
from user.forms import LoginForm, RegisterForm

def login(request):
    return render(request, 'user/login.html', {"form": LoginForm()})

def register(request):
    return render(request, 'user/register.html', {"form": RegisterForm()})

def logout(request):
    return render(request, 'user/register.html')