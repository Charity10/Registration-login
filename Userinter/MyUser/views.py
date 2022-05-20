from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def homePage(request):

    context = {}

    return render(request, 'MyUser/home.html', context)



def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created for successfully')
            return redirect('login')
    
    context = {'form':form}
    
    return render(request, 'MyUser/register.html', context)
        


def loginPage(request):
    
    if request.method == 'POST':
        form = CreateUserForm()
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if form.is_valid():
            login(request, user)
            return redirect('home')
        
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}

    return render(request,'MyUser/login.html', context)

