from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from main.forms import CreateUserForm


def index(request):
    context = {
        "values": ["Test 1", "Test 2"],
        "username": request.user.username
    }
    return render(request, "main/index.html", context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Username OR password is incorrect')

    return render(request, "main/login.html")


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    context = {
        "form": form
    }
    return render(request, "main/register.html", context)
