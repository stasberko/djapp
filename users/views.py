from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.contrib import auth

from django_redis import get_redis_connection
rcon = get_redis_connection()

# Create your views here.
from django.core.cache import cache
from django.contrib.auth.hashers import check_password, make_password


def users(request):
    return render(request, "base.html")

def login(request):
    return render(request, "users/login.html")

def signup(request):
    return render(request, "users/signup.html")



def mlogin(request):
    if request.method == "GET":
        return render(request, "users/mlogin.html")
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(email = email, password = password)
        if user:
            request.session['member_id'] = user.id
            cache.set("member_id", user.id, nx=True)
            rcon.set("member_id", user.id)
            return HttpResponseRedirect(reverse('main'))
        else:
            return HttpResponseRedirect(reverse('mlogin'))

def mlogout(request):
    del request.session['member_id']
    return HttpResponseRedirect(reverse('main'))
