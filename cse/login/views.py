from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import  login, authenticate
from .forms import SignUpForm
# Create your views here.

def sign_up_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully — Login")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful! Welcome back.")
            return redirect('dashboard')  # or your homepage

    return render(request, 'login.html')
