# views.py in your application directory

from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework.response import Response
from rest_framework.decorators import api_view




User = get_user_model()

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def get_user_by_id(request, pk):
    try:
        user = User.objects.get(id=pk)
        return Response({"username": user.username, "bio": user.bio, "phone_number": user.phone_number})
    except CustomUser.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
    
