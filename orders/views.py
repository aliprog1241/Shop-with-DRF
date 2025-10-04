# orders/views.py
from rest_framework import generics, permissions
from rest_framework.throttling import ScopedRateThrottle
from .models import Order
from .serializers import OrderSerializer, OrderCreateSerializer
from .permissions import IsOrderOwner

class OrderListAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_scope = "products"  # همان نرخ عمومی
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("-created_at")

class OrderRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrderOwner]

class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_scope = "products"

    def perform_create(self, serializer):
        serializer.save()
