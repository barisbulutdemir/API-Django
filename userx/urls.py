from django.urls import path
from .views import UserListAPIView, get_user_by_id

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('<str:pk>/', get_user_by_id, name='user'),
]
