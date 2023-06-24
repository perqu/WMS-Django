from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class CustomUserManager(BaseUserManager):

    """
    Custom user manager for creating and managing user accounts.

    Methods:
    - create_user(email, password, **extra_fields): Creates a regular user account.
    - create_superuser(email, password, **extra_fields): Creates a superuser account.

    Model:
    - User: The user model associated with this user manager.

    Fields:
    - email: Char field for the user's email address.
    - username: Char field for the user's username.
    - date_of_birth: Date field for the user's date of birth.

    User Creation:
    - Normalizes the email address and creates a new user account with the provided data.
    - Sets the user's password using set_password() method.

    Superuser Creation:
    - Creates a superuser account with the provided data and additional superuser permissions.
    - Validates and ensures that the is_staff and is_superuser flags are set to True.

    Usage:
    - Typically used as the manager for the User model to handle user account creation
      and management operations.
    """

    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):

    """
    Custom user model for storing user information.

    Fields:
    - email: Char field for the user's email address.
    - username: Char field for the user's username.
    - date_of_birth: Date field for the user's date of birth.

    Manager:
    - CustomUserManager: The custom user manager associated with this user model.

    Note: This user model inherits from AbstractUser, providing the default fields and
    functionality from the Django built-in user model. Additional fields and customizations
    can be added as needed.
    """

    email = models.CharField(max_length=80, unique=True)
    username = models.CharField(max_length=45, unique=True)
    date_of_birth = models.DateField(null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username
