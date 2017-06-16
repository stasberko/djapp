from django.shortcuts import render, HttpResponseRedirect

# Create your views here.


def users(request):
    return render(request, "base.html")

def login(request):
    return render(request, "users/login.html")

def signup(request):
    return render(request, "users/signup.html")