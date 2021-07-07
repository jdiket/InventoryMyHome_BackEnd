from django.shortcuts import render
from django.http import HttpResponse
from .models import InventoryList, Item

# Create your views here.

def index(request):
    return render(request, "Inventory/base.html", {})

def lists(request):
    ls = InventoryList.objects.all()
    return render(request, "Inventory/index.html", {"ls": ls})

def detail_list(request, id):
    ls = InventoryList.objects.get(id=id)
    return render(request, "Inventory/list.html", {"list": ls})

def create(request):
