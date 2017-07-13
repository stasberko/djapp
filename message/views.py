from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import Message
from django.contrib.auth.decorators import login_required


@login_required()
def chat(request):
    return render(request, "messages/chat.html")

@login_required()
def receive_message(request):
    if request.method == 'POST' and request.POST["mess"]:
            Message.objects.create(
                auth=request.user,
                mess = request.POST['mess'],)

            return HttpResponse("ok")
    return HttpResponse("error")

def mess_liad(request):
    obj = Message.objects.all().order_by("-dtime")[:10]
    return render_to_response("messages/chatresp.html", {'obj': obj})