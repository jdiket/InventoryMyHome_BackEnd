from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import InventoryList, Item
from .forms import CreateNewList

# Create your views here.

def index(request):
    return render(request, "Inventory/base.html", {})

def lists(request):
    ls = InventoryList.objects.all()
    return render(request, "Inventory/index.html", {"ls": ls})

def detail_list(response, id):
    ls = InventoryList.objects.get(id=id)

    if response.method == "POST":
        _name = response.POST.get("name")
        _serial = response.POST.get("serial")
        _location = response.POST.get("location")
        ls.item_set.create(name=_name, serial=_serial, location=_location)

    return render(response, "Inventory/list.html", {"list": ls})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = InventoryList(name=n)
            t.save()

        return HttpResponseRedirect('lists/%i' %t.id)
    else:
        form = CreateNewList()

    
    return render(response, "Inventory/create.html", {"form": form})
