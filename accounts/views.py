# accounts/views.py
from rest_framework import generics, permissions
from .serializers import RegisterSerializer

class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    throttle_scope = "auth"  # Throttle scoped
