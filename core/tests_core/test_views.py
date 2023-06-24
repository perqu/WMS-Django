from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):
    def test_index_view_returns_status_200(self):
        # Sprawdź, czy strona główna zwraca poprawny status odpowiedzi 200 OK
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        # Sprawdź, czy strona główna używa poprawnego szablonu "core/index.html"
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "core/index.html")
