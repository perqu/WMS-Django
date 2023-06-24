from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import ProductListCreateView, ProductRetrieveUpdateDeleteView


class TestUrls(SimpleTestCase):
    def test_products_url(self):
        url = reverse("products")
        self.assertEqual(resolve(url).func.view_class, ProductListCreateView)

    def test_product_detail_url(self):
        url = reverse("product-detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, ProductRetrieveUpdateDeleteView)
