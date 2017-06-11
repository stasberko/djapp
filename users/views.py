from django.shortcuts import render, HttpResponse

# Create your views here.


def users(request):
    return render(request, "users/profile.html")


def login(request):
    return render(request, "users/login.html")

def signup(request):
    return render(request, "users/signup.html")