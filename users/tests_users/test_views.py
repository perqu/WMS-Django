from django.test import TestCase, RequestFactory
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse
from ..views import SignUpView
from ..models import User


class SignUpViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_signup_success(self):
        data = {
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpassword",
        }
        request = self.factory.post("/signup/", data)
        view = SignUpView.as_view()

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "User Created Successfully")
        self.assertEqual(response.data["data"]["email"], "test@example.com")
        self.assertEqual(response.data["data"]["username"], "testuser")

    def test_signup_failure(self):
        data = {
            "email": "invalid_email",
            "username": "",
            "password": "short",
        }
        request = self.factory.post("/signup/", data)
        view = SignUpView.as_view()

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {
            "username": "testuser",
            "password": "testpassword",
            "email": "test@example.com",
        }
        cls.user = User.objects.create_user(**cls.user_data)
        cls.token = Token.objects.create(user=cls.user)

    def test_post_login_successful(self):
        url = reverse("login")
        data = {
            "username": "testuser",
            "password": "testpassword",
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Login Successful")
        self.assertEqual(response.data["token"], self.token.key)

    def test_post_invalid_credentials(self):
        url = reverse("login")
        data = {
            "username": "testuser",
            "password": "wrongpassword",
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Invalid username or password")
        self.assertNotIn("token", response.data)

    def test_get_user_information(self):
        url = reverse("login")
        response = self.client.get(url, HTTP_AUTHORIZATION="Token " + self.token.key)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["auth"], str(self.token))

    def test_get_unauthenticated_user_information(self):
        url = reverse("login")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], "AnonymousUser")
        self.assertIn("None", response.data["auth"])
