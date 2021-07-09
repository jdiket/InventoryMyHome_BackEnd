from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class InventoryList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="inventorylist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    inventory_list = models.ForeignKey(InventoryList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    serial = models.IntegerField(default=0)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name