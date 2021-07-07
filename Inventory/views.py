from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("this is working")

def list(response, id):
    return HttpResponse("<h1>%s</h1>" % id)