from django.http import HttpResponse
from django.shortcuts import render
from app1.models import Students
import datetime


def home(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

def Education(request):
    return render(request,'Education.html')

def Register(request):
    if request.method == "POST":
        StudentID=  request.POST.get("id")
        StudentRoll= request.POST.get("roll")
        Class= request.POST.get("class")
        Shift= request.POST.get("shift")
        StudentsName= request.POST.get("sname")
        FatherName= request.POST.get("fname")
        MotherName= request.POST.get("mname")
        Mobile = request.POST.get("mobile")
        Gender= request.POST.get("gender")
        Email= request.POST.get("email")
        Address = request.POST.get("address")
        
        Register_Students0 = Students(StudentID=StudentID , StudentRoll=StudentRoll , Class=Class , Shift=Shift, StudentsName=StudentsName, FatherName=FatherName, MotherName=MotherName, Mobile=Mobile, Gender=Gender, Email=Email, Address=Address)
        Register_Students0.save()

    return render(request,'Register.html')

def Login(request):
    return render(request,'Login.html')

def StudentIdCards(request):
    return render(request,'StudentIdCards.html')