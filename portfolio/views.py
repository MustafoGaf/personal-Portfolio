from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

def home(req):
    projects = Project.objects.all()
    return render(req, 'portfolio/home.html', {"project": projects})

def signupuser(req):
    if req.method == "GET":
        return render(req, 'portfolio/signupuser.html', {'form': UserCreationForm()})
    else:
        if req.POST['password1'] ==req.POST['password2']:
            try:
                user = User.objects.create_user(req.POST['username'], password = req.POST["password1"])
                user.save()
                login(req, user)
                return redirect('/', {'username':req.POST["username"]})
            except IntegrityError :
                return render(req, 'portfolio/signupuser.html', {'form': UserCreationForm(), "error":"Пользователь с этим именам уже существуеть"})

        else:
            return render(req, 'portfolio/signupuser.html', {'form': UserCreationForm(), "error":"Не совподают паролы"})


def logoutuser(req):
    if req.method == "POST":
        logout(req)
        return redirect('/')


def loginuser(req):
    if req.method == "GET":
         return render(req, 'portfolio/signupuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(req, username=req.POST['username'], password = req.POST['password'])
        if user is None:
            return render(req, 'portfolio/signupuser.html', {'form': AuthenticationForm(), "error":"Не правильно имя пользовател или"})
        else:
            login(req, user)
            return redirect('/')