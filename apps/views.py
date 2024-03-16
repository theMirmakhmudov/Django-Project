from django.shortcuts import render
from apps.models import Person


def index(request):
    return render(request, "home.html")


def index2(request):
    return render(request, "about.html")


def index3(request):
    data = {}
    data["dataset"] = Person.objects.all()
    return render(request, 'index.html', data)
