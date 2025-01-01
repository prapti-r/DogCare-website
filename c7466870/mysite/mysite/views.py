from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Welcome to Django views about us method")
    return render(request, "home.html")