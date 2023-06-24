from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import index


class TestUrls(SimpleTestCase):
    def test_products_url(self):
        url = reverse("index")
        self.assertEqual(resolve(url).func, index)
