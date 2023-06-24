from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError

from .models import User


class SignUpSerializer(serializers.ModelSerializer):

    """
    Serializer for user sign-up.

    Fields:
    - email: Email field for the user's email address.
    - username: Char field for the user's username.
    - password: Char field for the user's password (write-only).

    Model:
    - User: The User model used for creating new user accounts.

    Validation:
    - Checks if the provided email and username are already used by existing users.
    - Raises a ValidationError if the email or username is already used.

    Creation:
    - Creates a new user account with the validated data.
    - Hashes and sets the user's password using set_password() method.

    Note: This serializer does not handle authentication or login. It is specifically
    designed for the sign-up process.

    Usage:
    - Typically used in combination with a sign-up view or endpoint to handle
      user registration and account creation.
    """

    email = serializers.EmailField()
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, max_length=20, write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def validate(self, attrs):
        email = User.objects.filter(email=attrs["email"]).exists()
        username = User.objects.filter(username=attrs["username"]).exists()

        if email:
            raise ValidationError("Email has already been used")

        if username:
            raise ValidationError("Username has already been used")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        return user
