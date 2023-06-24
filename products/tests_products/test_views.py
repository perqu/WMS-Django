from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from ..models import Product
from decimal import Decimal
from django.contrib.auth import get_user_model

User = get_user_model()


class ProductAPITest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser", password="testpassword", email="testuser@example.com"
        )
        cls.token = Token.objects.create(user=cls.user)

        cls.product_data = {
            "name": "Product 1",
            "code": "ABC123",
            "description": "Test product",
            "price": "9.99",
        }
        cls.product = Product.objects.create(**cls.product_data)

    def test_get_product_list(self):
        url = reverse("products")
        response = self.client.get(url, HTTP_AUTHORIZATION="Token " + self.token.key)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], self.product_data["name"])

    def test_create_product(self):
        url = reverse("products")
        data = {
            "name": "New Product",
            "code": "ABC123",
            "description": "Test product",
            "price": "9.99",
        }
        response = self.client.post(
            url, data, format="json", HTTP_AUTHORIZATION="Token " + self.token.key
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "New Product")

        # Check if the product was created in the database
        created_product = Product.objects.get(id=response.data["id"])
        self.assertEqual(created_product.name, "New Product")


class ProductDetailAPITest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser", password="testpassword", email="testuser@example.com"
        )
        cls.token = Token.objects.create(user=cls.user)

        cls.product_data = {
            "name": "Product 1",
            "code": "ABC123",
            "description": "Test product",
            "price": "9.99",
        }
        cls.product = Product.objects.create(**cls.product_data)

    def test_get_product_detail(self):
        url = reverse("product-detail", args=[self.product.id])
        response = self.client.get(url, HTTP_AUTHORIZATION="Token " + self.token.key)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.product_data["name"])

    def test_update_product(self):
        url = reverse("product-detail", args=[self.product.id])
        data = {"price": "19.99"}
        response = self.client.put(
            url,
            data,
            content_type="application/json",
            HTTP_AUTHORIZATION="Token " + self.token.key,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the product price was updated in the database
        updated_product = Product.objects.get(id=self.product.id)
        self.assertEqual(updated_product.price, Decimal("19.99"))

    def test_delete_product(self):
        url = reverse("product-detail", args=[self.product.id])
        response = self.client.delete(url, HTTP_AUTHORIZATION="Token " + self.token.key)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check if the product was deleted from the database
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=self.product.id)
