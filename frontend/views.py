from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def show_activities(request):
    return render(request, "show_activities.html")