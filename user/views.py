from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from user.forms import RegisterForm


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Hush kelibsiz {username}")
            return redirect('app:home')
        else:
            messages.error(request, 'Username yoki Password Xato ?')
    return render(request, 'user/login.html')


def logout_view(request):
    logout(request)
    return redirect('user:login_view')


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'complete')
            return redirect('user:login_view')
        else:
            messages.error(request, 'Error')
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)

