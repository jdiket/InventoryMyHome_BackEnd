from django.db import models
from django.contrib.auth.models import User


class InventoryList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="inventorylist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    inventory_list = models.ForeignKey(InventoryList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    serial = models.CharField(max_length=200, default=0)
    where_purchased = models.CharField(max_length=200, default='Unknown')
    purchase_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_purchased = models.DateField(default=None)

    def __str__(self):
        return self.name