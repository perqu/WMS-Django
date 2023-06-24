from ..serializers import SignUpSerializer
from rest_framework.test import APITestCase
from users.models import User


class SignUpSerializerTest(APITestCase):
    def test_valid_data(self):
        data = {
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpassword",
        }
        serializer = SignUpSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_missing_required_fields(self):
        data = {}  # Puste dane - brak wymaganych pól
        serializer = SignUpSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)
        self.assertIn("username", serializer.errors)
        self.assertIn("password", serializer.errors)

    def test_duplicate_username(self):
        User.objects.create(username="existinguser", email="existing@example.com")

        data = {
            "email": "newuser@example.com",
            "username": "existinguser",  # Próba użycia istniejącej nazwy użytkownika
            "password": "testpassword",
        }
        serializer = SignUpSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("Username has already been used", str(serializer.errors))

    def test_duplicate_email(self):
        User.objects.create(username="existinguser", email="existing@example.com")

        data = {
            "email": "existing@example.com",
            "username": "testuser",
            "password": "testpassword",
        }
        serializer = SignUpSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("Email has already been used", str(serializer.errors))

    def test_invalid_email(self):
        data = {
            "email": "invalid_email",
            "username": "testuser",
            "password": "testpassword",
        }
        serializer = SignUpSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", str(serializer.errors))
