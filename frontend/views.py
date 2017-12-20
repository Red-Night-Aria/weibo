from django.shortcuts import render

# Create your views here.

def signin(request):
    return render(request, "signin.html")

def signup(request):
    return render(request, "signup.html")

def index(request):
    return render(request, "index.html")
