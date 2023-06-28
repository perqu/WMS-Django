from django.test import TestCase
from decimal import Decimal
from ..models import Product
from ..serializers import ProductSerializer


class ProductSerializerTest(TestCase):
    def setUp(self):
        self.product_data = {
            "name": "Test Product",
            "code": "TP001",
            "description": "This is a test product",
            "price": "9.99",
        }

    def test_product_serializer_with_valid_data(self):
        serializer = ProductSerializer(data=self.product_data)
        self.assertTrue(serializer.is_valid())

    def test_product_serializer_with_missing_required_field(self):
        data_without_name = self.product_data.copy()
        del data_without_name["name"]
        serializer = ProductSerializer(data=data_without_name)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors["name"][0], "This field is required.")

    def test_product_serializer_with_invalid_price(self):
        data_with_invalid_price = self.product_data.copy()
        data_with_invalid_price["price"] = "invalid_price"
        serializer = ProductSerializer(data=data_with_invalid_price)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors["price"][0], "A valid number is required.")

    def test_product_serializer_create(self):
        serializer = ProductSerializer(data=self.product_data)
        self.assertTrue(serializer.is_valid())
        product = serializer.save()

        self.assertIsInstance(product, Product)
        self.assertEqual(product.name, self.product_data["name"])
        self.assertEqual(product.code, self.product_data["code"])
        self.assertEqual(product.description, self.product_data["description"])
        self.assertEqual(product.price, Decimal(self.product_data["price"]))
