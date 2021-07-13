from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import InventoryList, Item
from .forms import CreateNewList

# Create your views here.

def index(request):
    return render(request, "Inventory/base.html", {})

def lists(request):
    # ls = InventoryList.objects.all()
    return render(request, "Inventory/index.html", {})

def detail_list(response, id):
    ls = InventoryList.objects.get(id=id)

    if ls in response.user.inventorylist.all():

        if response.method == "POST":
            _name = response.POST.get("name")
            _serial = response.POST.get("serial")
            _where_purchased = response.POST.get("where_purchased")
            _purchase_amount = response.POST.get("purchase_amount")
            _date_purchased = response.POST.get("date_purchased")
            ls.item_set.create(
                name=_name, 
                serial=_serial, 
                where_purchased=_where_purchased, 
                purchase_amount=_purchase_amount, 
                date_purchased=_date_purchased
            )

        # The following is not functional, but is hopefully how a delete method would work
        # if response.method == "DELETE":
        #     get the item.id
        #     Item.objects.get(pk=id).delete()

        return render(response, "Inventory/list.html", {"list": ls})


    return render(response, "Inventory/base.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = InventoryList(name=n)
            t.save()
            response.user.inventorylist.add(t)
        return HttpResponseRedirect('lists/%i' %t.id)

    else:
        form = CreateNewList()

    return render(response, "Inventory/create.html", {"form": form})