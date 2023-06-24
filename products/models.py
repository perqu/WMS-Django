from django.db import models


class Product(models.Model):
    """
    Model representing a product.

    Fields:
        - name (str): Represents the name of the product.
        - code (str, optional): Represents the code of the product. It can be a text value.
        - description (str, optional): Represents the description of the product. It can be a text value.
        - price (Decimal): Represents the price of the product as a Decimal value.
        - image (ImageField, optional): Represents the product image that will be uploaded to the "static/imgs/products" directory.
        - created_at (DateTimeField): Represents the date and time when the product was created. Set automatically on creation.
        - updated_at (DateTimeField): Represents the date and time of the last update to the product. Automatically updated.
    """

    name = models.CharField(max_length=100)
    code = models.TextField(null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="static/imgs/products", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"
        ordering = ["name"]
