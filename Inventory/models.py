from django.db import models

# Create your models here.

class InventoryList(models.Model):
    owner = models.CharField(max_length=200)
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