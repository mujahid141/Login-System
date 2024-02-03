# myapp/views.py
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render('home.html')  # Redirect to your desired URL after successful signup
    else:
        form = SignUpForm()

    return render(request, 'home.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # Log in the user or perform other necessary actions
            return HttpResponse('home.html')  # Redirect to your desired URL after successful login
    else:
        form = AuthenticationForm()

    return render(request, 'home.html', {'form': form})

def home(request):
    return render(request, 'home.html')
