from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import SignUpView


class TestUrls(SimpleTestCase):
    def test_products_url(self):
        url = reverse("signup")
        self.assertEqual(resolve(url).func.view_class, SignUpView)
