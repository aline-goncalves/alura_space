from django.shortcuts import render, redirect
from apps.user.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            return doLogin(request, form)
        
    return render(request, 'user/login.html', {"form": LoginForm()})

def doLogin(request, form):
    username = form["username"].value()
    password = form["password"].value()    
    user = auth.authenticate(request, username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        messages.success(request, f'{username} logado com sucesso!')
        return redirect('home')
    else:
        messages.error(request, 'Erro ao tentar realizar o login. Confira os dados informados!')
        return redirectLoginForm()

def register(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            return registerUser(request, form)                            
    
    return render(request, 'user/register.html', {"form": RegisterForm()})

def verifyIfpasswordsMatch(form):
    password = form["password"].value()
    confirm_password = form["confirm_password"].value()
    
    return password == confirm_password

def registerUser(request, form):
    if verifyIfUserExists(form):
        messages.error(request, 'Usuário já existe! Realize o login')
        return redirectLoginForm()
    
    if verifyIfpasswordsMatch(form):
        createUser(request, form) 
        return redirectLoginForm() 
    else:
        messages.error(request, 'As senhas digitadas não são iguais!')
    
    return redirectRegisterForm()

def createUser(request, form):
    username = form["username"].value()
    email = form["email"].value()
    password = form["password"].value()
        
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()   
    messages.success(request, f'Usuário {username} cadastrado com sucesso!')

def verifyIfUserExists(form):
    username = form["username"].value()     
    return User.objects.filter(username=username).exists()

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirectLoginForm()

def redirectLoginForm():
    return redirect('login') 
    
def redirectRegisterForm():
    return redirect('register')
