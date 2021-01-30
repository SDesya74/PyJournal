from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.forms import CreateUserForm


def index(request):
    context = {
        "values": ["Test 1", "Test 2"]
    }
    return render(request, "main/index.html", context)


def loginPage(request):
    return render(request, "main/login.html")


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = CreateUserForm()

    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            authenticate(request, username=username, password=password)
            return redirect('home')

    context = {
        "form": form
    }
    return render(request, "main/register.html", context)
