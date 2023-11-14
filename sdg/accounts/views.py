from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login

from .forms import RegisterForm
from .models import CustomUser

# Create your views here.
def home(request):
    return HttpResponse('Hi')


def login(request):
    if request.method == "GET":
        return HttpResponse("Login")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/")
        else:
            return HttpResponse("Invalid")
    else:
        return HttpResponse("Failed attempt")


def logout_view(request):
    logout(request)
    return redirect("login")


def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'registration/signup.html', {"form":form})
