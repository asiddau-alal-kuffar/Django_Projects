from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/VideoChatApp/Login')
    return render(request,'index.html')

def Login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        password = request.POST.get("password")
        user = authenticate(request,username=user, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)    
            return redirect('/VideoChatApp/')
        else:
            return render(request,'login.html')


    return render(request,'login.html')

def LogOut(request):
    logout(request)
    return redirect('/VideoChatApp/Login') 