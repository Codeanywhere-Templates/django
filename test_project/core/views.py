from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to Django!</h1><p>Your Django application is running successfully.</p>")

