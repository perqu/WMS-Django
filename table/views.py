from django.shortcuts import render


def home(request):
    return render(request, "base.html")


def room(request):
    return render(request, "room.html")
