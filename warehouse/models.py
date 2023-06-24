from django.db import models
from products.models import Product


class StoragePlace(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    localization = models.CharField(max_length=200)


class ProductStorageLink(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    storage_place_id = models.ForeignKey(StoragePlace, on_delete=models.CASCADE)
    quantity = models.IntegerField()
