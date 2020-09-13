from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def hello(request):
    return HttpResponse("Hello world ! ")


def login(request):
    return render(request, "login.html")


def editor(request):
    return render(request, "editor.html")