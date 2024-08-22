from django.shortcuts import render

# Create your views here.


def home(request):
    return render (request, "index.html")

def te(request):
    peoples=[
        {'name': 'Asik' , 'age':16},
        {'name': 'Rafi' , 'age':16},
        {'name': 'alal' , 'age':16},
    ]
    return render (request, "table.html", context={'people':'peoples'})