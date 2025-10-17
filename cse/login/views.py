from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import  login
from .forms import Sign_UpForm, LoginForm
# Create your views here.

def sign_up_view(request):
    if request.method == "POST":
        form = Sign_UpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully — Login")
            return redirect('sign_up')
    else:
        form = Sign_UpForm()
    return render(request, 'sign_up.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
