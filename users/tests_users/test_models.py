from django.test import TestCase
from ..models import User


class UserModelTestCase(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            email="test@example.com", password="testpassword"
        )

        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("testpassword"))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(
            email="admin@example.com", password="adminpassword"
        )

        self.assertEqual(superuser.email, "admin@example.com")
        self.assertTrue(superuser.check_password("adminpassword"))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
