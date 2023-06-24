from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import SignUpSerializer
from rest_framework.authtoken.models import Token


class SignUpView(generics.GenericAPIView):
    """
    API view for user sign-up.

    Serializer Class:
    - SignUpSerializer: Serializer used for validating and creating user accounts.

    Permissions:
    - None: No specific permissions required.

    Supported HTTP Methods:
    - POST: Create a new user account with provided data in the request body.

    Returns:
    - HTTP 201 Created: If the user account is successfully created.
      Response format: {"message": "User Created Successfully", "data": serialized_user_data}

    - HTTP 400 Bad Request: If the provided data is invalid or fails validation.
      Response format: Serialized error data with details about the validation errors.
    """

    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "User Created Successfully", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = []

    def post(self, request: Request):
        """
        Handles the login process for users.

        Receives the username and password from the request data.
        Authenticates the user using the provided credentials.
        If authentication is successful, generates or retrieves the user's token.
        Returns a response with the message "Login Successful" and the user's token.

        If authentication fails, returns a response with the message "Invalid username or password".

        :param request: The HTTP request object.
        :type request: Request
        :return: The HTTP response object.
        :rtype: Response
        """

        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)

            response = {"message": "Login Successful", "token": token.key}

            return Response(data=response, status=status.HTTP_200_OK)

        else:
            response = {"message": "Invalid username or password"}

            return Response(data=response)

    def get(self, request: Request):
        """
        Handles the GET request for retrieving user information.

        Returns a response containing the user's information and authentication details.

        :param request: The HTTP request object.
        :type request: Request
        :return: The HTTP response object.
        :rtype: Response
        """

        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)
