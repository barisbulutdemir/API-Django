# views.py in your application directory

from django.contrib.auth import get_user_model
from rest_framework.response import Response

# Rest Framework permissions and generics for views
from rest_framework import permissions, generics

# SimpleJWT for creating tokens
from rest_framework_simplejwt.tokens import RefreshToken

# Our custom serializer
from .serializers import UserSerializer

# Get the User model
User = get_user_model()

# List all the users
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Register a new user
class RegisterView(generics.GenericAPIView):
    # Anyone can register a new user
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        # Parse the request data
        serializer = self.get_serializer(data=request.data)

        # Validate the data
        serializer.is_valid(raise_exception=True)

        # Save the user and get a User model instance
        user = serializer.save()

        # Create a JWT refresh token for the user
        refresh = RefreshToken.for_user(user)

        # Prepare the response data
        res = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        # Return the tokens
        return Response(res, status=201)

# Log in a user
class LoginView(generics.GenericAPIView):
    # Anyone can log in
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        # Parse the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Get the user by username
        user = User.objects.filter(username=username).first()

        # If there's no such user, return an error
        if user is None:
            return Response({'detail': 'User not found'}, status=404)

        # If the password is incorrect, return an error
        if not user.check_password(password):
            return Response({'detail': 'Wrong password'}, status=400)

        # Create a JWT refresh token for the user
        refresh = RefreshToken.for_user(user)

        # Prepare the response data
        res = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        # Return the tokens
        return Response(res, status=200)
