from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def index2(request):
    return render(request, "about.html")
