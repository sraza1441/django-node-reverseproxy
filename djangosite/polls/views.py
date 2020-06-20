from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Shahid!\nHope you are doing good!")
