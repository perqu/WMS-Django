from django.test import TestCase
from ..models import Product


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            name="Test Product",
            code="ABC123",
            description="Test description",
            price="9.99",
        )

    def test_name_field(self):
        product = Product.objects.get(id=1)
        field = product._meta.get_field("name")
        self.assertEqual(field.max_length, 100)
        self.assertFalse(field.null)

    def test_code_field(self):
        product = Product.objects.get(id=1)
        field = product._meta.get_field("code")
        self.assertEqual(field.null, True)

    def test_description_field(self):
        product = Product.objects.get(id=1)
        field = product._meta.get_field("description")
        self.assertEqual(field.null, True)

    def test_price_field(self):
        product = Product.objects.get(id=1)
        field = product._meta.get_field("price")
        self.assertEqual(field.max_digits, 10)
        self.assertEqual(field.decimal_places, 2)

    def test_image_field(self):
        product = Product.objects.get(id=1)
        field = product._meta.get_field("image")
        self.assertEqual(field.upload_to, "static/imgs/products")
        self.assertEqual(field.null, True)

    def test_created_at_field(self):
        product = Product.objects.get(id=1)
        field = product._meta.get_field("created_at")
        self.assertTrue(field.auto_now_add)

    def test_updated_at_field(self):
        product = Product.objects.get(id=1)
        field = product._meta.get_field("updated_at")
        self.assertTrue(field.auto_now)
