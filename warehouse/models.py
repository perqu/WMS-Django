from django.db import models
from products.models import Product


class Warehouse(models.Model):
    name = models.CharField(max_length=100)


class Zone(models.Model):
    name = models.CharField(max_length=100)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)


class Rack(models.Model):
    name = models.CharField(max_length=100)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)


class Shelf(models.Model):
    name = models.CharField(max_length=100)
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)


class ProductStorageLink(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    quantity = models.IntegerField()
